from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import yaml
try:
    import markdown
except ImportError:
    markdown = None
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

PLANNING_START = "<!-- PLANNING_RECORD_START -->"
PLANNING_END = "<!-- PLANNING_RECORD_END -->"
DECISION_START = "<!-- DECISION_RECORD_START -->"
DECISION_END = "<!-- DECISION_RECORD_END -->"
VOICE_START = "<!-- VOICE_SUMMARY_START -->"
VOICE_END = "<!-- VOICE_SUMMARY_END -->"

SKILL_FILES = [
    "market_regime.md",
    "fundamental_fair_value.md",
    "technical_entry_timing.md",
    "portfolio_capital_allocation.md",
    "options_covered_calls.md",
]


def read_json_optional(path: Path | None) -> Any:
    if path is None or not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def redact(value: Any) -> Any:
    blocked = {
        "password", "passcode", "token", "secret", "api_key", "apikey",
        "account_number", "routing_number", "ssn", "social_security_number",
    }
    if isinstance(value, dict):
        return {k: ("[REDACTED]" if str(k).lower() in blocked else redact(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    return value


def extract_block(text: str, start: str, end: str) -> tuple[str, str | None]:
    pattern = re.compile(re.escape(start) + r"\s*(.*?)\s*" + re.escape(end), re.S)
    match = pattern.search(text)
    if not match:
        return text, None
    body = match.group(1).strip()
    body = re.sub(r"^```(?:json|text)?\s*", "", body)
    body = re.sub(r"\s*```$", "", body)
    cleaned = (text[:match.start()] + text[match.end():]).strip()
    return cleaned, body.strip()


def render_html(markdown_text: str, title: str) -> str:
    if markdown is not None:
        body = markdown.markdown(markdown_text, extensions=["tables", "fenced_code"])
    else:
        body = f"<pre>{html.escape(markdown_text)}</pre>"
    return f"""<!doctype html>
<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>{html.escape(title)}</title>
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:1180px;margin:36px auto;padding:0 24px;line-height:1.55;color:#171717}}
h1,h2,h3{{line-height:1.2}} table{{border-collapse:collapse;width:100%;margin:16px 0}} th,td{{border:1px solid #ddd;padding:8px;vertical-align:top}} th{{background:#f6f6f6}} code,pre{{background:#f6f6f6;border-radius:4px}} pre{{padding:12px;overflow:auto}} blockquote{{border-left:4px solid #bbb;margin-left:0;padding-left:14px;color:#444}}
</style></head><body>{body}</body></html>"""


def build_prompt(root: Path, config: dict[str, Any], request: str, portfolio: Any, chains: Any, previous: str | None) -> str:
    planner = (root / "runtime" / "adaptive_planner.md").read_text(encoding="utf-8")
    registry = (root / "runtime" / "capability_registry.yaml").read_text(encoding="utf-8")
    skill_text = []
    for name in SKILL_FILES:
        skill_text.append(f"\n<SKILL name='{name}'>\n{(root / 'skills' / name).read_text(encoding='utf-8')}\n</SKILL>\n")

    watchlist = config.get("watchlist", [])
    max_words = int(config.get("run", {}).get("report_max_words", 2200))
    return f"""
You are executing Trading OS v1 for a real investment-research decision.

USER REQUEST
{request}

USER / RUN CONTEXT
- Timezone: {config.get('user', {}).get('timezone', 'America/Los_Angeles')}
- Watchlist: {json.dumps(watchlist)}
- Normal report ceiling: {max_words} words unless deeper detail is necessary to support a high-stakes decision.

PRIVATE PORTFOLIO INPUT
{json.dumps(redact(portfolio), indent=2) if portfolio is not None else 'UNAVAILABLE'}

PRIVATE OPTION-CHAIN INPUT
{json.dumps(redact(chains), indent=2) if chains is not None else 'UNAVAILABLE'}

PREVIOUS REPORT
{previous if previous else 'UNAVAILABLE'}

INSTRUCTIONS
1. Use the adaptive planner. Do not mechanically run every skill as a full essay.
2. First choose the minimum-sufficient capability IDs from the registry, then research current evidence using web search.
3. Perform the planner's decision-flip coverage audit and add omitted capabilities only if they could materially alter the recommendation.
4. For changing public facts, use current web search and cite sources in the displayed Markdown.
5. Prefer official/primary sources for filings, earnings, macro releases, dates, and company disclosures.
6. Never claim live brokerage access beyond the supplied private snapshot. Do not invent portfolio values, cost bases, option quotes, deltas, IV, or technical indicators.
7. For multi-stock work, use one shared market regime, not one macro essay per ticker.
8. Ownership/desired allocation must precede covered-call strike selection.
9. Treat cash/wait/no-calls as valid actions.
10. Produce ONE decision-first report, not stitched prompt outputs.
11. Keep internal chain-of-thought private. The planning record must contain only a brief user-safe rationale for capability selection.

At the end, include exactly three machine-readable blocks:

{PLANNING_START}
```json
{{
  "decision_intents": [],
  "selected_capabilities": [],
  "omitted_capabilities_checked": [],
  "capabilities_added_after_coverage_audit": [],
  "depth": "scan|standard|deep|audit",
  "missing_inputs": [],
  "reasoning_summary": "brief rationale"
}}
```
{PLANNING_END}

{DECISION_START}
```json
{{
  "decision_id": "",
  "as_of": "ISO-8601",
  "request": "",
  "universe": [],
  "actions": [],
  "market_posture": "",
  "confidence": "low|medium|high",
  "missing_inputs": []
}}
```
{DECISION_END}

{VOICE_START}
A spoken summary of at most 90 words: what matters now, top action(s), and critical warning(s).
{VOICE_END}

<ADAPTIVE_PLANNER>
{planner}
</ADAPTIVE_PLANNER>

<CAPABILITY_REGISTRY>
{registry}
</CAPABILITY_REGISTRY>

{''.join(skill_text)}
""".strip()


def synthetic_report(now: datetime) -> str:
    return f"""# Trading OS Decision Brief — DEMO

**As of:** {now.isoformat()}  
**Status:** Demo only; no live research performed.

> The adaptive planner is installed. A live run selects capability IDs based on the question, current state, and decision-flip audit rather than blindly running five full prompts.

## Read first

- Vague questions such as “What should I do today?” begin with change detection, portfolio state, market regime, and event risk.
- Only material names are escalated into deeper valuation or technical work.
- Covered calls run only after desired ownership is determined.
- Missing live portfolio or chain inputs block precise sizing/strike recommendations rather than causing fabricated precision.

{PLANNING_START}
```json
{{"decision_intents":["demo"],"selected_capabilities":["MARKET.CHANGE","PORT.STATE","PORT.NO_ACTION"],"omitted_capabilities_checked":[],"capabilities_added_after_coverage_audit":[],"depth":"scan","missing_inputs":["live public data","portfolio snapshot","option chain"],"reasoning_summary":"Demo validates the adaptive selection interface only."}}
```
{PLANNING_END}

{DECISION_START}
```json
{{"decision_id":"{uuid.uuid4()}","as_of":"{now.isoformat()}","request":"demo","universe":[],"actions":[{{"action":"wait","reason":"demo has no live inputs"}}],"market_posture":"unavailable","confidence":"low","missing_inputs":["live public data","portfolio snapshot","option chain"]}}
```
{DECISION_END}

{VOICE_START}
Trading OS adaptive planning is installed in demo mode. No live investment recommendation was generated because current portfolio, market, and option-chain inputs were not queried.
{VOICE_END}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--portfolio-file", type=Path)
    parser.add_argument("--option-chain-file", type=Path)
    parser.add_argument("--previous-report", type=Path)
    parser.add_argument("--request", default="")
    parser.add_argument("--output-root", type=Path, default=Path("runs"))
    parser.add_argument("--model", default="gpt-5.6")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8")) if args.config and args.config.exists() else {}
    request = args.request or config.get("run", {}).get("request") or "What should I do today?"
    tz_name = config.get("user", {}).get("timezone", "America/Los_Angeles")
    now = datetime.now(ZoneInfo(tz_name))

    portfolio = read_json_optional(args.portfolio_file)
    chains = read_json_optional(args.option_chain_file)
    previous = args.previous_report.read_text(encoding="utf-8") if args.previous_report and args.previous_report.exists() else None

    if args.demo:
        raw = synthetic_report(now)
        response_dump: dict[str, Any] = {"demo": True}
    else:
        if OpenAI is None:
            raise RuntimeError("openai package is not installed")
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set")
        prompt = build_prompt(root, config, request, portfolio, chains, previous)
        client = OpenAI()
        response = client.responses.create(
            model=args.model,
            reasoning={"effort": args.reasoning_effort},
            tools=[{"type": "web_search", "search_context_size": "high"}],
            include=["web_search_call.action.sources"],
            store=False,
            input=prompt,
        )
        raw = response.output_text
        response_dump = response.model_dump(mode="json")

    displayed, planning_body = extract_block(raw, PLANNING_START, PLANNING_END)
    displayed, decision_body = extract_block(displayed, DECISION_START, DECISION_END)
    displayed, voice_body = extract_block(displayed, VOICE_START, VOICE_END)

    planning = json.loads(planning_body) if planning_body else {"missing": True}
    decision = json.loads(decision_body) if decision_body else {"missing": True}
    voice = voice_body or "Trading OS report is ready."

    run_id = now.strftime("%Y-%m-%dT%H%M%S") + "-" + uuid.uuid4().hex[:8]
    out_root = args.output_root.resolve()
    run_dir = out_root / now.strftime("%Y") / now.strftime("%Y-%m-%d") / run_id
    latest = out_root / "latest"
    run_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "report.md").write_text(displayed.strip() + "\n", encoding="utf-8")
    (run_dir / "report.html").write_text(render_html(displayed, "Trading OS Decision Brief"), encoding="utf-8")
    (run_dir / "planning_record.json").write_text(json.dumps(planning, indent=2), encoding="utf-8")
    (run_dir / "decision_record.json").write_text(json.dumps(decision, indent=2), encoding="utf-8")
    (run_dir / "voice_summary.txt").write_text(voice.strip() + "\n", encoding="utf-8")
    manifest = {
        "run_id": run_id,
        "created_at": now.isoformat(),
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "request": request,
        "portfolio_supplied": portfolio is not None,
        "option_chain_supplied": chains is not None,
        "trading_os_ref": os.environ.get("TRADING_OS_REF", "unknown"),
    }
    (run_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (run_dir / "response_dump.json").write_text(json.dumps(response_dump, indent=2), encoding="utf-8")

    if latest.exists():
        shutil.rmtree(latest)
    shutil.copytree(run_dir, latest)
    print(str(run_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
