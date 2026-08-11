# Skill — Fundamental Analysis and Fair Value

## Mission

Determine the quality, durability, expectations, and fair-value range of a public company, then state whether the stock is attractive at the current price for the specified horizon.

> A strong company is not automatically a good stock at any price.

The analysis must connect business performance to expectations already embedded in valuation.

## Modes

`daily_update`, `single_stock_deep_dive`, `multi_stock_comparison`, `earnings_event`, `scout_finalist`, `deep`.

## Inputs

Required: company/ticker, current price/timestamp, research cutoff, horizon, market-regime packet, and prior thesis/position context when available.

Useful: filings, earnings releases, investor presentations, transcripts, guidance, segment revenue/margins, cash flow/balance sheet/share count, consensus estimates/revisions with source/date, peers/historical valuation, material news/regulatory filings/industry data.

If current price, shares outstanding, or essential financial data is missing, do not manufacture fair-value precision.

## Source hierarchy

Use regulatory filings/audited financials first, then company earnings/IR disclosures, official industry/regulator data, current market data, reputable reporting, and clearly labeled analyst estimates/interpretation. Management statements are claims, not independent verification.

## Analysis method

### Define the research question

State the decision, horizon, current price, position/watchlist status, and what changed. Avoid generic company summaries.

### Understand the business

Explain how the company makes money, segments/products/geographies/customers, revenue model/unit economics, recurring versus transactional revenue, customer concentration, supplier/channel dependence, capital intensity, cyclicality, and regulation. Identify the few variables that drive equity value.

### Assess business quality

Evaluate market structure/growth, competitive advantage, pricing power, switching costs/ecosystem, differentiation, retention/expansion, execution, management credibility, reinvestment runway, return on incremental capital, and resilience. Separate durable moat from temporary scarcity/narrative advantage.

### Reconstruct financial quality

Cover revenue growth by segment, margins, stock-based compensation, FCF/conversion, working capital, capex, debt/cash/liquidity, dilution/convertibles/buybacks/issuance, acquisitions versus organic growth, GAAP/non-GAAP differences, guidance and revisions. For cyclical names distinguish peak from normalized earnings.

### Evaluate management and capital allocation

Assess guidance accuracy, strategic consistency, disclosure, incentives, buybacks/dividends/debt/acquisitions/capacity investment, and whether capital allocation creates value.

### Analyze competitive and industry structure

Assess competitors/substitutes, customer and supplier power, barriers, technology transitions, capacity additions, regulation/geopolitics, and future margin pressure/expansion. For semis/AI infrastructure explicitly examine customer concentration, dual sourcing, product cycles, capex timing, supply constraints, and internalization/commoditization risk.

### Define the expectations gap

Ask what must be true for today's price to be justified; which growth/margin/multiple/capital-intensity assumptions are embedded; what consensus appears to assume; what evidence may be underweighted; and whether the next catalyst bar is higher than the last result. Use reverse valuation when possible.

### Triangulate valuation

Use suitable methods such as forward P/E, EV/EBITDA/EBIT, EV/revenue with margin normalization, FCF yield, SOTP, DCF, reverse DCF, and historical/peer ranges. Do not average inappropriate methods mechanically. Explain relevance/failure modes, assumption sources/ranges/sensitivities, and use fair-value ranges rather than false point precision.

### Build bear, base, and bull cases

Each case contains operating-driver assumptions, margins, cash-flow/earnings, share count/capital structure, multiple/discount rate, fair-value range, probability judgment, catalysts, and thesis breakers. Probabilities sum to 100%; probability-weighted value is only as good as the assumptions.

### Distinguish thesis from catalyst

State long-term thesis, near/intermediate catalysts, what is priced in, positive/negative surprises, and invalidation conditions. A catalyst without a mispricing is not necessarily an investment opportunity.

### Evaluate strategy suitability

Score separately long-term ownership quality, current valuation attractiveness, near-term event risk, timing suitability, covered-call compatibility, and confidence. Do not collapse everything into one unexplained number.

### Make a clear fundamental conclusion

Choose: `attractive`, `selectively attractive`, `fairly valued`, `expensive but improving`, `priced for perfection`, `unattractive`, or `insufficient evidence`. State price zones/conditions that improve or weaken the conclusion.

## Machine-readable packet

Return ticker/as_of/current_price/research_cutoff, business_quality, financial_quality, expectations_gap, valuation methods and bear/base/bull ranges/probabilities, catalysts, invalidation, fundamental_stance, ownership_quality, entry_attractiveness, covered_call_compatibility, missing_data, and source_notes.

## Failure conditions

Do not equate revenue growth with value creation; ignore dilution/debt/capital intensity; use trailing multiples alone for rapidly changing businesses; use undated forward estimates; call a stock cheap because it fell or expensive because it rose; treat management claims as proof; assign precise fair value from weak inputs; recommend buying solely because the business is excellent; or omit priced expectations.
