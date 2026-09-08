# Trading OS repository instructions

This repository is the methodological source, not a destination for private account records.

## Current-version discovery

The default branch's `TRADING_OS_CURRENT.json` is the stable discovery entry point. Resolve its active ref to one commit at run start and use that commit consistently. Do not ask the user to repeat a branch or choose files. A saved SHA reproduces a past run; it does not define the latest run.

`@full-stock-analysis TICKER [optional instructions]` runs the full workflow named in that pointer. Plain text `/full-stock-analysis` and `/full stock analysis` are aliases interpreted by the installed skill, not registered platform slash commands.

## Changes and verification

For authorized methodology edits, edit the canonical source referenced by the pointer. Preserve legacy prompts. If the canonical ref or workflow location changes, update the default-branch pointer and entry-point instructions in the same release operation; verify the pointer resolves to the tested files. Do not point it at unvalidated or inaccessible content.

Run the existing tests plus relevant workflow/record checks before marking a change complete. Use synthetic public fixtures for tests. Source hashes, complete packets and coverage records demonstrate provenance and inspectability; they do not prove superior investment returns.

Keep source instructions authoritative and avoid copying whole specialist prompts into wrappers. The installed personal skill contains discovery and invocation only; the workflow and analytical requirements live here.

