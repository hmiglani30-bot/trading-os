# Full Stock Analysis

## Invocation and scope

Run this workflow for `@full-stock-analysis <ticker> [optional instructions]`, `$full-stock-analysis`, the text aliases `/full-stock-analysis` or `/full stock analysis`, and an explicit request for full stock analysis. The slash spellings are natural-language aliases; they are not a claim of a registered ChatGPT slash command. Preserve everything after the invocation as the user's instructions.

The default is deep coverage of market/sentiment, fundamental/fair-value, and technical/entry-timing research for the named security. Include portfolio allocation when holdings, sizing or new capital are involved, and options when covered calls or existing options are involved. Include Scout only when discovery, a broad alternative search or a portfolio-wide run is requested. Shared market work runs once. A ticker-only invocation still researches the three core disciplines; missing brokerage access only limits private sizing and option feasibility.

Use the user's current and established constraints. Unless specified otherwise, disclose provisional horizons of 12–24 months for ownership and 4–12 weeks for tactical review; use actual dates for option scenarios. Optional instructions can change those horizons, scope, emphasis, formats and word budgets. They do not erase evidence limitations. Ask only when the ticker or another necessary choice remains ambiguous.

## Resolve the current source

1. Read repository metadata to identify its default branch.
2. Read `TRADING_OS_CURRENT.json` there. Follow its `active_ref`; do not select the newest-looking branch, a search snippet, an old chat's SHA or default-branch legacy prompts.
3. Resolve the active ref once to an immutable commit. Read this workflow, START_HERE, the planner, registry, the six library files and relevant schemas at that commit. Execute the applicable libraries; loading a file is not evidence of completing it.
4. Record the pointer-file SHA, resolved commit, file paths/hashes and actual evidence cutoffs. If resolution fails, disclose that current-version verification is blocked. Continue only with a clearly labeled last-verified version when useful; never call it latest.

## Execute and preserve the research

Explicit full mode selects every capability in the market, fundamental and technical groups. The planner may mark a conditional requirement unavailable or not applicable with reasons; it must not silently downgrade full mode to a selective update. Add portfolio and options capabilities according to the user's question. Preserve the plan before synthesis and record any later expansion.

Gather current account and market evidence through the connected read-only tools available in the host. The standalone API runner only has supplied private snapshots and its declared tools; it cannot inherit ChatGPT brokerage access. Separate current facts from historical snapshots and do not treat buying power as cash.

Complete a specialist stage for each selected library. Save its substantive findings and native machine-readable packet with source IDs, cutoff, horizon, assumptions, contrary evidence, missing inputs, confidence and reversal conditions. Use a `research_record.json` conforming to `v1/schemas/research_record.schema.json`. Human-readable appendices preserve calculations, assumptions and evidence behind conclusions; the structured record is not a substitute for analysis.

Specific completion checks:
- Market: distinguish observed price changes from causal claims; evaluate rates, credit, breadth, revisions and positioning where data exists; state competing explanations and an evidence-backed company transmission map; provide unweighted market scenarios and the events relevant to the horizon.
- Fundamentals: normalize financial definitions and distinguish reported, guided and estimated denominators. Assess competitive durability, management execution, concentration, capex and dilution. Show a supported valuation or reverse-valuation sensitivity that connects growth, margins, capital and share count to price. If inputs prevent a defensible value range, preserve explicit break-even assumptions and named blockages. A high revenue multiple alone does not establish overvaluation.
- Technicals: validate genuine history and timeframe. Show evidence for levels; pair each actionable scenario with an observation/entry zone, a defined confirmation interval, invalidation, first resistance or target and risk/reward where supportable. Address gaps and event risk; unavailable history must not produce invented indicators.
- Portfolio: compare the incremental decision with cash/waiting and a realistic existing alternative, preserving the user's requested scope. Reconcile current shares and obligations before proposing additions. Evaluate relevant shared exposures internally; respect the user's preference for actionable decisions instead of unsolicited leverage discussion.
- Options: establish desired ownership first. Preserve quoted bid/ask, timestamp, liquidity, contract counts and retained shares. Compare new purchases with no/partial/alternative calls; compare existing calls kept versus closed from the same current starting mark and terminal date. Keep historical premiums distinct from prospective returns. Apply the user's actual lot objective; unavailable adjusted lots keep assignment economics conditional with a timely contingency for existing obligations.

## Coverage and synthesis

For every selected capability, save a coverage row: capability ID, status (`covered`, `partial`, `blocked`, `not_applicable`), evidence/finding location, reason, decision impact and whether the gap could change the action. A covered row requires a source-backed finding. Blockages name the unavailable input; a not-applicable row explains scope. The full workflow cannot be labeled analytically complete while a material selected requirement remains partial or blocked. A provisional decision may still be useful.

Run the planner's omitted-capability audit before synthesis. Preserve the actual IDs checked and any capabilities added. Do not fabricate that record afterward as if it were contemporaneous.

Synthesize one decision brief, followed by the specialist appendices and coverage record. State the dominant reason, disagreement between disciplines, and the evidence needed to change the action. Keep ownership, timing and option horizons distinct. Do not average incompatible scores, count correlated technical signals as independent votes, or allow premium yield to override the ownership decision.

Separate how much is researched from how much is displayed. A concise brief may reference detailed appendices. Do not truncate or discard specialist findings to satisfy a report-wide word ceiling. Honor explicit user word limits and save supporting work separately if necessary. Record the actual word counts when a word limit was requested.

## Completion and review

Persist a source/run manifest, planning record, research record, decision record and dated report privately. Keep each stage's evidence and conclusions before composing the final recommendation; references may share one underlying source without copying it repeatedly.

Validate required fields and cross-references. Missing records or unresolved mandatory coverage must be labeled accurately, not upgraded to completion because the prose reads smoothly. Structural validation confirms inspectability, not investment accuracy or an edge.

For an improvement comparison, use the same original decision and information cutoff for a frozen replay. Separate newly researched facts, fresh market/account changes and method changes. Do not attribute a better result solely to prompts when inputs also changed. Preserve the original report; a new conclusion gets a new record.

Research authorization is not trade execution. Keep account identifiers, private holdings and raw broker data outside this public repository.

