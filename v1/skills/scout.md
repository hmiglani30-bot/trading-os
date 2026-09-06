# Prompt — Scout: Stock Discovery and Shortlisting

## Run Scout

Run this prompt independently by saying **“Run Scout”**, or use it through the adaptive planner's `scout` default plan. Scout is a peer of Fundamental Analysis. Its job is to discover investments, underwrite the strongest candidates and return decisions in the same run. A description of how a future scanner would work is not a completed Scout run.

Default request: **Find stocks worth owning across the available U.S.-listed universe. Search through the eight channels below, compare the finalists with the strongest available alternatives, and return zero to five ranked buy/add/wait decisions with entry conditions, evidence, rejection reasons and a separate covered-call handoff.**

Use an initial 12–24-month ownership horizon and a 4–12-week tactical review window unless the user supplies another horizon. State the actual research cutoff and market-data dates. Missing investment amounts, portfolio files or option chains do not block stock discovery or ownership research. They restrict personalized sizing, portfolio comparisons or precise option recommendations respectively.

## Mission

Find companies the user and researcher would not otherwise think to name. Start with a defined universe and multiple discovery routes, then narrow to a short investment queue using common evidence standards. Optimize prospective combined stock-and-option wealth over a stated horizon, after known costs. Premium yield is not an ownership screen.

This prompt combines the wealth-playbook requirements to find stocks worth owning before screening calls and to compare new money or assignment proceeds with the best alternatives. It owns Scout's canonical rules; the portfolio prompt receives its ranked findings for allocation.

## Establish the universe

Define eligibility before selecting stories. Begin with U.S.-exchange-listed common stocks and tradable ADRs across all sectors. Prefer dated official symbol directories plus verified issuer/instrument mapping. Identify duplicate issuer lines and corporate actions; exclude funds, warrants, preferred shares and test symbols from this common-stock mandate. State the U.S.-listing limitation instead of claiming worldwide coverage.

Proposed starting thresholds, to evaluate prospectively rather than present as optimized:

- **Core:** market capitalization of at least $1 billion and median daily dollar turnover of at least $20 million over the preceding 20 trading sessions.
- **Smaller-company discovery:** market capitalization of at least $300 million and the same turnover measure of at least $5 million; label this lane separately.
- Compute turnover from compatible per-session price and share-volume units. Average share volume, a single day's volume and median dollar turnover are different measurements. If the required series is unavailable, mark the liquidity gate unverified; identify any proxy without claiming the threshold passed.
- Use genuine available history for new listings and spin-offs. Verify the first regular listing date; remove provider-generated interpolated/prelisting records and investigate zero-volume bars before computing indicators. A response containing 255 rows does not establish 255 genuine trading sessions. Report genuine observations used; do not require a 200-day average where 200 sessions do not exist. Such a company can still enter fundamental research.
- Current profitability, a familiar theme and liquid weekly calls are not universal discovery requirements. Unprofitable businesses require a credible funding and economic path during underwriting.

Report the source snapshot, instrument scope and actual eligible count only if calculated. If a complete bulk feed or directory is unavailable, run the supported channels and label the result **a bounded discovery pass**. List the unsearched areas and data gaps. Do not substitute a handpicked watchlist for a verified whole-universe scan.

## Validate sources and coverage

Use current accessible filings, company releases, official calendars and verified market data. Existing read-only broker screeners or saved scans may supply one or more discovery channels: inspect their criteria, dates, sorting, pagination and instrument scope. Do not create, change or save broker scans merely to run Scout.

Keep these quantities separate: provider-reported matching count; rows actually returned; rows retrieved across pages; unique issuers reviewed; qualified candidates. A result reporting 1,000 matches but returning 20 rows establishes only 20 retrieved rows. Deduplicate overlaps without deleting their source provenance. Preserve conflicting provider totals as discrepancies. Paginate where supported and useful; otherwise state the cap. For range-based pagination, verify boundary ties and changing sort values so strict bounds cannot silently omit rows; if this is not possible, report the remaining completeness gap. A saved scan's label does not prove its rules match this prompt.

For each of the eight channels mark **executed**, **partial** or **unavailable**, with source, timestamp, tested scope, returned rows, useful leads and limitation. Web search results support the named issuers found; they do not establish all-market coverage. Separate database matches from human research choices.

Do not infer missing analyst-consensus histories. Raised company guidance is not an analyst revision or a consensus beat unless the separate timestamped evidence exists. Distinguish publication date, financial period, observation date and retrieval date. Treat syndicated copies of the same release as one source family. Record discrepancies instead of averaging incompatible figures.

Validate each quote field's actual observation date and session. A field named `close` can contain the prior session while `last_trade` reflects a newer regular session. Do not label that older field the latest completed-session close based on a tool description. If only a near-close trade is verified, label it a regular-session last-trade reference rather than an official closing price.

Search material issuer events through the actual research cutoff, including after-hours, weekends and holidays after the price reference. A trial result, filing or other material announcement can invalidate the apparent price or option opportunity before the next session. Identify whether the quoted market has had a chance to incorporate the news; suspend a buy or precise overlay recommendation when the post-event price is unknown rather than carrying forward the pre-event conclusion.

## Run eight discovery channels

Take the **union** of the channels. Any one may admit a company to research; do not require every company to satisfy all eight. Up to ten supported leads per channel is a workload cap, not a quota to manufacture names. Related price and earnings signals are not automatically independent confirmation.

| Channel | Discovery question and evidence | False positives to challenge |
|---|---|---|
| 1. Quality and valuation | Which sector peers combine appropriate profitability, cash conversion and valuation unusually well? Use filings, normalized financial histories and current prices. | One-time gains, peak-cycle earnings, incompatible accounting or inappropriate sector ratios. |
| 2. Improving business results | Which issuers raised guidance, improved margins, accelerated orders or credibly exceeded documented expectations? Compare current disclosures with their actual prior baseline. | Acquisitions, easy comparisons, revenue pulled forward or invented consensus revisions. |
| 3. Price leadership | Which eligible stocks show sustained 6- and 12-month relative performance, including a longer measure excluding the latest month? Use sufficient adjusted or total-return history and name the benchmark. | Short squeezes, broken histories, corporate-action errors or duplicate momentum signals. |
| 4. Customer and supplier links | Where does one company's spending become another company's meaningful revenue and incremental profit? Verify named relationships, timing, concentration and economics. | A thematic association or partnership with no material recognized business. |
| 5. Corporate change and selling pressure | Investigate separations, divestitures, strategic reviews, leadership changes and substantiated forced selling using original filings and transaction documents. | Business deterioration called a temporary dislocation, or selling pressure asserted without evidence. |
| 6. Owner and insider activity | Review meaningful insider purchases, original manager letters and new or enlarged positions from a varied manager roster. Check actual Form 4/13F/13D filings and their periods. | Grants or exercises called purchases; price gains called share accumulation; stale holdings treated as current instructions. |
| 7. Filing changes and operating evidence | Compare successive reports and test a specific business question using properly sourced pricing, inventory, utilization, hiring, traffic or shipment observations. | Boilerplate differences, changing sample coverage, seasonality, poor issuer mapping or correlation without economic linkage. |
| 8. Unfamiliar industries and innovation | Rotate through trade publications, technical conferences and original university or industry research; identify listed beneficiaries with a credible commercialization path. | Interesting science without a listed beneficiary, adoption evidence or plausible profits. |

Use sector-appropriate economics for banks, insurers, REITs, cyclical producers and young businesses. A universal P/E or free-cash-flow cutoff is not adequate. Follow who captures profits rather than treating all companies associated with a theme as equivalent.

## Triage and preserve breadth

Create an auditable candidate ledger before narrowing. Retain ticker, verified issuer, sector, new/existing status, channel, source links/dates, measured screen values, actual eligibility status and the decisive business question.

Take up to 20 unique issuers into initial review, up to eight into detailed underwriting and zero to five into the final buy/add/wait queue. In the 20-name research queue, target at least half outside the user's usual themes and at least five sectors. When the known focus is AI/semiconductors, count that breadth explicitly. If the queue is smaller, report both numerator and denominator. These are research targets, not purchase-allocation requirements. Show shortfalls and their reasons; never weaken ownership standards to fill slots.

These workload limits are configurable defaults. Declare any research-budget override and its reason in the run record, and always report the work actually performed. If a pilot reviews 24 leads, record 24 with the pilot override; do not relabel, backfill or silently discard records to claim the default 20 was followed. Distinguish retrieved screen rows, initial reviews and detailed underwriting when applying the budget.

Existing holdings are comparison candidates, not the source of the whole search. Keep unfamiliar-business discovery separate from following the supply chain of a familiar holding. Research priority and investment attractiveness are different: a turnaround may warrant investigation while remaining a wait.

For a monthly review, or when explicitly requested, inspect ten eligible companies outside the usual screen results across sectors. Record the reproducible sampling method or selection rule, snapshot and omissions. This blind-spot audit must not be described as random or representative unless the selection method supports that claim.

## Underwrite finalists

Reuse the canonical fundamental, technical and market prompts for deep candidates. Run shared market/event work once, then apply issuer-specific consequences. Require current issuer evidence plus a distinct corroborating evidence family, and name the few variables that drive value.

Answer for each candidate:

1. Why did it surface now, and what might the market be misunderstanding?
2. What growth, margins, cash conversion and valuation does the current price require?
3. What are plausible bear/base/bull outcomes over the stated horizon, and which assumptions dominate them?
4. What evidence or event could change the market's view, and when?
5. What would invalidate the business thesis or suspend further buying?
6. Why should the next dollar go here rather than the strongest available existing holding, another finalist or waiting?

Normalize GAAP and adjusted earnings, investment/disposal gains, dilution and cyclical economics. Verify each earnings denominator's exact fiscal dates and number of months: transition or spin-off guidance may cover a seven-month stub even when presented under a fiscal-year label. Do not calculate an annual P/E from stub-period EPS. Any annualization must be explicitly labeled as a diagnostic, justify its seasonal comparability and remain separate from actual annual guidance. Confirm current stock-split units, diluted share counts, ADR conversion ratios and currency compatibility across price and earnings. Quarterly earnings multiplied by four are a diagnostic, not a forward estimate. ARR, backlog and contracts are not recognized revenue or profit. Label management targets and researcher assumptions.

Tie entry conditions to sourced valuation or verified price structure. An arbitrary desired discount is an entry preference, not support or fair value. Distinguish a temporary price invalidation from a business-thesis break. Do not invent technical indicators from missing histories or precise probabilities without a defensible model. Missing current essential evidence means research-only or wait, not a fabricated buy.

## Return the investment decision

Lead with zero to five unique ranked finalists and one clear action for each: **buy, add or wait**. A wait finalist must have a specific evidence or price condition for promotion. Allow zero buys. Do not turn an incomplete research lead into a trade-ready recommendation.

For each finalist provide current price/date, business case, discovery channel, valuation assumptions, entry range/trigger, staged-buy condition, principal downside, thesis-break condition, next review event/date, confidence and material missing evidence. Explain the ranking through direct comparisons rather than an opaque aggregate score. Identify which existing holding it beats for incremental capital only when current holdings are actually known; otherwise compare finalists and mark the personalized comparison unavailable.

Return a separate rejected/deferred ledger for every substantively reviewed exclusion: status (**reject**, **watchlist** or **insufficient data**), decisive reason, source/date and reconsideration trigger. Do not claim a rejected company's business is weak merely because its current price is unattractive. A screen-only row may be recorded as **not advanced** with the screen reason, rather than falsely claiming full underwriting.

Compare deployment with the best retained holding, waiting and confirmed cash needs. Do not automatically reinvest premium receipts or repurchase assigned shares. Missing capital permits a clearly illustrative per-dollar allocation or conditional tranche plan, never an invented account budget. Coordinate alternative entry paths so they cannot silently exceed one intended allocation.

## Hand off ownership to options

For each ownership-approved candidate separately choose **own without calls**, **evaluate selective calls** or **defer the overlay**. Missing or poor option liquidity can reject the overlay while leaving ownership attractive. Keep upside uncapped where the premium does not compensate for the relinquished opportunity.

Send eligible candidates to `options_covered_calls.md` for fresh two-sided quotes, spreads, expiry/event comparisons and same-share/same-horizon outcomes against no calls. No recommended contract count or assignment-profit claim may substitute average basis for actual adjusted lots. Reserve shares across existing calls, proposed calls, orders and pending events; verify contract deliverables. Missing lot records do not suspend existing assignment obligations. Scout itself places no trades or schedules.

## Audit and output contract

A completed run delivers findings, not another playbook. Use this report order:

1. Ranked investment decisions and the strongest counterargument.
2. Actual universe/source coverage and eight-channel status table, including all unavailable channels.
3. Candidate funnel: provider matches where known, returned rows, unique initial reviews, deep reviews, finalists, sectors and outside-theme share. Show unknown counts as unknown.
4. Finalist evidence and direct comparisons, with entry and invalidation conditions.
5. Rejected/deferred log and ownership-to-options handoff.
6. What this run could not establish and which process defect, if any, should be corrected.

Attach a compact machine-readable packet to the authorized private report or return it inline if no destination is available. Fields: `as_of`, `prompt_ref`, `run_mode` (`complete_for_declared_scope` or `bounded`), `ownership_horizon`, `tactical_horizon`, `research_budget` (defaults/overrides/reasons/actual_counts), `universe` (source/date/scope/eligible_count/limitations), `channel_status`, `funnel_counts`, `breadth`, `candidate_ledger`, `finalists`, `rejected_candidates`, `options_handoffs`, `missing_inputs` and `next_review`. Within each source preserve `reported_match_count`, `rows_returned`, `rows_retrieved` and `unique_issuers_reviewed` separately when available. In the runtime, place this object under `scout` in the decision record.

Preserve rejected and deferred candidates for forward evaluation. Track business predictions and 1-, 3-, 6- and 12-month stock total returns against appropriate sector and broad-market comparisons; measure option results separately. Include costs, failures and delistings in historical work, using information available at the decision date. One successful run, published anomaly or subsequent winner does not establish a durable advantage.

Keep account identifiers, positions and private scan records out of a public repository. Record prompt version and dates in the private output without copying private evidence into this prompt library.

## Research basis and limits

The discovery design draws on documented practitioner approaches and historical research. These motivate channels; the thresholds, workload limits and breadth targets above are proposed operating choices, not statistically optimized rules.

- [Baron Capital investment approach](https://www.baroncapitalgroup.com/article/baron-capital-investment-approach): industry work, events and customer/supplier investigation.
- [Counterpoint Global process](https://www.morganstanley.com/im/en-us/institutional-investor/strategies/global-insight.html): quantitative screens plus qualitative discovery.
- [Novy-Marx, The Other Side of Value](https://mysimon.rochester.edu/novy-marx/research/OSoV.pdf): profitability alongside valuation.
- [Cohen and Frazzini, Economic Links](https://www.aqr.com/Insights/Research/Journal-Article/Economic-Links-and-Predictable-Returns): customer/supplier information in historical returns.
- [Cohen, Malloy and Nguyen, Lazy Prices](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12885): material changes across company reports.
- [Baillie Gifford academic partnerships](https://www.bailliegifford.com/en/uk/individual-investors/insights/ic-article/2022-q2-academic-partnerships-10012339/): learning outside familiar finance themes.
- [SEC data APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [Nasdaq symbol-directory definitions](https://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs) and [SEC Form 13F guidance](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f): source scope and reporting limitations.
- [McLean and Pontiff](https://onlinelibrary.wiley.com/doi/10.1111/jofi.12365): published predictability can weaken; evaluate the process prospectively.
