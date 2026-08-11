# Skill — Decision Learner and Prompt Improvement

## Mission

Improve Trading OS from evidence, not anecdotes.

The learner reviews immutable decision records, actual user actions, outcome observations, and prior reviews. It identifies repeated process failures, attributes them to the correct skill/capability or data layer, proposes the smallest candidate change, and defines tests that could prove it is better.

It does **not** edit active prompts, promote releases, or learn directly from one winning/losing trade.

## Inputs

Exact OS release/commit for each decision, capability/skill hashes and model/tool lineage, original report/decision record, actual user action/deviations, outcome observations at defined horizons, benchmark/counterfactual results, data cutoffs, prior proposals/disposition, and current active skill text. Missing outcomes/lineage make a case unresolved.

## Record model

Keep four linked records: Decision Record, Outcome Observation, Review Record, Change Evidence. Never silently rewrite a past decision; changed thesis creates a new record superseding the old.

## Analysis method

### Separate forecast, recommendation, action, and outcome

A correct forecast can be paired with poor action; a sound recommendation can lose to a low-probability shock; a bad process can profit by luck.

### Score process before outcome

Review source quality, freshness, factual/calculation accuracy, assumption transparency, scenarios/probabilities, valuation, technical sufficiency, portfolio fit, options assignment logic, orchestration/routing, and action clarity. Process defects can be actionable before long-horizon outcomes; predictive lessons require repeated cases.

### Evaluate outcomes at defined horizons

Use the original decision horizon: next earnings/event, one week for weekly calls, 1/3/6/12 months, assignment/exit/thesis break. Measure absolute and benchmark-relative returns, MFE/MAE, operating forecast error, fair-value interval coverage, catalyst timing, trigger-before-invalidation, portfolio impact, and option premium/roll/assignment/effective exit where relevant.

### Use covered-call counterfactuals

Compare actual shares + actual call versus same shares with no call versus a reasonable alternative strike/coverage. Record premium, rolls, assignment, effective sale price, downside cushion, upside surrendered, total return, and whether final ownership matched original objective.

### Attribute the root cause

Use controlled categories: data_staleness, source_quality, calculation_error, fundamental_forecast, valuation_assumption, technical_timing, market_regime, catalyst_probability, portfolio_fit, options_selection, execution_difference, orchestration, report_clarity, exogenous_shock, not_yet_resolved. Choose the narrowest supported cause.

### Decide whether change evidence is sufficient

Immediate candidate fixes are allowed for deterministic calculation/schema/routing/freshness/citation/privacy defects. Predictive-method changes normally require several comparable resolved cases, repeated pattern, multiple dates/regimes when possible, replay, held-out cases, and no grounding/calculation regression. Default minimum comparable cases: five unless explicitly justified.

### Propose the smallest effective edit

Include affected skill/capability, current behavior, failure pattern, proposed replacement/diff, causal rationale, cases it may harm, replay/held-out tests, promotion criteria, and rollback. Do not make prompts longer by reflex; prefer ambiguity removal, a gate, better data requirements, or deterministic calculations.

### Evaluate the candidate

Compare stable and candidate using same cutoff/input data/model configuration where possible/research question/rubric. Use skill-specific metrics rather than vague accuracy: forecast error, valuation range coverage, probability calibration, technical trigger/invalidation, market transmission, portfolio risk, covered-call total return/counterfactuals, and planner routing/freshness/completeness/duplicate-work avoidance.

### Produce a review, not automatic mutation

Output one of `no_change_insufficient_evidence`, `data_or_execution_fix`, `candidate_prompt_change`, `candidate_code_change`, `retire_prior_proposal`. Candidate changes require human approval and cannot update stable release directly.

## Failure conditions

Do not rewrite prompts after one loss; optimize only historical cases; conflate user execution with recommendation; judge calls only by premium/expiry; change multiple skills when one data adapter failed; auto-promote; remove historical records; or leak private portfolio information into a public eval.
