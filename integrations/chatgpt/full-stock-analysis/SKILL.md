---
name: full-stock-analysis
description: Run the user's complete Trading OS stock analysis with market sentiment, fundamentals, technicals, and relevant portfolio or covered-call decisions. Use for full stock analysis, /full-stock-analysis, /full stock analysis, or a named ticker with this skill; accept optional instructions after the ticker.
---

# Full Stock Analysis

Use `hmiglani30-bot/trading-os` as the single methodological source. The user supplies a ticker or company and optional instructions; infer an unambiguous security from the current conversation if omitted. Do not require repository, branch, prompt paths, or a repeated long invocation.

1. Use the connected GitHub tools to read repository metadata and discover its default branch. Read `TRADING_OS_CURRENT.json` from that branch. Resolve its `active_ref` once to an immutable commit.
2. Read the manifest's full-stock-analysis workflow, entry point, planner, capability registry and required libraries at that commit. Follow the full workflow, including saved specialist findings, coverage audit and final critical review. Refresh this discovery each run; do not reuse an old commit as the latest source.
3. Preserve the user's optional instructions and established constraints. Research the three core disciplines fully. Add portfolio and covered-call analysis when relevant; add broad Scout only when requested. Use available connected brokerage tools for authorized read-only account research. Never claim unavailable lot data or current quotes.
4. Produce the decision and preserve detailed evidence privately. Loading prompts or producing a short summary does not establish complete execution. Report blocked requirements accurately. Source-resolution failures must be disclosed; do not silently substitute generic prompts.
5. When asked to repeat a prior run, distinguish a current update from an evaluation at the original information cutoff. Preserve the old output and compare material coverage and decision implications.

In ChatGPT, invoke by selecting `@full-stock-analysis`, then add `CBRS` and optional instructions. The text spellings `/full-stock-analysis CBRS` and `/full stock analysis CBRS` are conversational aliases this skill recognizes, not native slash-command registrations. In Codex, `$full-stock-analysis` invokes the same skill.

The workflow itself lives in GitHub; this installed skill is only the stable entry point. Research does not authorize submitting orders or changing the account.
