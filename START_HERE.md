# Trading OS — start here

This is the single source for the five core decision prompts. Use the existing branch `candidate/trading-os-v1-adaptive-planner`. Its `v1/skills/` files are canonical; the legacy P00–P12 files are historical comparison material.

| Core prompt | Canonical path |
|---|---|
| Fundamental analysis and fair value | [fundamental_fair_value.md](v1/skills/fundamental_fair_value.md) |
| Technical analysis and entry timing | [technical_entry_timing.md](v1/skills/technical_entry_timing.md) |
| Market, macro and sentiment | [market_regime.md](v1/skills/market_regime.md) |
| Portfolio allocation and Scout | [portfolio_capital_allocation.md](v1/skills/portfolio_capital_allocation.md) |
| Options and covered calls | [options_covered_calls.md](v1/skills/options_covered_calls.md) |

Scout belongs in portfolio allocation. Sentiment belongs in market analysis. The [adaptive planner](v1/runtime/adaptive_planner.md) routes the work; the [learner](v1/skills/learner.md) evaluates the process. Neither is a sixth core investment prompt.

## The result to deliver

Answer what to buy, what to do with each current holding, and which calls to sell, keep, close, or skip. Optimize prospective combined stock-and-option wealth over an explicit horizon, after known costs, with tax uncertainty stated. Do not replace decisions with another operating plan.

## Start a run

1. Read this entry point, the planner, the five canonical files required for the request, and the latest accessible private decision report. Record the actual Git commit and data cutoffs.
2. Retrieve the intended account's current holdings, existing calls, order/pending-event state, prices, corporate actions, and applicable lot policy. Do not reconstruct missing private facts from a generic example.
3. Research the shared market/events once. Compare current holdings with a liquid scout universe. Normalize earnings, calculate sufficiently supported technicals, and rank the next dollar.
4. Return one purchase queue, one decision per holding and a priced covered-call comparison. Reserve lots across existing and proposed calls; never substitute average basis when a selected-lot scenario is required.
5. Critique the decisions, record unresolved items, and save the dated private result. Update these original prompts only for demonstrated process defects; predictive changes need prospective evidence.

Missing adjusted lots blocks a verified assignment-profit claim. It does not block ownership analysis. A closed market permits a labeled last-session dry run; it does not provide executable orders.

## September 5 process revision

The five original files and planner now require action-first outputs, normalized earnings denominators, adequate genuine price history, event-aware timing, one ranked allocation queue, actual lot reservation, realistic bid/ask economics, and retained-share reconciliation.

These are candidate process improvements from a manual decision pass. They are not proof of superior returns or an unattended runner deployment. This branch remains under the existing [PR #2](https://github.com/hmiglani30-bot/trading-os/pull/2).

## Private records

This repository is public. Keep account identifiers, balances, quantities, private reports and raw broker records in an authorized private destination. A report saved separately is a run output, not a second prompt library. Reload it when available; label missing continuity rather than inventing it. Never move account data into this repository merely to simplify navigation.
