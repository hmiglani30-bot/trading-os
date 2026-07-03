# P04 — Security Research Note

## Purpose

Create an on-demand company or ticker research note using primary sources first, then dashboards and commentary as supporting context.

## Required inputs

- Name or ticker.
- Research question.
- Time horizon.
- User-provided notes or files, if any.

## Source checklist

1. Company investor relations page.
2. Latest annual and quarterly filings.
3. Latest earnings release and transcript, if available.
4. Revenue, margin, cash flow, balance sheet, and guidance context.
5. Peer or sector context when useful.
6. News only for recent developments and narrative context.

## Output format

```markdown
# Security Research Note — <Name/Ticker>

## 1. Research Question

## 2. Business Snapshot

## 3. Key Drivers
| Driver | Evidence | What to monitor |
|---|---|---|

## 4. Financial Quality
- Revenue trend:
- Margin trend:
- Cash flow:
- Balance sheet:
- Guidance / outlook:

## 5. Valuation Context

## 6. Bull / Base / Bear Framing
| Case | What has to be true | Evidence | What would weaken it |
|---|---|---|---|

## 7. Recent Developments

## 8. Open Questions

## 9. Sources Used

## 10. Missing Data
```

## Quality checks

- Prefer filings and company materials for core facts.
- Do not use headlines as substitutes for filings.
- Clearly label assumptions and estimates.
