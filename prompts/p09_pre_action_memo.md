# P09 — Pre-Action Research Memo

## Purpose

Create a written memo before a meaningful manual financial action. The memo must document thesis, evidence, risk, alternatives, and missing data. It does not execute or instruct account actions.

## Required inputs

- Proposed manual action in the user's words.
- Time horizon.
- Relevant ticker or theme.
- Supporting evidence.
- Portfolio context if provided.
- Risk constraint if provided.

## Source checklist

1. User-provided notes and snapshots.
2. Primary sources for company or macro facts.
3. Dashboard context for market and chart data.
4. News only for recent developments.
5. Prior Trading OS reports if available.

## Output format

```markdown
# Pre-Action Research Memo — <Ticker/Theme>

## 1. Proposed Manual Action
Restate exactly. Do not add instructions.

## 2. Thesis
One paragraph. Include what must be true.

## 3. Evidence Table
| Claim | Evidence | Source | Confidence | Weakness |
|---|---|---|---|---|

## 4. Portfolio Context
How this relates to concentration, correlation, event risk, or existing exposure.

## 5. Scenario Map
| Scenario | What happens | What confirms | What invalidates |
|---|---|---|---|

## 6. Risk Budget / Sizing Context
Only discuss if the user provided constraints. Do not invent account values.

## 7. Alternatives
Include “do nothing / wait” as one alternative.

## 8. Reassessment Triggers
What would require updating the memo?

## 9. Missing Data

## 10. Sources Used

## 11. Memo Quality Score
```

## Quality checks

- Do not convert a weak thesis into a confident conclusion.
- Make assumptions explicit.
- Always include alternatives and data gaps.
- Include the possibility that no manual action is the best process outcome.
