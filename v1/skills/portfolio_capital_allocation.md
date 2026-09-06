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

Source integration: the supplied September 5, 2026 wealth playbook, P03 (ownership discovery), P17 (next-dollar and assignment-proceeds allocation), and method steps 3, 4, 6, 8, and 11. The rules below adapt those requirements into this canonical module.

### Define the search and apply gates

Declare the research cutoff, ownership horizon, relevant call horizon, actual universe searched, and data limitations. Use a liquid/researchable core universe plus a smaller discovery lane with explicit inclusion/exclusion rules. Search beyond current holdings and include businesses with different earnings drivers; do not present a review of familiar holdings as a market-wide scan. Keep new names distinguishable from additions to existing positions.

Prefer verifiable cash generation, sustainable funding, understandable competitive strengths, and a valuation with plausible upside. Before scoring, reject candidates that fail business, funding, share liquidity, current disclosure, listing, governance, event, or portfolio-fit gates. Separate an ownership rejection from an options rejection: weak option liquidity can rule out calls while leaving uncovered ownership attractive. Label missing evidence individually; do not fill gaps with assumed numbers.

Reuse the market, fundamental, and technical modules. For survivors, examine what growth and margins the price requires, valuation scenarios, catalysts, downside mechanisms, and entry conditions. Use source-linked assumptions and current prices. Distinguish reported earnings from recurring economics. Include events inside the contemplated ownership and call windows. Do not rank by premium yield or let a score replace the investment case.

### Return a decision, not a ticker list

Return no more than five unique finalists, plus a rejected-candidate log. For each finalist give:

- Rank, buy/add/wait action, proposed ownership role, and why it merits capital at the observed price.
- Entry range or trigger, staged deployment condition, valuation assumptions, and the principal downside scenario.
- Evidence that would strengthen or invalidate ownership, the next review event/date, and confidence or missing data.
- The existing holding or other finalist it beats for incremental capital, with an explicit comparison; retain worthwhile current holdings even when new purchases rank ahead.
- A separate choice of own without calls, own with selective calls, or defer/reject the overlay, with the reason and the upside that a call would surrender.

The rejected-candidate log must identify each substantively evaluated exclusion, its decisive failed gate or price objection, source/date, and what would allow reconsideration. Distinguish rejected, watchlist, and insufficient-data cases. Report the universe and funnel counts only when actually tracked. Do not invent candidates merely to fill five places.

Return two distinct outputs: the ranked ownership shortlist and the covered-call handoff drawn from ownership-approved candidates. Pass the latter to the options module for fresh two-sided quotes, expiry/event comparison, eligible lots, existing share commitments, and a same-quantity comparison against no call. Attractive ownership does not require immediate call selling.

### Decide how proceeds are used

Compare new purchases with adding to the best retained holding, waiting, and the user's confirmed cash needs and reserves. Do not automatically reinvest premiums or repurchase assigned shares. Rank the next use of capital and state the condition for deployment. Missing exact available capital blocks exact dollar sizing, not the shortlist; use clearly illustrative allocations or conditional tranches. If nothing clears the ownership hurdle, return a watchlist or cash rather than force a buy.

## Machine-readable packet

Return as_of/portfolio_cutoff/input_quality/capital_available/risk_posture/portfolio_risks/cash_reserve_range, ranked actions with action/role/score/confidence/allocation/entry/tranche/fit/invalidation, covered_call_handoffs, cash_alternative, missing_data, and source_notes. In scout mode also return searched_universe, ownership_horizon, call_horizon, finalist_count, rejected_candidates (reason/source/as_of/reconsideration_trigger), uncovered_ownership_reason, and next_review for each finalist.

## Failure conditions

Do not force full deployment; infer account values; rank companies without current price; count correlated tickers as diversification; use one score instead of reasoning; recommend calls before desired ownership; provide exact sizes from stale data; hide wait/pass; or optimize premium at the expense of the portfolio thesis.
