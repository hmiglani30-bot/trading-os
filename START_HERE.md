# Trading OS — start here

This is the single source for the six core decision prompts. Discover the current source through `TRADING_OS_CURRENT.json` on this repository's default branch. Resolve its active ref once to a commit and read the canonical files at that commit; the user never needs to supply a branch. Legacy P00–P12 files are historical comparison material.

| Core prompt | Canonical path |
|---|---|
| Fundamental analysis and fair value | [fundamental_fair_value.md](v1/skills/fundamental_fair_value.md) |
| Technical analysis and entry timing | [technical_entry_timing.md](v1/skills/technical_entry_timing.md) |
| Market, macro and sentiment | [market_regime.md](v1/skills/market_regime.md) |
| Portfolio allocation | [portfolio_capital_allocation.md](v1/skills/portfolio_capital_allocation.md) |
| Options and covered calls | [options_covered_calls.md](v1/skills/options_covered_calls.md) |
| **Scout: stock discovery and shortlisting** | **[scout.md](v1/skills/scout.md)** |

Scout is independently runnable and owns its discovery rules. Portfolio allocation consumes its findings; legacy `PORT.SCOUT` requests hand off to the same Scout file. Sentiment belongs in market analysis. The [adaptive planner](v1/runtime/adaptive_planner.md) routes the work; the [learner](v1/skills/learner.md) evaluates the process.

## One command

Use **@full-stock-analysis CBRS**, followed by any optional instructions. The installed ChatGPT skill resolves the current GitHub source on every run and executes [Full Stock Analysis](v1/workflows/full_stock_analysis.md). Text aliases /full-stock-analysis and /full stock analysis are also understood; they are not platform slash-command registrations.

This selects deep market/sentiment, fundamental and technical work with preserved specialist packets, then adds portfolio and options work when relevant. Ordinary adaptive requests remain selective. See the workflow for source resolution, horizons, coverage, output records and frozen replay rules.

## The result to deliver

Answer what to buy, what to do with each current holding, and which calls to sell, keep, close, or skip. Optimize prospective combined stock-and-option wealth over an explicit horizon, after known costs, with tax uncertainty stated. Do not replace decisions with another operating plan.

## Run Scout directly

Say **“Run Scout”** and load [scout.md](v1/skills/scout.md). You do not need to invoke Portfolio Allocation first. The default is a broad U.S.-listed stock search with a 12–24-month ownership horizon and a 4–12-week tactical review window. Return ranked findings, the actual search scope, all eight source-channel statuses and a rejection log.

The API runner supports the same entry point:

```bash
python v1/runtime/run_adaptive.py --workflow scout --request "Run Scout" --output-root /path/to/private-runs
```

Optional `--scout-evidence-file /path/to/dated-scan.json` supplies exported source records or broker scan rows. Optional portfolio, chain and previous-report files preserve context. No account snapshot is required to source stocks. The runner's live mode requires its documented dependencies and an authorized API key; it has web search and supplied files, not automatic access to connected brokerage tools. `--demo` verifies routing/artifacts only and does not research stocks.

## Start a combined portfolio run

1. Read this entry point, the planner, the canonical files required for the request, and the latest accessible private decision report. Record the actual Git commit and data cutoffs.
2. Retrieve the intended account's current holdings, existing calls, order/pending-event state, prices, corporate actions, and applicable lot policy. Do not reconstruct missing private facts from a generic example.
3. Research the shared market/events once. Compare current holdings with a liquid scout universe. Normalize earnings, calculate sufficiently supported technicals, and rank the next dollar.
4. Return one purchase queue, one decision per holding and a priced covered-call comparison. Reserve lots across existing and proposed calls; never substitute average basis when a selected-lot scenario is required.
5. Critique the decisions, record unresolved items, and save the dated private result. Update these original prompts only for demonstrated process defects; predictive changes need prospective evidence.

Missing adjusted lots blocks a verified assignment-profit claim. It does not block ownership analysis. A closed market permits a labeled last-session dry run; it does not provide executable orders.

## September 5 process revision

The five original files and planner now require action-first outputs, normalized earnings denominators, adequate genuine price history, event-aware timing, one ranked allocation queue, actual lot reservation, realistic bid/ask economics, and retained-share reconciliation.

These are candidate process improvements from a manual decision pass. They are not proof of superior returns or an unattended runner deployment. This branch remains under the existing [PR #2](https://github.com/hmiglani30-bot/trading-os/pull/2).

## September 6 Scout revision

Scout is now the sixth top-level decision prompt. It applies eight discovery channels, an explicit universe, source and count reconciliation, research breadth targets, common ownership diligence and a separate options handoff. Proposed screening thresholds and research quotas require prospective evaluation; they are not proof of an investment advantage. Read-only saved scans can contribute evidence without becoming the complete universe by assertion.

## Private records

This repository is public. Keep account identifiers, balances, quantities, private reports and raw broker records in an authorized private destination. A report saved separately is a run output, not a second prompt library. Reload it when available; label missing continuity rather than inventing it. Never move account data into this repository merely to simplify navigation.
