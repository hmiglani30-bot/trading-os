# Skill — Portfolio Risk, Capital Allocation, and Scout

## Mission

Convert stock-level research into a portfolio decision: whether to deploy, which names deserve capital, how much, sequencing/tranches, what remains in cash, and what existing risk the decision adds or reduces.

This skill is also the home of **Scout**, the discovery and ranking mode. Scout is a funnel using the same market, fundamental, technical, portfolio, and options standards—not another mega-prompt.

## Modes

`portfolio_review`, `capital_deployment`, `multi_stock_ranking`, `existing_position_review`, `scout`, `morning`, `event_rebalance`.

## Inputs

For personalized allocation: timestamped portfolio snapshot, quantities/weights, prices/market values, buying power/cash, cost-basis lots when relevant, open options/expiries, horizon/liquidity/constraints, and market/fundamental/technical packets. Useful: margin/maintenance, gains, supplied tax constraints, near-term obligations, sector/factor classifications, events, correlations/shared risk drivers.

Never infer account balances, sizes, taxes, or constraints. If state is stale, separate what remains valid from what is blocked.

## Required decision output

For a portfolio-and-scout request, the first output must contain: (1) one action for every current holding, (2) a ranked shortlist of new ownership candidates with entry conditions, (3) explicit wait/pass candidates, and (4) an options handoff for eligible shares. State the objective as expected combined stock-and-option wealth over a named horizon, after known costs and with tax uncertainty labeled. Gross premium receipts are not the objective.

Missing exact investable capital blocks exact deployment size, not stock ranking or ownership research. Offer a clearly illustrative per-dollar allocation or staged plan when useful; never invent an approved budget. Run constraints only to determine which proposed action is feasible; do not replace the requested decisions with a generic diagnostic report.

## Core principles

Capital need not be fully invested. Evaluate the next dollar incrementally. Measure concentration by shared economic drivers, not ticker count. High conviction does not eliminate sizing risk. Ownership quality and covered-call suitability are separate. Low confidence should mean smaller size, tranches, or waiting. Final recommendations must be feasible under real liquidity constraints.

## Analysis method

### Validate portfolio state

Report snapshot timestamp, supplied investable capital, holdings/concentration, missing cost bases/options, stale prices, margin/liquidity availability, and supplied cash needs. Block exact dollar sizing when capital input is absent/unreliable.

### Identify existing risk clusters

Assess single-name, sector/industry, AI/data-center/semi, mega-cap duration, rates, cyclicality, customer/supplier overlap, geography/regulation, event clustering, volatility/gap, and margin/liquidity risk. Many semi tickers can still be one concentrated trade.

### Establish a cash and risk posture

Choose deploy, selectively deploy, tranches, reserve cash for catalysts, or wait, based on regime and constraints. Do not use a generic fixed cash percentage.

### Evaluate each candidate independently

Use separate dimensions: business/financial quality, valuation/expectations gap, technical timing, catalyst asymmetry, portfolio fit, liquidity, and confidence. If a score is used, it cannot replace reasoning.

### Rank incremental opportunities

For each candidate state action (buy/add/hold/wait/pass/reduce), role, attractive entry condition, initial/max exposure ranges, tranche plan, funding/cash impact, principal risk, and invalidation. Explain why A is better than B at current prices.

### Resolve the replacement decision

For each new finalist, name the existing holding it beats for incremental capital and explain why at the observed prices. Distinguish new purchases from core holdings that remain worth retaining. A reduction recommendation must state whether it means an immediate sale, a price-triggered sale, or willingness to accept an existing call assignment. Historical cost does not establish forward investment value, but selected-lot instructions govern any assignment-profit claim.

### Size under uncertainty

Consider downside scenario, volatility/gap, confidence, liquidity, event proximity, correlated exposure, drawdown tolerance, and buying-power reserve. Prefer ranges/tranches over false precision.

### Make the no-action comparison

Compare deployment with holding cash, adding to an existing highest-conviction position, waiting for a catalyst/technical confirmation, or reducing correlated exposure first. The hurdle is better than realistic alternatives after portfolio risk.

## Scout mode

Use a liquid/researchable core universe plus a smaller discovery lane with explicit inclusion/exclusion/data-quality rules. Hard-filter for liquidity, current disclosures, listing suitability, option liquidity when calls matter, event/delisting risk, accounting/governance red flags, portfolio duplication, and user exclusions.

Scout returns two distinct outputs: ownership candidates and covered-call candidates. Funnel: universe → hard filters → market-regime fit → fundamental/valuation shortlist → technical timing → portfolio-risk gate → final ranked candidates → optional options handoff. If nothing clears the hurdle, return cash/watchlist.

## Machine-readable packet

Return as_of/portfolio_cutoff/input_quality/capital_available/risk_posture/portfolio_risks/cash_reserve_range, ranked actions with action/role/score/confidence/allocation/entry/tranche/fit/invalidation, covered_call_handoffs, cash_alternative, missing_data, and source_notes.

## Failure conditions

Do not force full deployment; infer account values; rank companies without current price; count correlated tickers as diversification; use one score instead of reasoning; recommend calls before desired ownership; provide exact sizes from stale data; hide wait/pass; or optimize premium at the expense of the portfolio thesis.
