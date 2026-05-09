# Text Layout v5

Text must fit by contract in every bounded component slot.

## Defaults

- Body copy defaults to `fitPolicy: $textFit.wrapToLines`.
- If overflow remains, shrink within typography bounds.
- Reject cut-off phrases that end mid-structure (`and`, `or`, trailing comma).

## Required

- Respect slot content insets.
- Respect min/max typography tokens.
- Keep readable hold for key statements.

## Forbidden

- clip-as-default for body text in cards;
- text larger than card body bounds;
- mixing independent text motion and card motion with no parent linkage.
