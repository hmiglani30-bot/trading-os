# Trading OS v1 Candidate

Trading OS v1 is organized around **six canonical decision prompts + one learner + one adaptive planner**.

The user may invoke a named prompt directly or let the planner select the necessary work. The adaptive planner interprets the decision question, current state, and material changes; selects the minimum sufficient capabilities from the skill libraries; expands research only when omitted analysis could change the decision; and produces one decision-first report plus a ledger record.

## Canonical skill libraries

1. Market / macro / sentiment regime
2. Fundamental analysis / fair value
3. Technical analysis / entry timing
4. Portfolio risk / capital allocation
5. Options / covered calls
6. **[Scout / stock discovery and shortlisting](skills/scout.md)**

The [learner](skills/learner.md) evaluates decisions separately.

These are **libraries, not mandatory sequential mega-prompts**. Their internal sections are addressable capabilities. A run may use a few sections from several skills or most sections from one skill.

## Run Scout

Use `skills/scout.md` directly, say **“Run Scout”**, or run:

```bash
python v1/runtime/run_adaptive.py --workflow scout --output-root /path/to/private-runs
```

Live API execution requires `pip install -r v1/requirements.txt` and an authorized `OPENAI_API_KEY`. The runner uses current web research and optional supplied files; it does not retrieve a brokerage account itself. `--scout-evidence-file` accepts dated JSON scan/source evidence, and the existing portfolio, option-chain and previous-report options remain available. Do not put private outputs or inputs in this public repository. `--demo` is a routing/artifact check only.

The Scout default plan runs discovery through ranked decisions. It reports each channel as executed, partial or unavailable and distinguishes actual retrieved rows from a provider's match count. It does not claim a complete market scanner merely because a broad universe was requested. `PORT.SCOUT` remains compatible by handing off to this single canonical prompt.

## Core loop

`intent -> state -> plan -> minimum-sufficient research -> coverage audit -> selective expansion -> synthesis -> challenge -> decision record`

For vague questions such as “What should I do today?”, the planner proactively checks portfolio state, shared market regime, material changes, events, opportunities, and risks, then deep-dives only the names or decisions that can matter today.

Legacy P00–P12 remain unchanged while v1 is evaluated. They are not the active v1 interface and should not be deleted until migration coverage is proven.
