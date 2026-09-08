"""Structural checks for preserved full-analysis records; not an investment-quality score."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

CORE_SKILLS = ("market_regime", "fundamental_fair_value", "technical_entry_timing")
RESEARCH_START = "<!-- RESEARCH_RECORD_START -->"
RESEARCH_END = "<!-- RESEARCH_RECORD_END -->"
PACKET_KEYS = {
    "market_regime": ("as_of", "cutoff", "mode", "regime_label", "confidence", "growth", "inflation", "policy_liquidity", "rates_credit", "equity_tape", "leadership", "what_changed", "scenario_probabilities", "watchlist_transmission", "event_calendar", "decision_posture", "risk_flags", "missing_data", "source_notes"),
    "fundamental_fair_value": ("ticker", "as_of", "current_price", "research_cutoff", "business_quality", "financial_quality", "expectations_gap", "valuation", "catalysts", "invalidation", "fundamental_stance", "ownership_quality", "entry_attractiveness", "covered_call_compatibility", "missing_data", "source_notes"),
    "technical_entry_timing": ("ticker", "as_of", "data_cutoff", "timeframes", "input_quality", "multi_timeframe_trend", "setup_class", "volatility_regime", "levels", "entry_plan", "covered_call_context", "setup_score", "entry_suitability", "missing_data", "source_notes"),
}


def core_capabilities(root: Path) -> list[str]:
    registry = yaml.safe_load((root / "runtime/capability_registry.yaml").read_text())
    return [cap for name in CORE_SKILLS for cap in registry["skills"][name]["capabilities"]]


def validate_current_pointer(pointer: dict) -> None:
    if pointer.get("schema_version") != 1 or pointer.get("repository") != "hmiglani30-bot/trading-os":
        raise ValueError("Unsupported current-source pointer")
    ref = pointer.get("active_ref")
    if not isinstance(ref, str) or not ref.strip() or any(c.isspace() for c in ref):
        raise ValueError("Current source requires a nonempty Git ref")
    for key in ("entry_point", "full_stock_analysis"):
        p = pointer.get(key)
        if not isinstance(p, str) or not p or Path(p).is_absolute() or ".." in Path(p).parts:
            raise ValueError("Current-source paths must stay inside the repository")


def source_manifest(root: Path) -> dict:
    paths = [root.parent / "TRADING_OS_CURRENT.json", root.parent / "START_HERE.md",
             root / "runtime/adaptive_planner.md", root / "runtime/capability_registry.yaml",
             root / "workflows/full_stock_analysis.md", root / "schemas/research_record.schema.json"]
    paths += sorted((root / "skills").glob("*.md"))
    paths += [root / "runtime/run_adaptive.py", root / "runtime/full_analysis.py"]
    hashes = {str(p.relative_to(root.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.exists()}
    def git(*args):
        try:
            return subprocess.check_output(["git", "-C", str(root.parent), *args], stderr=subprocess.DEVNULL, text=True).strip()
        except (OSError, subprocess.CalledProcessError):
            return None
    commit = git("rev-parse", "HEAD")
    status = git("status", "--porcelain")
    return {"git_commit": commit, "working_tree_dirty": bool(status) if status is not None else None,
            "file_sha256": hashes,
            "freshness": "local_checkout_only; resolve default-branch pointer before calling this latest"}


def validate_full_analysis(root: Path, planning: dict, research: dict) -> dict:
    schema = json.loads((root / "schemas/research_record.schema.json").read_text())
    errors = ["research." + ".".join(map(str, e.absolute_path)) + ": " + e.message
              for e in Draft202012Validator(schema).iter_errors(research)]
    plan_schema = json.loads((root / "schemas/planning_record.schema.json").read_text())
    errors += ["planning." + ".".join(map(str, e.absolute_path)) + ": " + e.message
               for e in Draft202012Validator(plan_schema).iter_errors(planning)]
    if errors:
        return {"status": "invalid", "errors": errors, "limitations": []}
    if planning["depth"] != "deep":
        errors.append("Full stock analysis requires deep depth")
    required = set(core_capabilities(root))
    selected = set(planning["selected_capabilities"])
    registry = yaml.safe_load((root / "runtime/capability_registry.yaml").read_text())
    owners = {cap: name for name, spec in registry["skills"].items() for cap in spec["capabilities"]}
    if not selected <= set(owners):
        errors.append("Unknown selected capabilities: " + ", ".join(sorted(selected - set(owners))))
    if not required <= selected:
        errors.append("Core capabilities missing from plan: " + ", ".join(sorted(required - selected)))
    stages = {s["skill"]: s for s in research["stages"]}
    if len(stages) != len(research["stages"]):
        errors.append("Duplicate specialist stage")
    for skill in CORE_SKILLS:
        if skill not in stages:
            errors.append("Missing specialist stage: " + skill)
        else:
            absent = set(PACKET_KEYS[skill]) - set(stages[skill]["packet"])
            if absent:
                errors.append(skill + " packet missing fields: " + ", ".join(sorted(absent)))
    for name, stage in stages.items():
        sources = {s["id"] for s in stage["sources"]}
        findings = {f["id"]: f for f in stage["findings"]}
        if len(sources) != len(stage["sources"]) or len(findings) != len(stage["findings"]):
            errors.append(name + " has duplicate source or finding IDs")
        if stage["status"] == "complete" and not findings:
            errors.append(name + " claims completion without findings")
        if stage["status"] == "blocked" and not stage["missing_inputs"]:
            errors.append(name + " is blocked without naming missing inputs")
        for finding in findings.values():
            if not set(finding["source_ids"]) <= sources:
                errors.append(name + " finding references an unknown source")
            if finding["kind"] in {"fact", "management_claim"} and not finding["source_ids"]:
                errors.append(name + " factual finding lacks a source")
    rows = {r["capability_id"]: r for r in research["coverage"]}
    if len(rows) != len(research["coverage"]):
        errors.append("Duplicate capability coverage")
    if not selected <= set(rows):
        errors.append("Selected capabilities lack coverage: " + ", ".join(sorted(selected - set(rows))))
    limitations = []
    for cap, row in rows.items():
        if cap not in owners or owners[cap] != row["stage"]:
            errors.append(cap + " is not mapped to its owning specialist")
        stage = stages.get(row["stage"])
        if stage is None:
            errors.append(cap + " references a missing stage")
            continue
        findings = {f["id"]: f for f in stage["findings"]}
        if not set(row["finding_ids"]) <= set(findings):
            errors.append(cap + " references a missing finding")
        if row["status"] == "covered":
            if not row["finding_ids"] or not any(findings.get(i, {}).get("source_ids") for i in row["finding_ids"]):
                errors.append(cap + " claims coverage without a source-backed finding")
        if row["status"] in {"partial", "blocked"}:
            limitations.append(cap + ": " + row["reason"])
    if any(s["status"] != "complete" for s in stages.values()):
        limitations.append("One or more specialist stages are incomplete")
    return {"status": "invalid" if errors else ("partial" if limitations else "structurally_complete"),
            "errors": errors, "limitations": limitations,
            "meaning": "Structural checks do not certify evidence truth, analytical sufficiency or future returns"}


def research_output_instruction(root: Path) -> str:
    return f"""
FULL-ANALYSIS OUTPUT CONTRACT
Use deep depth. Select these core capability IDs: {json.dumps(core_capabilities(root))}.
Preserve each stage's detailed findings in report appendices before final compression.
In addition to planning, decision and voice blocks, include:
{RESEARCH_START}
A JSON object conforming exactly to the following schema:
{(root / 'schemas/research_record.schema.json').read_text()}
Native packet keys required per core specialist (null is permitted only with a named data gap):
{json.dumps(PACKET_KEYS)}
{RESEARCH_END}
Do not include the schema itself in the returned record. Fill it with actual findings,
sources, assumptions, contrary evidence, native packets and coverage statuses.
Missing evidence must remain partial or blocked. Never invent coverage.
"""
