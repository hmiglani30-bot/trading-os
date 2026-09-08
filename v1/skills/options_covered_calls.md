# Skill — Options and Covered-Call Overlay

## Mission

Decide whether to sell covered calls at all, how much of the position may be overwritten, and which expiry/strike tradeoff best matches ownership thesis, event risk, and assignment tolerance.

Mandatory sequence:

```text
retain the stock? → desired owned shares → acceptable assignment shares → no/partial/full calls → expiry/strike comparison
```

Premium is not free return; a call exchanges upside and flexibility for cash and limited downside cushion.

## Modes

`weekly_covered_call`, `existing_position`, `earnings_event`, `roll_review`, `multi_lot_distribution`, `morning_update`.

## Required inputs

For precision: ticker, share quantity, lot-level cost basis when relevant, underlying price/timestamp, desired ownership quantity, max acceptable assignment, chain timestamp, expirations/strikes/bid/ask/mid, volume/OI, delta/IV when available, earnings/ex-div dates, technical packet, fundamental/portfolio ownership packets, and supplied tax/liquidity constraints. For a weekend or holiday dry run, use timestamped last-session bid/ask references, mark every premium as non-executable, and require a refreshed quote before a trade. If quotes are absent, give a strike/condition without fabricated premium.

## Analysis method

### Reconfirm the ownership decision

State core shares that should not be called, tactical/excess shares eligible, existing assignment exposure, thesis direction, and catalyst asymmetry. Choose `no calls`, `partial calls`, or `full calls`. No calls is valid. Reconcile the planned retained shares under partial and full assignment. If existing calls can sell more shares than the desired retention target allows, show either the priced close/roll needed or an explicit temporary willingness to sell those shares. Do not promise a core holding that existing obligations can remove.

### Validate the option chain

Check quote timestamp, spread, OI/volume, DTE, delta, IV/term structure when available, earnings/event overlap, ex-dividend risk, corporate actions, and live/delayed/stale status. Reject/downgrade illiquid contracts; do not use an old last trade as executable premium. Use the bid as a conservative sell reference and the ask as a conservative close reference, with spread and depth limits. A zero bid is not income; reject unusable spreads. Delta is a model sensitivity and rough assignment proxy, not a validated real-world probability.

### Calculate mechanics deterministically

For candidate contracts calculate gross premium, premium yield on current value, premium yield on cost basis when meaningful, static downside cushion, upside to strike, if-called return from current price/cost basis, effective sale price, DTE, and simple annualized premium yield clearly labeled. State bid/mid/limit assumption.

### Compare the counterfactuals

Compare proposed call versus same shares with no call, reasonable higher-strike/lower-coverage alternative, and waiting until after a known catalyst when relevant. Evaluate premium, upside surrendered, assignment proxy, flexibility, downside cushion, and ownership fit. Do not judge success only by expiry worthless.

### Select duration and strike

Balance assignment tolerance, technical resistance/breakout risk, fair value, event calendar, delta, premium, liquidity, theta, and volatility. Use lower delta/higher strike for shares strongly desired, closer strike only for shares genuinely acceptable to sell, shorter duration for flexibility when economics justify it, avoid crossing earnings unless deliberate, and partial coverage when ownership and income goals conflict.

### Distribute across lots

Load the user's explicit assignment objective before any lot calculation. If they require no stock-only assignment loss, allocate actual adjusted lots with basis at or below each strike, reserve each share once, and apply their realized-gain or tax preference among eligible lots. Never silently substitute average cost or the broker's default disposal method. Without adjusted lot inventory, state the maximum eligible basis and quantity needed as a conditional proposal; neither profit nor loss is verified. Missing lot data does not pause existing obligations: assignment can occur automatically. When a no-stock-loss requirement is binding, an existing-call recommendation must include a timely close/roll contingency for contracts whose qualifying lots cannot be reserved, rather than leaving the conflict unresolved until after assignment.

Reconcile deliverables, current short calls, open sell orders, and pending assignments before adding contracts. Shares available for stock sale do not establish uncovered call capacity. Separate broker-reported assignment P&L, a proposed lot-selection scenario, net option lifecycle P&L, and remaining unrealized stock P&L. Check whether assignment proceeds already include option premium before adding it again.

### Evaluate roll or close decisions

For existing calls distinguish original decision, current thesis, remaining extrinsic value, assignment likelihood, roll debit/credit, new cap/duration, and no-action alternative. A roll is a new trade, not an automatic rescue. Show both legs, net cash, realized option P&L, the new cap and expiry, and the no-action alternative. Original premium is sunk for the current hold-versus-close decision; do not count it as new income. Accepting assignment is valid when sale at the strike fits the ownership decision and lot constraint.

### Compare total economic outcomes

At a common starting mark, share count, and terminal date, show no call, proposed partial coverage, and a reasonable alternative at several explicit stock-price outcomes. For a new call, option P&L per share is premium minus max(terminal price minus strike, zero). Separate this from stock P&L and selected-lot tax reporting. For existing positions, compare future outcomes from the current option mark; do not present opening credit as profit already earned. Include fees and spread assumptions when known. Do not impose a weekly yield quota that forces unacceptable sale prices or illiquid contracts.

### Red-team the recommendation

Ask whether premium is event-driven, strike caps below fair value, strike sits inside breakout zone, assignment conflicts with allocation, spread is too wide, waiting improves information, or the economics depend on a non-executable quote.

## Machine-readable packet

Return ticker/as_of/position_cutoff/chain_cutoff, ownership shares total/to retain/eligible/max assignment, coverage_decision, recommended contracts with expiration/strike/contracts/quote basis/premium/delta/IV/OI/economics/rationale, counterfactuals, event risks, assignment fit, confidence, missing_data, and source_notes.

## Failure conditions

Do not optimize premium before ownership; call away core shares without explicit rationale; use stale quotes; ignore spread/OI/earnings/ex-div; treat annualized weekly premium as expected annual return; ignore upside surrendered; recommend more contracts than shares; treat rolls as costless; or judge strategy only by premium collected.

## Preservation in a full run

In full stock analysis involving existing calls, preserve a numerical keep-versus-close comparison from the same current starting mark, share count and terminal date, in addition to any historical realized-profit calculation. Preserve no-call and partial/higher-strike alternatives where applicable. Follow [Full Stock Analysis](../workflows/full_stock_analysis.md) for the shared coverage and saved-record contract.
