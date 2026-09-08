import json
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("run_adaptive", ROOT / "runtime" / "run_adaptive.py")
RUNTIME = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNTIME)


class CandidateTests(unittest.TestCase):
    def test_registry_paths_and_capability_ids(self):
        registry = yaml.safe_load((ROOT / "runtime" / "capability_registry.yaml").read_text(encoding="utf-8"))
        seen = set()
        for skill_name, skill in registry["skills"].items():
            path = Path(skill["path"])
            self.assertTrue((ROOT.parent / path).exists(), f"missing skill path for {skill_name}: {path}")
            headings = {
                line.lstrip("#").strip()
                for line in (ROOT.parent / path).read_text(encoding="utf-8").splitlines()
                if line.startswith("#")
            }
            for capability_id, capability in skill["capabilities"].items():
                self.assertNotIn(capability_id, seen, f"duplicate capability {capability_id}")
                self.assertIn(capability["section"], headings, f"missing section for {capability_id}")
                seen.add(capability_id)
        for plan_name, plan in registry.get("default_plans", {}).items():
            for key in ("start_with", "always_check", "add_if_needed"):
                for capability_id in plan.get(key, []):
                    self.assertIn(capability_id, seen, f"{plan_name} references unknown {capability_id}")
        scout = registry["entry_points"]["scout"]
        self.assertEqual(scout["path"], registry["skills"]["scout"]["path"])
        self.assertIn(scout["default_plan"], registry["default_plans"])

    def test_run_scout_routes_and_loads_evidence_without_portfolio(self):
        for request in ("Run Scout", " scout ", "Run Scout across unfamiliar sectors"):
            self.assertEqual(RUNTIME.resolve_workflow(request), "scout")
        self.assertEqual(RUNTIME.resolve_workflow("Review AMD"), "adaptive")
        self.assertEqual(RUNTIME.resolve_workflow("Find new stocks", "scout"), "scout")
        self.assertEqual(RUNTIME.resolve_workflow("Run Scout", "adaptive"), "adaptive")
        prompt = RUNTIME.build_prompt(
            ROOT, {}, "Run Scout", None, None, None,
            scout_evidence={"reported_match_count": 500, "rows_returned": 2, "token": "private-token"},
        )
        self.assertIn("Primary prompt: scout.md", prompt)
        self.assertIn("<SKILL name='scout.md'>", prompt)
        self.assertIn('"rows_returned": 2', prompt)
        self.assertIn('"reported_match_count": 500', prompt)
        self.assertIn("PRIVATE PORTFOLIO INPUT\nUNAVAILABLE", prompt)
        self.assertNotIn("private-token", prompt)

    def test_scout_cli_selects_scout_and_marks_demo_truthfully(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "runs"
            evidence = Path(tmp) / "scout.json"
            evidence.write_text('{"rows_returned": 2}', encoding="utf-8")
            subprocess.run([
                sys.executable, str(ROOT / "runtime" / "run_adaptive.py"),
                "--workflow", "scout", "--scout-evidence-file", str(evidence),
                "--output-root", str(out), "--demo",
            ], check=True)
            latest = out / "latest"
            manifest = json.loads((latest / "run_manifest.json").read_text())
            planning = json.loads((latest / "planning_record.json").read_text())
            self.assertEqual(manifest["request"], "Run Scout")
            self.assertEqual(manifest["workflow"], "scout")
            self.assertTrue(manifest["demo"])
            self.assertTrue(manifest["scout_evidence_supplied"])
            self.assertFalse(manifest["portfolio_supplied"])
            self.assertIn("SCOUT.DISCOVER", planning["selected_capabilities"])
            self.assertIn("zero stocks were screened", (latest / "report.md").read_text())

    def test_demo_runner_emits_browser_and_ledger_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "runs"
            cmd = [
                sys.executable,
                str(ROOT / "runtime" / "run_adaptive.py"),
                "--root", str(ROOT),
                "--config", str(ROOT / "config" / "runtime.example.yaml"),
                "--request", "What should I do today?",
                "--output-root", str(out),
                "--demo",
            ]
            subprocess.run(cmd, check=True)
            latest = out / "latest"
            required = {
                "report.md",
                "report.html",
                "planning_record.json",
                "decision_record.json",
                "voice_summary.txt",
                "run_manifest.json",
                "response_dump.json",
            }
            self.assertTrue(required.issubset({p.name for p in latest.iterdir()}))
            planning = json.loads((latest / "planning_record.json").read_text(encoding="utf-8"))
            decision = json.loads((latest / "decision_record.json").read_text(encoding="utf-8"))
            self.assertEqual(planning["depth"], "scan")
            self.assertEqual(decision["confidence"], "low")
            self.assertIn("<html", (latest / "report.html").read_text(encoding="utf-8").lower())

    def test_v1_does_not_delete_legacy_prompts(self):
        legacy = ROOT.parent / "prompts"
        expected = [legacy / f"p{i:02d}_" for i in range(13)]
        names = [p.name for p in legacy.glob("p*.md")]
        for i in range(13):
            self.assertTrue(any(name.startswith(f"p{i:02d}_") for name in names), f"legacy P{i:02d} missing")


if __name__ == "__main__":
    unittest.main()
