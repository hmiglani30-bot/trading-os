import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CandidateTests(unittest.TestCase):
    def test_registry_paths_and_capability_ids(self):
        registry = yaml.safe_load((ROOT / "runtime" / "capability_registry.yaml").read_text(encoding="utf-8"))
        seen = set()
        for skill_name, skill in registry["skills"].items():
            path = Path(skill["path"])
            self.assertTrue((ROOT.parent / path).exists(), f"missing skill path for {skill_name}: {path}")
            for capability_id in skill["capabilities"]:
                self.assertNotIn(capability_id, seen, f"duplicate capability {capability_id}")
                seen.add(capability_id)
        for plan_name, plan in registry.get("default_plans", {}).items():
            for key in ("start_with", "always_check", "add_if_needed"):
                for capability_id in plan.get(key, []):
                    self.assertIn(capability_id, seen, f"{plan_name} references unknown {capability_id}")

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
