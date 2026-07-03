# P08 — Covered Call and Options Overlay Scenario Review

## Purpose

Analyze the tradeoffs of a covered call or other options overlay using user-provided position and option-chain data. This is scenario analysis and education, not an order instruction.

## Required inputs

- Underlying ticker.
- Share quantity.
- Cost basis.
- Current price.
- Expiration.
- Strike.
- Bid/ask or mid price.
- Volume/open interest.
- Implied volatility or delta if available.
- Earnings date.
- Ex-dividend date if relevant.
- User's assignment or exit tolerance.

## Source checklist

1. User broker snapshot for position facts.
2. Broker option chain for quote facts.
3. Company IR or earnings calendar for event dates.
4. OCC, FINRA, or broker education for mechanics and risk definitions.
5. Chart context if provided.

## Output format

```markdown
# Covered Call / Options Overlay Scenario Review — <Ticker>

## 1. Input Quality
| Data item | Present? | Notes | Confidence impact |
|---|---:|---|---|
| Share quantity | | | |
| Cost basis | | | |
| Current price | | | |
| Expiration | | | |
| Strike | | | |
| Bid/ask or mid | | | |
| Volume/open interest | | | |
| Implied volatility / delta | | | |
| Earnings date | | | |
| Ex-dividend date | | | |
| Assignment or exit tolerance | | | |

## 2. Strategy Fit
- Is the user willing to exit at the strike?
- Does expiration cross earnings?
- Does expiration cross ex-dividend date?
- Is liquidity acceptable?
- Is the bid/ask spread reasonable?

## 3. Return Mechanics
Calculate only from provided data.

- Premium:
- Premium as % of current price:
- Static return:
- If-called return:
- Upside capped:
- Breakeven approximation:
- Days to expiration:

## 4. Scenario Table
| Scenario | Price path | Outcome mechanics | Main risk |
|---|---|---|---|

## 5. Event and Assignment Risk
Discuss early assignment, earnings gap risk, ex-dividend risk, and liquidity risk if applicable.

## 6. Alternatives to Consider
Examples: no overlay, shorter duration, higher strike, wait until after event, reduce size, or research more.

## 7. Manual Decision Checklist
Questions the user must answer before acting.

## 8. Sources Used

## 9. Missing Data

## 10. Readiness Score
```

## Quality checks

- Do not provide order instructions.
- Make assignment or exit assumptions explicit.
- State event-date and liquidity gaps clearly.
- Do not treat premium as free return; identify upside cap and downside exposure.
