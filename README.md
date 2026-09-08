# Trading OS

Use **/full-stock-analysis CBRS** plus optional instructions in a conversation that has this repository in context and GitHub selected. Once the personal Full Stock Analysis skill is installed, **@full-stock-analysis CBRS** is the persistent entry point across chats. A repository file alone does not install a ChatGPT skill.

Read [TRADING_OS_CURRENT.json](TRADING_OS_CURRENT.json) from the repository's default branch to discover the current canonical source automatically. Resolve its active ref to one commit per run, then load [START_HERE.md](START_HERE.md) and the workflow named by the pointer. No branch selection is required from the user.

**Run Scout:** use [scout.md](v1/skills/scout.md) directly, or say “Run Scout” to the adaptive planner. Scout is an independent stock-discovery and shortlisting prompt, alongside Fundamental Analysis. It returns actual ranked findings with honest search coverage.

The active candidate source is `candidate/trading-os-v1-adaptive-planner/v1/skills/`. Scout owns discovery; portfolio allocation consumes its findings. Sentiment remains in market analysis. Edit these originals rather than maintaining a duplicate prompt library.

The candidate is reviewed in [PR #2](https://github.com/hmiglani30-bot/trading-os/pull/2). Legacy P00–P12 remain available for comparison. Private account records do not belong in this public repository.
