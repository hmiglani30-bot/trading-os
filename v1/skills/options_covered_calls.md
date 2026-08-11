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

For precision: ticker, share quantity, lot-level cost basis when relevant, underlying price/timestamp, desired ownership quantity, max acceptable assignment, chain timestamp, expirations/strikes/bid/ask/mid, volume/OI, delta/IV when available, earnings/ex-div dates, technical packet, fundamental/portfolio ownership packets, and supplied tax/liquidity constraints. If chain/portfolio state is stale, give a framework/target delta or strike zone rather than fabricated premium.

## Analysis method

### Reconfirm the ownership decision

State core shares that should not be called, tactical/excess shares eligible, existing assignment exposure, thesis direction, and catalyst asymmetry. Choose `no calls`, `partial calls`, or `full calls`. No calls is valid.

### Validate the option chain

Check quote timestamp, spread, OI/volume, DTE, delta, IV/term structure when available, earnings/event overlap, ex-dividend risk, corporate actions, and live/delayed/stale status. Reject/downgrade illiquid contracts; do not use an old last trade as executable premium.

### Calculate mechanics deterministically

For candidate contracts calculate gross premium, premium yield on current value, premium yield on cost basis when meaningful, static downside cushion, upside to strike, if-called return from current price/cost basis, effective sale price, DTE, and simple annualized premium yield clearly labeled. State bid/mid/limit assumption.

### Compare the counterfactuals

Compare proposed call versus same shares with no call, reasonable higher-strike/lower-coverage alternative, and waiting until after a known catalyst when relevant. Evaluate premium, upside surrendered, assignment proxy, flexibility, downside cushion, and ownership fit. Do not judge success only by expiry worthless.

### Select duration and strike

Balance assignment tolerance, technical resistance/breakout risk, fair value, event calendar, delta, premium, liquidity, theta, and volatility. Use lower delta/higher strike for shares strongly desired, closer strike only for shares genuinely acceptable to sell, shorter duration for flexibility when economics justify it, avoid crossing earnings unless deliberate, and partial coverage when ownership and income goals conflict.

### Distribute across lots

When cost bases differ, ladder by lot basis, supplied tax/holding treatment, willingness to exit, fair value, resistance, liquidity, and total assignment exposure. Contract count must reconcile to eligible shares.

### Evaluate roll or close decisions

For existing calls distinguish original decision, current thesis, remaining extrinsic value, assignment likelihood, roll debit/credit, new cap/duration, and no-action alternative. A roll is a new trade, not an automatic rescue.

### Red-team the recommendation

Ask whether premium is event-driven, strike caps below fair value, strike sits inside breakout zone, assignment conflicts with allocation, spread is too wide, waiting improves information, or the economics depend on a non-executable quote.

## Machine-readable packet

Return ticker/as_of/position_cutoff/chain_cutoff, ownership shares total/to retain/eligible/max assignment, coverage_decision, recommended contracts with expiration/strike/contracts/quote basis/premium/delta/IV/OI/economics/rationale, counterfactuals, event risks, assignment fit, confidence, missing_data, and source_notes.

## Failure conditions

Do not optimize premium before ownership; call away core shares without explicit rationale; use stale quotes; ignore spread/OI/earnings/ex-div; treat annualized weekly premium as expected annual return; ignore upside surrendered; recommend more contracts than shares; treat rolls as costless; or judge strategy only by premium collected.
