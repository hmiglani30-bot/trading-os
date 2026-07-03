# P01 — Daily Market and Portfolio Context Brief

## Purpose

Produce a short daily report that answers: what is scheduled, what changed, what market regime appears to be in place, and what should be watched in relation to the user's watchlist or portfolio context.

## Required inputs

- Date and timezone.
- Watchlist and/or holdings snapshot, if available.
- Open overlays or notable exposures, if available.
- Prior report, if available.
- User focus: risk review, opportunity scan, earnings, macro, options overlay, or general context.

## Source checklist

Check only sources needed for the report:

1. Official economic calendar for today and tomorrow.
2. Fed/FOMC calendar if relevant.
3. Broad index movement: SPY, QQQ, IWM or equivalents.
4. Rates: 2Y, 10Y, and curve direction if available.
5. Volatility: VIX and major volatility change.
6. Sector/industry heatmap or dashboard.
7. Market breadth if available.
8. Major news affecting user-provided names.
9. Earnings or event dates for user-provided names.

## Output format

```markdown
# Daily Market and Portfolio Context Brief — YYYY-MM-DD

## 1. Read First
- Regime: <risk-on / risk-off / mixed / event-risk / rates-driven / earnings-driven / unclear>
- Top scheduled event:
- Top market driver:
- Top watchlist/portfolio implication:
- Main uncertainty:
- Confidence:

## 2. Scheduled Events
| Time | Event | Official source? | Why it matters | Names/themes affected |
|---|---|---:|---|---|

## 3. Overnight / Prior-Session Change
Summarize index, sector, rates, volatility, and major news changes.

## 4. Market Internals
- Rates:
- Volatility:
- Breadth:
- Sector leadership:
- Risk appetite:
- Liquidity/credit notes if available:

## 5. Watchlist / Portfolio Relevance
| Name/theme | Relevant driver | Evidence | What to watch | Missing data |
|---|---|---|---|---|

## 6. Today's Research Guardrails
- Do not overinterpret:
- Requires confirmation:
- Good candidates for deeper research:
- Events to wait for:

## 7. Missing Data

## 8. Sources Used

## 9. Readiness Score
```

## Quality checks

- Keep the brief readable in under three minutes.
- Do not turn every headline into a conclusion.
- Connect market context to the user's supplied watchlist or portfolio context.
- Mark missing data clearly.
