# Skill — Technical Analysis and Entry Timing

## Mission

Determine whether the current price structure offers a favorable timing window for the stated horizon. Identify trend, levels, volatility, confirmation, invalidation, and risk/reward without inventing indicators or pretending a static chart is live.

Technical analysis answers **when and at what conditions**, not whether the business is fundamentally worth owning.

## Modes

`morning`, `single_stock_deep_dive`, `multi_stock_comparison`, `earnings_event`, `covered_call`, `intraday` when sufficiently current data exists.

## Required inputs

Ticker, price/timestamp, horizon, chart or OHLCV data/timeframe, market-regime packet, event dates, prior technical plan when available. Useful indicators include moving averages, RSI, MACD, ATR, VWAP, Bollinger Bands, relative strength, volume profile, option-implied move, and sector/benchmark comparison only when actually computed or supplied.

State the data window and last bar. If an indicator/timeframe is absent, mark it unavailable rather than approximating from memory.

## Analysis method

### Validate the input

State source/timestamp, bar interval, adjusted/unadjusted data, volume availability, session state, missing indicators/timeframes, and whether the data is sufficient for the horizon. An old screenshot cannot support a live strike or entry decision. Verify the actual date of a provider's official-close field; it may lag the latest timestamped regular-session trade. Keep regular-session and extended-hours references distinct. Remove interpolated pre-listing bars and require at least N genuine observations before calculating an N-period indicator. Handle splits and ADR units before comparing price levels.

### Classify the multi-timeframe trend

Assess weekly, daily, intraday when available, relative strength, and volatility. Classify as clean trend, orderly pullback, breakout attempt, extended momentum, base/range, failed breakout, breakdown, reversal attempt, high-volatility event setup, chop/no edge, or insufficient data, with evidence.

### Map important levels

Identify evidence-backed swing highs/lows, breakout/breakdown levels, gaps, high-volume areas, moving-average clusters, VWAP/anchored VWAP when supplied, support/resistance zones, event-day references, and invalidation. Use zones rather than false exactness and rank level strength.

### Evaluate momentum and participation

When data exists, examine price versus 20/50/100/200-day averages, slope/alignment, RSI and divergence, MACD, ATR/realized volatility, Bollinger structure, advance/decline volume, accumulation/distribution clues, gaps/follow-through, breadth and sector confirmation. Indicators are evidence, not automatic signals.

### Diagnose extension and asymmetry

Ask how far price is from key averages/breakout levels; reward versus downside to invalidation; whether pullback/breakout/consolidation is needed; mean-reversion risk; and whether event risk overwhelms chart levels. Quantify when inputs allow.

### Create executable conditions

For each scenario provide entry/observation zone, confirmation trigger, invalidation, first resistance/target zone, expected path, and conditions where waiting is superior.

### Integrate fundamentals and market regime

Use market/fundamental packets to interpret rather than overwrite the chart. Distinguish a fundamentally attractive but technically weak setup from a technically strong but fundamentally overvalued momentum trade.

### Make the timing decision explicit

Return a usable purchase/observation range, confirmation trigger, invalidation, and the next action if price gaps past the range. Separate valuation entry disciplines from chart support. Identify a preferred staged entry and a no-purchase condition; do not require every candidate to wait indefinitely for an ideal pullback. Indicators derived from the same price series are not independent confirmations.

### Hand off to portfolio and options

Provide setup quality, entry suitability, event risk, assignment-relevant resistance zones, breakout risk from selling calls, and whether waiting for event resolution improves the decision. Do not select the final call strike here.

## Machine-readable packet

Return ticker/as_of/data_cutoff/timeframes/input_quality, multi-timeframe trend, setup_class, volatility_regime, levels, entry_plan, covered_call_context, setup_score, entry_suitability, missing_data, and source_notes.

## Failure conditions

Do not hallucinate chart values/indicators; call a level precise from weak evidence; use technical strength as proof of fair value; ignore earnings/event gaps; recommend chasing solely on momentum; claim an intraday view from EOD data; or bury `no edge` when that is the honest conclusion.

## Preservation in a full run

In full stock analysis, define the bar interval and observable confirmation behind terms such as held or sustained. Pair each actionable scenario with entry/observation, invalidation, first resistance/target and supported asymmetry; preserve these fields through synthesis. Follow [Full Stock Analysis](../workflows/full_stock_analysis.md) for the shared coverage and saved-record contract.
