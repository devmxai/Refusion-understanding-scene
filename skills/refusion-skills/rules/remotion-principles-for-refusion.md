# Remotion Principles For ReFusion

Use this rule when borrowing ideas from Remotion-style programmatic video.

Sources consulted:

- Remotion skills repository: `https://github.com/remotion-dev/skills`
- Remotion docs concepts: compositions, frame-based animation, Sequence,
  interpolation, spring, width/height/fps/duration metadata.

## What To Borrow

Borrow the mental model:

- a composition has width, height, fps, and duration;
- visible elements have explicit time spans;
- frame/time is deterministic;
- animations derive values from the current frame/time;
- sequences organize timing and reuse;
- assets are explicit;
- render output should match preview semantics.

## What Not To Borrow

Do not output:

- React;
- JSX;
- Remotion components;
- HTML;
- CSS;
- `useCurrentFrame()`;
- `interpolate()`;
- `<Sequence>`;
- `<Composition>`;
- `<Img>`;
- `<Video>`.

Those are Remotion execution surfaces. ReFusion execution is SceneProgram JSON.

## Translation Table

| Remotion idea | ReFusion-native equivalent |
|---|---|
| Composition width/height/fps/duration | `sceneProgram.canvasWidth/canvasHeight/frameRate/durationMs` via wrapper |
| Sequence from/duration | layer `startMs` and `durationMs`, or Director beat |
| useCurrentFrame | timeline `timeMs` evaluated by ReFusion |
| interpolate | channel keyframes + SpeedyGraph |
| Easing.bezier | SpeedyGraph Bezier timing |
| AbsoluteFill/layering | layer stack + full-canvas shapes |
| Img/Video component | image/video layer/element where supported |
| reusable component | semantic component + recipe |
| render check | ReFusion import/preview/export validation |

## Practical Rules

- Convert frame counts to milliseconds using `1000 / fps`.
- Prefer reusable scene recipes over raw copied code.
- Explicitly declare duration and holds.
- Keep timing deterministic.
- Use SpeedyGraph instead of ad-hoc interpolation formulas.
- Use Director beats instead of nested JSX sequences.

## Professional Lesson

Remotion's strength is not React itself. Its useful lesson for ReFusion is:

```text
deterministic timeline -> reusable scene blocks -> frame-accurate values
```

ReFusion should express the same discipline through editable DirectorPlan and
SceneProgram data.
