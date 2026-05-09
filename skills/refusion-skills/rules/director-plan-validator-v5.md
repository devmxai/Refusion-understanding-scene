# Director Plan Validator v5

Director briefs must fail closed before planning.

## Hard Validation Gates

- Reject vague intent phrases (`make cool`, `nice animation`, `anything`).
- Require explicit `audience`, `mood`, `primaryFocus`, `rhythm`.
- Require `aspect` token and `durationIntent` token.
- Enforce one primary focal target per beat.
- Reject contradictory mood-motion pairs (for example calm + aggressive whip).
- Reject duplicate semantic elements unless `allowDuplicate=true`.
- Require `primaryCardIndex` for multi-card feature groups.

## Output

Validator returns structured issues with deterministic codes:

- `BRIEF_INTENT_TOO_VAGUE`
- `BRIEF_MISSING_CONTEXT_FIELD`
- `BRIEF_PRIMARY_FOCUS_CONFLICT`
- `BRIEF_MOOD_CONTRADICTION`
- `BRIEF_DUPLICATE_ELEMENT`
- `BRIEF_CARD_GROUP_PRIMARY_MISSING`

Each issue includes:

- `path`
- `severity`
- `suggestedFixPath`
- `suggestedFixValue`
