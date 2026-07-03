# P08 — Options Overlay Scenario Review

## Purpose

Document the tradeoffs of an options overlay using user-provided position data and option-chain snapshots. This is an educational scenario review, not an order instruction.

## Required inputs

- Underlying name or ticker.
- Share quantity and cost basis, if relevant.
- Current price snapshot.
- Option-chain snapshot with bid/ask, expiration, strike, and volume/open interest if available.
- Relevant event dates.
- User's stated assignment or exit tolerance.

## Source checklist

1. User-provided broker snapshot for position-specific facts.
2. Broker option-chain snapshot for quote-specific facts.
3. Company event calendar or investor relations for date-specific risk.
4. OCC/FINRA/broker education pages for mechanics and risk definitions.

## Output format

```markdown
# Options Overlay Scenario Review — <Name/Ticker>

## 1. Input Summary

## 2. Data Quality
| Data item | Present? | Notes |
|---|---:|---|
| Share quantity | | |
| Cost basis | | |
| Current price | | |
| Expiration | | |
| Strike | | |
| Bid/ask | | |
| Events before expiration | | |

## 3. Scenario Table
| Scenario | Price path | Outcome mechanics | Key risk | Missing data |
|---|---|---|---|---|

## 4. Premium vs Upside Cap Review

## 5. Event and Liquidity Review

## 6. Questions Before Any Manual Action

## 7. Sources Used

## 8. Missing Data
```

## Quality checks

- Do not provide order instructions.
- Make assignment or exit assumptions explicit.
- State event-date and liquidity gaps clearly.
