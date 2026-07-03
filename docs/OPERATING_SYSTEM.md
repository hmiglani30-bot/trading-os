# Operating System Definition

This repository is a versioned research workflow, not an execution system.

The OS has four parts:

1. **Source registry** — tells each workflow which public sources or user-provided files are relevant.
2. **Prompt modules** — reusable analysis contracts with required inputs and outputs.
3. **Workflows** — daily, weekly, and on-demand sequences that combine prompt modules.
4. **Runs** — dated output folders containing Markdown, HTML, and PDF reports.

## Core loop

```text
inputs -> source checklist -> prompt module -> workflow report -> saved run -> review log -> prompt update
```

## Report rule

Every completed run should produce:

```text
runs/YYYY/YYYY-MM-DD/<workflow>/report.md
runs/YYYY/YYYY-MM-DD/<workflow>/report.html
runs/YYYY/YYYY-MM-DD/<workflow>/report.pdf
```

The Markdown report is the editable source of truth. HTML and PDF are generated artifacts.

## Human-in-the-loop rule

The system can organize evidence and document reasoning. It should not execute orders, automate account actions, or present outputs as financial advice.
