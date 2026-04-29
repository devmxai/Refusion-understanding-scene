# Tutorial Intake

Use this rule when the user provides an After Effects tutorial, Remotion sample,
motion reference, or transcript.

## Goal

Extract reusable engine capability, not a one-off imitation.

## Intake Steps

1. Preserve the raw tutorial text in the project notes or issue tracker.
2. Identify the visual goal.
3. Split the tutorial into motion techniques.
4. Map each technique to the capability registry.
5. Mark what is already supported.
6. Mark what is missing.
7. Choose the smallest reusable implementation slice.
8. Update this skill pack.
9. Add validation fixtures.
10. Add a Present demo only after the underlying capability is real.

## Extraction Table

Use this structure internally:

```text
Tutorial step:
Professional concept:
Registry category:
Current engine status:
Needed schema/model support:
Needed compiler/lowerer support:
Needed preview support:
Needed export support:
Validation fixture:
Reusable beyond this tutorial:
```

## Examples

### Circle Becomes Rectangle And Reveals Text

Professional concepts:

- shape position;
- shape size/cornerRadius morph;
- moving matte reveal;
- text readable hold;
- soft shadow.

Reusable capabilities:

- `Shape > morph`
- `Mask > movingMaskReveal`
- `Effects > shadow`
- `Choreography > handoff`

Do not implement as a single closed preset.

### Modern UI Cards With Counters And Charts

Professional concepts:

- rounded cards;
- counters;
- trim path charts;
- grouped parent motion;
- soft shadows;
- staggered reveal.

Reusable capabilities:

- `Layout > card`
- `Text > counter`
- `Shape > trimPath`
- `Composition > parentGroup`
- `Effects > shadow`
- `Choreography > leaderFollower`

## Present Demo Rule

Present demos are for validating capability. They are not proof that the engine
supports a professional tool unless the underlying capability exists in schema,
compiler/lowerer, preview, and export.
