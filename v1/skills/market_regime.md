# Skill — Market, Macro, and Sentiment Regime

## Mission

Determine the current market regime, identify what changed since the previous run, and translate those changes into decision-relevant implications for the user's portfolio and watchlist.

This skill is the shared umbrella for macroeconomics, rates and liquidity, cross-asset signals, market breadth and volatility, sector rotation, news, positioning and narrative, and event-calendar risk.

For a multi-stock request, run shared market work once. Every company receives the same dated market packet, followed by company-specific transmission analysis.

## Modes

- `morning`: premarket or start-of-day decision brief.
- `intraday`: material change since the most recent report.
- `weekly`: regime review and next-week setup.
- `event`: CPI, jobs, central-bank decision, major geopolitical event, sector shock, or another defined catalyst.
- `deep`: full market and sentiment report when explicitly requested.

## Inputs

Required: current date/time/timezone, analysis cutoff, user objective/horizon, portfolio/watchlist when relevant, and prior regime packet when available.

Useful: equity indices/futures, Treasury curve and real yields, credit spreads, dollar/oil/gold, volatility and options positioning, breadth, sector leadership, official economic releases, central-bank communications, major earnings/events, and high-quality news/company disclosures.

If sufficiently current data is unavailable, say so. Do not use stale market numbers while writing as if the market is live.

## Source discipline

Use primary/official sources first, then current market-data tools, then high-quality financial news for context, analyst commentary for interpretation, and social/retail narrative only as sentiment evidence. Separate observed fact, reported claim, inference, and judgment. Do not infer causality merely because assets moved together.

## Analysis method

### Establish the regime

Classify growth, inflation, policy, liquidity, rates, credit, equity tape, volatility, breadth, and actual sector/style leadership using evidence rather than slogans.

### Identify what changed

For each meaningful change state the new information, prior expectation, why the delta matters, whether it is durable/event-specific/noise, and which portfolio names are exposed. Prioritize changes to cash flows, discount rates, risk premia, capital availability, or positioning.

### Build the transmission map

Translate developments into company-level effects through discount rates/duration, capital spending, AI/data-center demand, semiconductor cycle, software budgets, consumer demand, FX, input costs, regulation/trade, credit availability, multiple compression/expansion, and crowded positioning. Distinguish direct fundamental exposure, indirect valuation exposure, short-term trading exposure, and narrative-only exposure.

### Evaluate sentiment and positioning

Assess price response to good/bad news, analyst revisions, earnings-reaction asymmetry, options-implied event pricing, volatility term structure, breadth/concentration, crowding, and narrative intensity when data exists. State what is priced in and what evidence would disprove the dominant narrative.

### Construct scenarios

Create bear/base/bull market scenarios with probabilities summing to 100%, observable conditions, confirming indicators, invalidating indicators, and watchlist transmission.

### Build the event calendar

Include only decision-relevant economic releases, central-bank events, relevant earnings, regulatory/policy events, industry/product events, and positioning events. Use exact dates/timezones and mark uncertainty.

### Produce a decision implication

Translate the regime into deployment posture, factor preferences, entry style, covered-call aggressiveness, and cash reserve logic. Do not recommend deployment merely because cash exists.

## Machine-readable packet

Return fields for as_of, cutoff, mode, regime_label, confidence, growth, inflation, policy_liquidity, rates_credit, equity_tape, leadership, what_changed, scenario_probabilities, watchlist_transmission, event_calendar, decision_posture, risk_flags, missing_data, and source_notes.

## Failure conditions

Do not repeat macro analysis for every ticker; treat price movement as proof of cause; report old data as current; convert social sentiment into fundamental evidence; bury the decision implication; assign unsupported precise probabilities; or claim certainty around geopolitical/policy outcomes.
