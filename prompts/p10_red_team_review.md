# P10 — Red-Team Review

## Purpose

Challenge a pre-action memo before any manual action is taken. The goal is to find weak evidence, hidden assumptions, missing data, and alternative interpretations.

## Required inputs

- Completed pre-action memo.
- Supporting notes or reports.
- User constraints and time horizon.

## Output format

```markdown
# Red-Team Review — <Name/Theme>

## 1. Strongest Objections
| Objection | Why it matters | Evidence needed |
|---|---|---|

## 2. Weakest Parts of the Memo

## 3. Missing Data That Could Change the View

## 4. Alternative Explanations

## 5. Process Risk
- Is the reasoning rushed?
- Is the idea driven by recent price movement or a headline?
- Are correlations or event timing being ignored?

## 6. Revised Confidence

## 7. Follow-up Checklist
```

## Quality checks

- Be adversarial but fair.
- Do not invent objections unsupported by facts.
- Focus on reasoning quality, not outcome prediction.
