# Prompt Scorecard

Use this scorecard before calling a prompt or workflow production-ready.

## Scoring method

Score each dimension from 1 to 5.

| Dimension | What good looks like | Score |
|---|---|---:|
| Input contract | Required inputs are explicit and missing data is flagged | |
| Source discipline | Uses the correct source tier and avoids unsupported claims | |
| Factual grounding | Distinguishes facts, assumptions, interpretation, and judgment | |
| Research depth | Covers the relevant macro, equity, technical, event, portfolio, or options lens | |
| Scenario quality | Provides plausible scenarios with triggers and invalidation | |
| Risk framing | Identifies what can go wrong and what data could change the view | |
| Decision usefulness | Clarifies what matters without creating automated account instructions | |
| Output readability | Works as Markdown, HTML, and PDF | |
| Workflow composability | Can feed into a combined workflow cleanly | |
| Learning loop | Produces improvements, failure logs, or test cases | |

## Rating bands

| Average score | Rating | Action |
|---:|---|---|
| 4.5–5.0 | Excellent | Production-ready |
| 4.0–4.4 | Strong | Use, then review after live tests |
| 3.5–3.9 | Usable | Revise before broad use |
| 3.0–3.4 | Weak | Rewrite |
| Below 3.0 | Not acceptable | Retire or redesign |

## Required v1 test workflows

Before calling Trading OS v1 ready, run and score:

1. Daily brief with a watchlist.
2. Weekly review with a sanitized holdings snapshot.
3. Options overlay scenario review with a real option-chain snapshot.

## Eval template

```markdown
# Prompt Eval — <Prompt or Workflow>

**Date:** YYYY-MM-DD  
**Evaluator:**  
**Test case:**  
**Inputs used:**  
**Missing inputs:**  

| Dimension | Score 1–5 | Notes |
|---|---:|---|
| Input contract | | |
| Source discipline | | |
| Factual grounding | | |
| Research depth | | |
| Scenario quality | | |
| Risk framing | | |
| Decision usefulness | | |
| Output readability | | |
| Workflow composability | | |
| Learning loop | | |

## Overall score

## What worked

## What failed

## Required prompt changes

## Follow-up test case
```
