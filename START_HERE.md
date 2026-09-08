# Trading OS — current source discovery

Read [TRADING_OS_CURRENT.json](TRADING_OS_CURRENT.json) from this repository's default branch. Resolve its active_ref to the current commit, then read the entry_point and full_stock_analysis paths at that immutable commit. The active source contains the six canonical libraries, planner, registry and schemas.

Use **/full-stock-analysis TICKER** plus optional instructions in a conversation that knows this repository and has GitHub selected. Once installed, **@full-stock-analysis TICKER** supplies that repository context across chats. The slash spelling is a conversational alias, not a native registered command. This performs deep market/sentiment, fundamental and technical research, adding portfolio and options work when relevant, and preserves the findings below a combined decision brief. The user should never need to specify a branch or repeat the workflow.

Refresh source discovery at each run. Do not choose a branch by recency, silently reuse a previous chat's commit, or treat legacy prompts here as the current source. Report an access failure as a current-version verification limitation. Maintainers change the pointer when the canonical source moves and verify the target before announcing completion.
