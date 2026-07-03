# Source Matrix

This file maps each report workflow to the sources it should check. The goal is to make reports source-aware instead of relying on ad hoc browsing.

## Source hierarchy

### Tier 1 — official or primary

Use these when precision matters.

- Company investor relations pages and SEC filings for company facts.
- BLS, BEA, Census, Treasury, Federal Reserve, and FRED for macro releases and time-series data.
- Exchange, regulator, and broker education pages for definitions, mechanics, and risk language.

### Tier 2 — dashboards

Use these for fast scanning, then verify important claims against Tier 1 sources.

- TradingView, Finviz, Yahoo Finance, Nasdaq, Koyfin, broker charts, and similar tools.

### Tier 3 — news and commentary

Use these to understand narratives and recent developments. Commentary is not source-of-truth data.

- Reuters, AP, WSJ, Bloomberg, CNBC, MarketWatch, Yahoo Finance, company press releases, analyst commentary, newsletters, blogs, Reddit, and social posts.

## Workflow-to-source map

| Workflow | Required inputs | Optional inputs | Output focus |
|---|---|---|---|
| Daily morning brief | economic calendar, index movement, volatility, rates, watchlist | major news, account snapshot | regime, events, watch items |
| Monday weekly review | holdings snapshot, open positions snapshot, macro calendar, recent activity, upcoming events | breadth, sentiment, sector dashboards | exposure, risk clusters, weekly priorities |
| Security research note | filings, earnings releases, transcripts, investor relations pages | peers, commentary, chart context | business, drivers, risks, open questions |
| Scenario review | position details, current market data snapshot, relevant dates, liquidity notes | volatility context, chart levels | scenario table and tradeoffs |
| Pre-action memo | thesis notes, evidence, context, assumptions | chart context, news, macro backdrop | documented reasoning and objections |
| Post-action review | original memo, outcome, price path, news after action | failure log | learning and process updates |

## Source discipline rules

1. Separate facts, assumptions, and judgments.
2. State when data is missing.
3. Use official sources for dates, filings, and macro releases whenever possible.
4. Use dashboards for speed, not as final authority.
5. Never let a single article or social post drive a report conclusion.
6. Every report must include `Sources used` and `Missing data` sections.
