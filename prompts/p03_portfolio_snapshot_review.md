# P03 — Portfolio Snapshot Review

## Purpose

Review a user-provided holdings or account snapshot for concentration, event exposure, missing information, and reporting quality. This prompt documents research context only; it does not provide account actions.

## Required inputs

- Holdings snapshot or manual position list.
- Open derivatives or overlay positions, if relevant.
- Watchlist, if provided.
- User time horizon and constraints.

## Source checklist

1. User-provided snapshot is primary for account-specific facts.
2. Public company-event calendars for user-provided names.
3. Broad sector and factor context.
4. Volatility and rates context if relevant.

## Output format

```markdown
# Portfolio Snapshot Review — YYYY-MM-DD

## 1. Executive Summary

## 2. Input Quality
| Input | Present? | Notes |
|---|---:|---|
| Holdings | | |
| Cost basis | | |
| Current value | | |
| Open overlays | | |
| Event dates | | |

## 3. Concentration Map
| Name/theme | Approx exposure | Why it matters | Missing data |
|---|---:|---|---|

## 4. Event Exposure
| Name/theme | Event | Date | Source | Relevance |
|---|---|---|---|---|

## 5. Scenario Review
| Scenario | Possible impact path | Evidence | Data needed |
|---|---|---|---|

## 6. Follow-up Checklist

## 7. Sources Used

## 8. Missing Data
```

## Quality checks

- Never infer account values that are not provided.
- State whether snapshots are stale or incomplete.
- Keep user-provided data separate from web-sourced context.
