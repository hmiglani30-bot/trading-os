# P03 — Portfolio Snapshot and Exposure Review

## Purpose

Analyze a user-provided portfolio or watchlist snapshot for concentration, factor exposure, event clustering, and options-overlay risk. Do not infer account values that are not provided.

## Required inputs

- Holdings list with ticker/name and approximate value or weight.
- Cost basis if available.
- Open overlays if available.
- Watchlist.
- Time horizon.
- User constraints.

## Source checklist

1. User-provided snapshot is primary for account-specific facts.
2. Company event dates for provided names.
3. Sector/factor classification.
4. Market regime context from P01 or P02.
5. Expiry and event dates for any overlays if provided.

## Output format

```markdown
# Portfolio Snapshot and Exposure Review — YYYY-MM-DD

## 1. Executive Summary
Include the biggest concentration, biggest event risk, and biggest missing data issue.

## 2. Input Quality
| Input | Present? | Quality | Impact if missing |
|---|---:|---|---|
| Tickers/names | | | |
| Position size/weight | | | |
| Cost basis | | | |
| Open overlays | | | |
| Expiry dates | | | |
| Earnings dates | | | |

## 3. Concentration Review
| Name/theme | Approx exposure | Type of risk | Why it matters | Missing data |
|---|---:|---|---|---|

## 4. Factor and Correlation Review
Identify repeated exposure such as mega-cap tech, semiconductors, AI, high beta, rates-sensitive growth, cyclicals, small caps, energy, financials, or other clusters.

## 5. Event Cluster Review
| Date | Event | Affected names | Risk type | Source |
|---|---|---|---|---|

## 6. Overlay Review
Summarize open overlays if provided: expiry, strike, event overlap, liquidity concerns, and scenario implications.

## 7. Scenario Map
| Scenario | Portfolio path | Main drivers | What to monitor |
|---|---|---|---|

## 8. Missing Data

## 9. Sources Used

## 10. Readiness Score
```

## Quality checks

- Never infer account values not provided.
- State whether snapshots are stale or incomplete.
- Keep user-provided account facts separate from public-market context.
- Flag concentration and event clustering even when the user did not ask directly.
