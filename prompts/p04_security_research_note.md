# P04 — Security Fundamental Research Note

## Purpose

Create an equity research note for a company or ticker using filings and company materials first. The goal is to understand business quality, drivers, valuation context, risks, and variant perception.

## Required inputs

- Ticker/company.
- Research question.
- Time horizon.
- Current position/watchlist status if provided.
- User notes/files if available.

## Source checklist

1. Company investor relations.
2. Latest annual and quarterly filings or equivalent disclosures.
3. Latest earnings release and transcript.
4. Segment data, revenue drivers, margins, cash flow, balance sheet.
5. Guidance and management commentary.
6. Peer or sector context.
7. Recent news only after primary facts are established.

## Output format

```markdown
# Security Fundamental Research Note — <Ticker>

## 1. Research Question

## 2. Business Model
How the company makes money, key segments, customer base, and unit economics if available.

## 3. Key Drivers
| Driver | Evidence | Direction | What to monitor |
|---|---|---|---|

## 4. Financial Quality
- Revenue growth:
- Gross/operating margin:
- Free cash flow:
- Balance sheet:
- Dilution/buybacks:
- Capital intensity:
- Debt/credit considerations:

## 5. Management and Guidance
Summarize guidance, tone, execution record, and credibility.

## 6. Competitive Position
Moat, competitive threats, pricing power, switching costs, regulation, and cyclicality.

## 7. Valuation Context
Multiples, growth-adjusted context, peer comparison, historical context if available. State limitations.

## 8. Variant Perception
What would the market need to be wrong about for this to be interesting?

## 9. Bull / Base / Bear Case
| Case | What must be true | Evidence | What breaks it |
|---|---|---|---|

## 10. Key Risks

## 11. Open Questions

## 12. Sources Used

## 13. Missing Data

## 14. Readiness Score
```

## Quality checks

- Prefer filings and company materials for core facts.
- Do not use headlines as substitutes for filings.
- Clearly label assumptions and estimates.
- Include balance sheet and capital structure, not just growth narrative.
