# Decision Intelligence Ledger

Trading OS v1 records four linked artifacts rather than a single flat prediction log:

1. **Planning record** — which decision intents/capabilities were selected and which omitted capabilities were checked.
2. **Decision record** — what was known, recommended, and missing at the decision cutoff.
3. **Outcome observation** — what happened at predefined horizons/events and what the user actually did.
4. **Review/change evidence** — process-vs-outcome attribution and evidence for any candidate methodology edit.

Decision records are append-only. If a thesis changes, create a new decision that supersedes the earlier one. The learner may propose candidate edits but never changes stable methodology automatically.

The private repository should store account-specific records. The public Trading OS repository stores only schemas, methodology, and sanitized evaluation cases.
