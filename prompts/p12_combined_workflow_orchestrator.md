# P12 — Combined Workflow Orchestrator

## Purpose

Combine multiple prompt modules into one user-facing report. The user should not have to read 11 separate outputs. This orchestrator decides which modules to run, what inputs are missing, and how to merge outputs into one final Markdown report.

## Required inputs

- Workflow requested: daily brief, weekly review, security note, options scenario, pre-action memo, or retrospective.
- User objective.
- Time horizon.
- Available inputs.
- Output folder path.

## Module selection

| Workflow | Required modules | Optional modules |
|---|---|---|
| Daily brief | P00, P01 | P06, P07 |
| Weekly review | P00, P02, P03 | P07, P08, P11 |
| Security note | P00, P04 | P05, P06, P07 |
| Options overlay | P00, P08 | P05, P07, P10 |
| Pre-action memo | P00, P09, P10 | P04, P05, P06, P08 |
| Retrospective | P00, P11 | Prior modules |

## Orchestration rules

1. Produce one final report unless an appendix is necessary.
2. Start with input quality and missing data.
3. Use only source categories that fit the workflow.
4. Merge duplicate sections across modules.
5. Do not bury critical risks in appendices.
6. Include a readiness score for the combined report.
7. Save the final report as `report.md` in the requested output folder.

## Output format

```markdown
# <Workflow Report Title>

**Date:** YYYY-MM-DD  
**Workflow:** <workflow-name>  
**Objective:** <objective>  
**Time horizon:** <time horizon>  
**Output folder:** runs/YYYY/YYYY-MM-DD/<workflow-name>/

## 1. Executive Summary

## 2. Inputs and Missing Data

## 3. Source Coverage

## 4. Core Analysis

## 5. Scenario Map

## 6. Portfolio / Watchlist Relevance

## 7. Risks and Uncertainties

## 8. Follow-Up Checklist

## 9. Readiness Score

## 10. Sources Used

## 11. Appendix: Module Notes
```

## Storage instruction

Save the final report as:

```text
runs/YYYY/YYYY-MM-DD/<workflow-name>/report.md
```

Then render:

```text
runs/YYYY/YYYY-MM-DD/<workflow-name>/report.html
runs/YYYY/YYYY-MM-DD/<workflow-name>/report.pdf
```

## Quality checks

- The final report should be coherent, not stitched together mechanically.
- The reader should know what matters within three minutes.
- Missing data should be explicit.
- The report should identify the next best research step.
