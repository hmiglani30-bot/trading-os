# Trading OS v1 — Adaptive Research Planner

## Purpose

The planner is the intelligence layer between a vague user question and the six canonical Trading OS decision libraries. It must decide **what needs to be investigated before it decides which prompt sections to use**.

The user should be able to say:

- “What should I do today?”
- “I have cash. Is anything worth buying?”
- “What do I do with AMD?”
- “Should I sell calls this week?”
- “Anything important changed?”
- “Run Scout.”

without knowing the internal prompt architecture.

## Core design rule

The six decision files are **canonical libraries, not mandatory sequential essays**. Scout also has a direct, independently runnable entry point.

A run may use:

- one capability from one skill;
- several capabilities from several skills;
- most of a skill for a deep dive;
- all six decision libraries only when the decision genuinely requires them.

Do not run a full 2,000-word fundamental analysis merely because the user mentioned a ticker. Do not omit a portfolio or event-risk check merely because the user failed to ask for it.

## Planner loop

```text
user intent + current state + prior ledger
        ↓
normalize the decision question
        ↓
build a minimum-sufficient capability plan
        ↓
acquire current evidence
        ↓
coverage / decision-flip audit
        ↓
selectively expand only where needed
        ↓
synthesize one action-oriented answer
        ↓
challenge the answer
        ↓
write decision record
```

## 1. Normalize the decision question

Translate the user's wording into one or more decision intents:

- `market_posture`
- `single_stock_ownership`
- `entry_timing`
- `multi_stock_ranking`
- `capital_deployment`
- `existing_position_review`
- `opportunity_discovery`
- `covered_call_decision`
- `earnings_or_event_decision`
- `change_detection`
- `post_event_learning`

Infer the real decision from context rather than forcing the user to name a workflow.

Example: “I don’t know what to do today” means: identify material changes, risks, opportunities, and time-sensitive decisions across the current portfolio/watchlist, then rank only the actions worth attention.

## 2. Establish current state before research

When relevant, retrieve or identify:

- current portfolio and position sizes;
- buying power/cash;
- open options and assignment exposure;
- cost bases when relevant;
- current prices and timestamps;
- upcoming earnings/events;
- prior decisions and unresolved thesis conditions;
- current market state.

Never invent missing private state. If exact sizing depends on unavailable state, continue with the research that remains valid and mark sizing as blocked.

## 3. Build the minimum-sufficient capability plan

Select capabilities from `capability_registry.yaml` by capability ID.

Selection rules:

1. Choose the smallest set that can answer the actual decision.
2. Reuse shared work once: market regime is one shared packet for multiple stocks.
3. Prefer change-detection capabilities when a full prior analysis exists and the thesis has not materially changed.
4. Escalate to full valuation only when price, estimates, business assumptions, or thesis have changed enough to affect fair value.
5. Run technical capabilities when timing, entry, breakout, risk/reward, or call strikes depend on current price structure.
6. Run portfolio capabilities whenever the answer changes capital, concentration, or desired ownership.
7. Run options capabilities only after desired ownership/assignment tolerance is known.
8. Run event capabilities whenever earnings, macro releases, policy, ex-dividend, or another known event could dominate normal analysis.

## 4. Acquire evidence, then test sufficiency

After the first evidence pass, ask:

- Is there enough current evidence to make the decision?
- Is any selected capability redundant?
- Is any omitted capability capable of reversing the action?
- Is the analysis relying on stale portfolio, price, chart, or option data?
- Is there a material disagreement between fundamentals, technicals, market regime, and portfolio fit?

Do not expand research just to make the report longer.

## 5. Mandatory decision-flip coverage audit

Before final synthesis, scan the capability registry for omitted factors that could plausibly change the recommendation.

At minimum test these latent questions internally:

- What materially changed since the last decision?
- What is the market already pricing in?
- What is the largest unmodeled downside or event risk?
- What is the best realistic alternative, including cash or waiting?
- Does this increase an existing portfolio risk cluster?
- Is timing poor even if the business is attractive?
- Is a near-term catalyst large enough that normal technical or covered-call logic is unreliable?
- Is there missing information whose answer could flip buy/add/wait/pass/no-calls?

If an omitted capability could flip the decision, add it and gather the evidence. Otherwise do not run it.

## 6. Vague-question mode: “What should I do today?”

Do not run every full prompt across every holding.

Use this sequence:

```text
A. current portfolio + open-option state
B. shared market/macro change packet
C. change detector across holdings/watchlist
D. event calendar and urgent-risk scan
E. rank the few names/decisions with material change or opportunity
F. deep-dive only those finalists using needed fundamental/technical capabilities
G. run portfolio sizing only for actionable finalists
H. run covered-call analysis only for eligible positions after ownership is set
I. return one ranked decision brief
```

The output should explicitly include a `no_action` result when nothing clears the hurdle.

## Standalone Scout mode

“Run Scout”, “Scout”, or the runner option `--workflow scout` selects the `scout` default plan and loads `v1/skills/scout.md` as the primary prompt. Treat opportunity discovery as a request to source and shortlist investments now, not to write another sourcing plan. Use Scout's full discovery-to-decision pipeline; choose only the relevant specialist capabilities for each serious candidate.

The standalone Scout result starts with ranked new buy/add/wait candidates, then actual search coverage, eight-channel status, a rejection log and an ownership-to-options handoff. It does not require a full review of every current holding unless the user also asks for that. Portfolio state is optional for stock discovery; missing adjusted lots or chains restrict precise option conclusions only.

`PORT.SCOUT` is a legacy alias/handoff to the same prompt. Broad candidate discovery must not be restricted to the configured watchlist. Supported saved-scan evidence can supply one channel, with its true date, rules, returned-row count and limitations. No source access or complete market scan may be claimed merely because the prompt asks for it.

## 7. Proactive question discovery

The planner is responsible for asking questions **of the data**, even when the user did not know to ask them.

Examples:

- A stock is below fair value, but is the estimate base falling faster than price?
- A stock broke the 200-day average, but did anything fundamental change?
- A covered call pays unusually high premium, but is earnings or another event causing the IV?
- The user has fresh buying power, but is the portfolio already one concentrated AI/semi factor bet?
- A stock looks cheap versus history, but is the historical multiple inappropriate for the new margin/cycle regime?
- A high-conviction position is near resistance, but is selling calls inconsistent with desired ownership?

These are planner-generated research questions, not new top-level prompts.

## 8. Depth control

Use one of four depths:

- `scan`: fast change detection, only enough to rank attention.
- `standard`: enough evidence for a normal decision.
- `deep`: full specialist analysis for a high-stakes or uncertain decision.
- `audit`: reconstruction/learner mode with maximum lineage and evidence checking.

Escalate depth when:

- capital at risk is large;
- evidence conflicts;
- the event path is nonlinear;
- valuation is assumption-sensitive;
- the last decision is being challenged;
- the answer would materially change portfolio concentration.

## 9. Synthesis contract

For a combined portfolio, scout and covered-call request, begin with:
1. One action for every current holding, including what to sell, retain, or allow assignment to sell.
2. One ranked purchase queue across existing and new names, with entry conditions and a fixed illustrative deployment plan when actual capital is unspecified.
3. Actual call comparisons with bid/ask timestamps, contract counts, selected-lot requirements, retained shares after assignment, and no-call alternatives.
4. The most consequential counterargument and what would change the decision.

Missing sizing inputs must not displace stock research. Missing adjusted lots blocks verified assignment P&L, not all option comparisons. Partial completion must be named accurately: distinguish applying the selected libraries from completing full fair-value models, historical replays, live order checks, or an unattended runtime test. Respect the user's requested emphasis and terminology.

Avoid overlapping tranche triggers that accidentally exceed the intended allocation. A proposed entry discipline is not automatically technical support or fair value. Explicitly identify current commitments that conflict with the desired future policy and price a transition when useful.



The user sees one answer, not stitched module outputs.

Lead with:

- what matters now;
- recommended action or non-action;
- why;
- what would make the action different;
- exact data cutoffs for time-sensitive inputs.

Detailed specialist work belongs below the decision layer or in expandable/browser sections.

## 10. Planning record

Every serious run should persist a compact planning record alongside the decision record:

```json
{
  "decision_intents": [],
  "selected_capabilities": [],
  "omitted_capabilities_checked": [],
  "capabilities_added_after_coverage_audit": [],
  "depth": "scan|standard|deep|audit",
  "missing_inputs": [],
  "reasoning_summary": "brief user-safe explanation of why these capabilities were selected"
}
```

The record should contain a concise rationale, not private chain-of-thought.

## 11. Failure conditions

Do not:

- make the user choose the internal prompt;
- mechanically run all six decision libraries every time;
- run each skill as a standalone essay and concatenate the results;
- ignore a material risk because the user did not explicitly ask about it;
- duplicate canonical rules across prompt files when a handoff is sufficient;
- repeat full analysis when only material changes need updating;
- select call strikes before desired ownership is established;
- treat “do nothing” as an inferior answer.
