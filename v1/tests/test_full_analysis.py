import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from full_analysis import CORE_SKILLS, PACKET_KEYS, core_capabilities, validate_current_pointer, validate_full_analysis
from run_adaptive import build_prompt, resolve_workflow


def valid_fixture():
    caps = core_capabilities(ROOT)
    planning = dict(decision_intents=["single_stock_ownership"], selected_capabilities=caps,
                    omitted_capabilities_checked=[], capabilities_added_after_coverage_audit=[],
                    depth="deep", missing_inputs=[], reasoning_summary="Synthetic validation fixture")
    stages = []
    for skill in CORE_SKILLS:
        stages.append(dict(skill=skill, status="complete", as_of="2026-01-01T00:00:00Z",
             horizon="12 months", findings=[dict(id="f1", claim="Synthetic documented fact", kind="fact", source_ids=["s1"])],
             sources=[dict(id="s1", title="Synthetic fixture", reference="fixture:public-example", cutoff="2026-01-01")],
             assumptions=[], counterarguments=[], missing_inputs=[], reversal_conditions=["Changed fixture"],
             packet={key: "synthetic" for key in PACKET_KEYS[skill]}))
    names = dict(MARKET="market_regime", FUND="fundamental_fair_value", TECH="technical_entry_timing")
    rows = [dict(capability_id=cap,status="covered",stage=names[cap.split(".")[0]],finding_ids=["f1"],
                 reason="Synthetic evidence",decision_impact="Fixture only",could_flip_decision=False) for cap in caps]
    research = dict(schema_version=1,stages=stages,coverage=rows,
                    synthesis=dict(dominant_reason="Synthetic fixture",conflicts=[],decision_dependencies=["f1"]))
    return planning,research


class FullAnalysisTests(unittest.TestCase):
    def test_command_aliases_and_override(self):
        for q in ("@full-stock-analysis CBRS", "$full-stock-analysis AMD",
                  "/full stock analysis CBRS — compare 1000 shares", "Run full stock analysis WDC"):
            self.assertEqual(resolve_workflow(q), "full_stock_analysis")
        self.assertEqual(resolve_workflow("review CBRS"), "adaptive")
        self.assertEqual(resolve_workflow("Run Scout"), "scout")
        self.assertEqual(resolve_workflow("/full-stock-analysis CBRS", "adaptive"), "adaptive")

    def test_full_prompt_retains_custom_request_and_research_contract(self):
        request="@full-stock-analysis CBRS; compare 1000 and 2000 shares; protect tax cash."
        p=build_prompt(ROOT,{},request,None,None,None)
        self.assertIn(request,p)
        self.assertIn("RESEARCH_RECORD_START",p)
        self.assertIn("no report-wide word ceiling",p)
        self.assertNotIn("Normal report ceiling: 2200 words",p)

    def test_missing_research_cannot_pass(self):
        plan,_=valid_fixture()
        self.assertEqual(validate_full_analysis(ROOT,plan,{})["status"],"invalid")

    def test_missing_selected_coverage_and_dangling_sources_fail(self):
        plan,r=valid_fixture()
        r["coverage"].pop()
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"invalid")
        plan,r=valid_fixture()
        r["stages"][0]["findings"][0]["source_ids"]=["absent"]
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"invalid")

    def test_no_silent_depth_or_native_packet_downgrade(self):
        plan,r=valid_fixture()
        plan["depth"]="standard"
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"invalid")
        plan,r=valid_fixture()
        del r["stages"][1]["packet"]["valuation"]
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"invalid")

    def test_blocked_coverage_is_reported_as_partial(self):
        plan,r=valid_fixture()
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"structurally_complete")
        r["coverage"][0].update(status="blocked",finding_ids=[],reason="Missing input")
        r["stages"][0].update(status="partial",missing_inputs=["Current input unavailable"])
        out=validate_full_analysis(ROOT,plan,r)
        self.assertEqual(out["status"],"partial")
        self.assertTrue(out["limitations"])

    def test_current_pointer_paths(self):
        p=json.loads((ROOT.parent/"TRADING_OS_CURRENT.json").read_text())
        validate_current_pointer(p)
        p["full_stock_analysis"]="../other.md"
        with self.assertRaises(ValueError): validate_current_pointer(p)

    def test_unknown_or_wrong_specialist_coverage_fails(self):
        plan,r=valid_fixture()
        plan["selected_capabilities"].append("FAKE.CAPABILITY")
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"invalid")
        plan,r=valid_fixture()
        r["coverage"][0]["stage"]="fundamental_fair_value"
        self.assertEqual(validate_full_analysis(ROOT,plan,r)["status"],"invalid")

    def test_full_demo_never_claims_completed_research(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable,str(ROOT/"runtime/run_adaptive.py"),
                            "--workflow","full_stock_analysis","--request","Full stock analysis CBRS",
                            "--output-root",tmp,"--demo"],check=True,capture_output=True,text=True)
            latest=Path(tmp)/"latest"
            manifest=json.loads((latest/"run_manifest.json").read_text())
            self.assertEqual(manifest["workflow"],"full_stock_analysis")
            self.assertEqual(manifest["validation_status"],"demo")
            self.assertIn("no specialist research",(latest/"report.md").read_text())
            self.assertTrue((latest/"research_record.json").exists())


if __name__=="__main__":
    unittest.main()
