# Effects And Renderer Contract

Use this rule when a scene uses effects or when a prompt asks for professional
visual treatment.

## Principle

Effects are editable scene data. They are not hidden overlays, HTML filters,
CSS filters, bitmap tricks, or renderer-only hacks.

If the engine does not support an effect, do not pretend it does. Either omit
it, approximate with supported editable primitives, or state the limitation.

## Current Important Effects

### Motion Blur

Use for visible high-speed movement:

- fast swipe;
- spin transition;
- zoom push;
- scale burst;
- fast product-card movement;
- kinetic title arcs.

Motion Blur should be driven by SpeedyGraph velocity, not only by a static
amount.

### Motion Tile / Edge Fill

Use when rotation, scale-down, zoom-out, position movement, or Motion Blur may
expose blank canvas areas.

Expected meaning:

- fills blank areas outside the original source;
- supports mirrored continuation when requested;
- does not change the transform anchor;
- does not mutate rotation center;
- should feed Motion Blur so black gaps are not repeated.

### Gaussian Blur

Use for:

- soft background separation;
- depth;
- intentional defocus.

Do not use Gaussian Blur as fake Motion Blur.

## Preferred Visual Chain

When combining these effects:

```text
Motion Tile / Edge Fill
-> Motion Blur
-> Gaussian Blur
```

## Safe Authoring Behavior

When an effect is used, document it as an editable effect instance or animatable
effect parameter in the SceneProgram style accepted by ReFusion docs.

If uncertain about exact effect serialization, keep the scene valid using
supported transform/opacity/shape channels and mention the effect in
DirectorPlan intent rather than inventing unsupported JSON keys.

## Stop List

Do not:

- use CSS filters;
- use HTML canvas;
- use hidden code;
- use remote assets as effect processors;
- create overlay-only effects;
- claim export parity for an unsupported effect;
- use Motion Tile in a way that changes rotation pivot;
- use bitmap/proof/media-retriever concepts as realtime output.
