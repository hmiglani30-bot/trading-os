# P05 — Chart Context Review

## Purpose

Summarize chart context from a user-provided chart screenshot, OHLC data, or dashboard notes. This prompt documents trend, levels, momentum, and uncertainty; it does not provide order instructions.

## Required inputs

- Ticker or instrument name.
- Chart timeframe.
- Screenshot, price data, or user-provided chart notes.
- Current broad market context, if available.

## Output format

```markdown
# Chart Context Review — <Name/Ticker>

## 1. Input Summary

## 2. Trend Context
- Primary trend:
- Secondary trend:
- Relative strength if available:

## 3. Key Levels
| Level | Type | Evidence | Confidence |
|---:|---|---|---|

## 4. Momentum and Volume

## 5. Scenario Map
| Scenario | What would confirm it | What would weaken it |
|---|---|---|

## 6. Data Quality Limits

## 7. Sources Used

## 8. Missing Data
```

## Quality checks

- Do not hallucinate indicators not visible or provided.
- State if the screenshot is too limited.
- Separate observed chart facts from interpretation.
