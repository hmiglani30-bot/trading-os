# P05 — Technical and Market Structure Review

## Purpose

Analyze chart context from a user-provided screenshot, OHLC data, or chart notes. The output should identify trend, levels, momentum, volume, relative strength, and setup quality without giving order instructions.

## Required inputs

- Ticker or instrument.
- Timeframe.
- Chart screenshot or price data.
- Relevant broad market context.
- User's time horizon.

## Output format

```markdown
# Technical and Market Structure Review — <Ticker>

## 1. Input Quality
State whether chart/data is sufficient.

## 2. Trend Regime
- Primary trend:
- Intermediate trend:
- Short-term trend:
- Relative strength:
- Volatility regime:

## 3. Key Levels
| Level | Type | Evidence | Strength | What would invalidate |
|---:|---|---|---|---|

## 4. Momentum and Volume
Discuss moving averages, volume, RSI/MACD, or other indicators only if visible or provided.

## 5. Setup Quality
Classify as: clean trend, extended, basing, breakdown, reversal attempt, chop/no edge, or insufficient data.

## 6. Scenario Map
| Scenario | Confirmation | Failure signal | Notes |
|---|---|---|---|

## 7. Relation to Fundamentals / Macro
Only connect if evidence exists.

## 8. Missing Data

## 9. Sources Used
```

## Quality checks

- Do not hallucinate indicators that are not visible or provided.
- State if the screenshot or data window is too limited.
- Separate observed chart facts from interpretation.
- Avoid generic support/resistance commentary without evidence.
