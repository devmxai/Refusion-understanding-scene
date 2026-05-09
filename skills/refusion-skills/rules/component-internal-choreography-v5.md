# Component Internal Choreography v5

Every professional component has micro-beats inside itself.

## Required Order

1. container shell enters;
2. icon enters;
3. label/body enters;
4. interaction affordance enters;
5. exit in reverse order unless design says otherwise.

## Prompt Input Bar Contract

- Shell appears first (pop or stretch).
- Plus icon and send icon are slot-bound and optically centered.
- Text reveal starts only after shell and icons are stable.
- Enter action uses coherent follow-through, not raw opacity drop.

## Reject

- child elements animating before parent shell exists;
- text and icon moving in unrelated directions with no handoff;
- uniform fade-only choreography for all children.
