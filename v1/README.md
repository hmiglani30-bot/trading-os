# Trading OS v1 Candidate

Trading OS v1 is organized around **five canonical decision skill libraries + one learner + one adaptive planner**.

The user should never need to know which prompt to invoke. The adaptive planner interprets the decision question, current state, and material changes; selects the minimum sufficient capabilities from the skill libraries; expands research only when omitted analysis could change the decision; and produces one decision-first report plus a ledger record.

## Canonical skill libraries

1. Market / macro / sentiment regime
2. Fundamental analysis / fair value
3. Technical analysis / entry timing
4. Portfolio risk / capital allocation / Scout
5. Options / covered calls
6. Learner / retrospective improvement

These are **libraries, not mandatory sequential mega-prompts**. Their internal sections are addressable capabilities. A run may use a few sections from several skills or most sections from one skill.

## Core loop

`intent -> state -> plan -> minimum-sufficient research -> coverage audit -> selective expansion -> synthesis -> challenge -> decision record`

For vague questions such as “What should I do today?”, the planner proactively checks portfolio state, shared market regime, material changes, events, opportunities, and risks, then deep-dives only the names or decisions that can matter today.

Legacy P00–P12 remain unchanged while v1 is evaluated. They are not the active v1 interface and should not be deleted until migration coverage is proven.
