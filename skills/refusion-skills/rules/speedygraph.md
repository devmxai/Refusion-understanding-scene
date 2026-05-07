# SpeedyGraph

Use this rule for animation timing, easing, Speed Graph behavior, or Motion Blur
velocity semantics.

## Principle

Bezier control points are the cubic timing execution truth.

Speed, velocity, influence, preset names, and graph handles are authoring inputs
or computed views. They must compile into executable Bezier timing through the
official ReFusion timing contract.

Forbidden state:

```text
UI/agent writes velocity metadata
but the evaluator consumes a different Bezier
```

## Required Presets

Use these names when authoring timing:

| Preset | Meaning | Use |
|---|---|---|
| `linear` | constant progress | typewriter, progress, mechanical loops |
| `easyEase` / `f9` | AE-like smooth ease | default natural motion |
| `slowFastSlow` | slow start, fast middle, slow end | cinematic hero motion |
| `fastSlow` / `easeOut` | fast start, soft landing | arrivals, settling |
| `slowFast` / `easeIn` | slow start, fast end | exits, launches |
| `fastSlowFast` | fast, plateau, fast | hover/hold-in-middle motion |
| `whip` / `snap` | punchy accent | badge, button, fast UI action |
| `customSpeedGraph` | authored curve | exact motion design |

## Timing Taste

- Hero card entrance: `slowFastSlow`.
- Landing motion: `fastSlow`.
- Exit or throw: `slowFast`.
- Button press: `whip`.
- Typewriter: `linear`.
- Large spin/rotation: `slowFastSlow` plus Motion Tile and Motion Blur if
  blank edges or speed trails are likely.

## Motion Blur

Motion Blur must follow authored velocity:

- `slowFastSlow`: blur weak at start/end, strongest near middle.
- `fastSlow`: blur strongest near start.
- `slowFast`: blur strongest near end.
- `linear`: stable blur strength.

Do not fake Motion Blur with Gaussian Blur. Gaussian Blur is a separate visual
effect, not velocity blur.

## Agent Authoring Rules

When asked for professional motion:

1. choose a timing preset for every important segment;
2. use linear only when it is semantically correct;
3. keep one property in one ordered channel;
4. avoid many micro-keyframes when one Bezier segment is sufficient;
5. never use random timing labels unknown to ReFusion.

## Clip Speed Ramp Boundary

SpeedyGraph controls property interpolation such as position, rotation, scale,
opacity, blur, and effect amount.

It does not control media playback time, clip speed ramp, time remapping,
reverse playback, or freeze-frame logic. Those require separate contracts.
