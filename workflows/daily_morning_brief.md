# Workflow — Daily Morning Brief

## Goal

Create one short daily report that can be read quickly in a browser.

## Modules used

- `prompts/p00_master_report_contract.md`
- `prompts/p01_daily_context_brief.md`
- `source_registry/source_matrix.md`

## Inputs to provide

- Date and timezone.
- Watchlist or themes.
- Any relevant user notes or snapshots.
- Optional: prior day's report.

## Source plan

1. Check scheduled public events for today and tomorrow.
2. Check broad index, sector, rates, and volatility context.
3. Check major news only for user-provided names or themes.
4. Mark any source gaps.

## Output location

Save as:

```text
runs/YYYY/YYYY-MM-DD/daily-morning-brief/report.md
```

Then run the renderer to generate:

```text
runs/YYYY/YYYY-MM-DD/daily-morning-brief/report.html
runs/YYYY/YYYY-MM-DD/daily-morning-brief/report.pdf
```

## Report length

Target: 1-2 pages.

## Required final sections

- Read First
- Scheduled Events
- Broad Context
- Watchlist Relevance
- Follow-up Checklist
- Sources Used
- Missing Data
