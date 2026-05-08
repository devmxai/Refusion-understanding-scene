# Validation

Use this checklist before returning ReFusion JSON.

## JSON Integrity

- Return one complete JSON object.
- The first non-space character must be `{`.
- The final non-space character must be `}`.
- The closing `}` must belong to the same root object. A scene that starts with
  `{` but does not end with `}` will be rejected by ReFusion as an incomplete
  paste.
- No Markdown around JSON.
- No comments.
- No trailing commas.
- No truncated fragments.
- Never split one scene across multiple chat messages.
- For 50-60 second demos, write compact JSON or provide a `.json` artifact when
  the environment supports files; do not rely on a long mobile paste that may be
  cut off.
- Root has `directorPlan` and `sceneProgram`.
- `directorPlan.schemaVersion` is `refusion.motion-director/v1`.
- `sceneProgram.schemaVersion` is `refusion.scene-program/v1`.

## Security

Forbidden keys anywhere:

```text
code, script, function, eval, imports, remoteImports, shaderSource, html, css,
jsx, react, gsap
```

No URLs unless the user and engine explicitly support that asset path.

## Timing

- `durationMs`, `startMs`, `endMs`, `timeMs`, and `frameRate` are numbers.
- Beats stay inside `durationMs`.
- Overlapping distinct-component beats must explicitly say they are parallel,
  while/meanwhile, alongside, or during another motion.
- Overlapping shared-component beats must explicitly say they are a handoff,
  morph, transform, expand, collapse, or becomes transition, and they must
  animate disjoint property groups.
- Primitives stay inside owning beats.
- Primitive `beatId` points to an existing beat.
- The owning beat includes the primitive `targetComponentId` in
  `componentRefs`.
- Layer `durationMs` covers all local keyframes.
- Project-time channels declare `timeBasis: "project"`.
- No empty channels. Remove channels without keyframes.
- No same-target/same-property overlap unless deliberately authored as one
  ordered channel.
- Important motion does not silently use linear timing when the user asked for
  cinematic, professional, smooth, Easy Ease, Speed Graph, or After Effects-like
  motion.
- Scene does not end before all child motion completes.
- Visible component final motion should not land exactly on the final scene
  boundary without a resolve/hold moment.
- Text has readable hold when important.
- Text reveal/typewriter channels must finish early enough to leave readable
  hold inside the owning layer.
- Final visible motion should leave completion hold unless it exits via
  opacity/scale to zero or belongs to a background, mask, or transition cover.

## Director Plan Alignment

- Every beat references existing components.
- Every primitive targets an existing component.
- Every primitive maps to a real Scene Program channel.
- Background fade primitives are implemented by an actual opacity channel, not
  only static opacity properties.
- Typewriter primitive maps to `typewriterProgress`.

## Scene Program

- Every layer has `id`, `name`, `kind`, `startMs`, `durationMs`, and
  `elements`.
- Every element has `id`, `kind`, and valid `properties`.
- Every animation is represented by a channel with sorted keyframes.
- Use stable semantic IDs, not random UUID-like names.
- Do not create excessive layers for a simple scene.

## Mask Reveal And Shape Morph

- Use `kind: "mask"` only when a visible target must be revealed by a matte or
  wipe.
- A mask element should declare `maskTarget`, `maskMode`, and
  `revealDirection` so the timeline remains understandable when opened later.
- `movingMaskReveal` and `maskReveal` values are normalized progress values
  from `0.0` to `1.0`.
- Shape morphs should animate canonical `width`, `height`, and
  `cornerRadius`, or use the supported aliases `morphSize` and `roundness`.
- Do not make shape morphs by swapping separate layers on/off unless the prompt
  explicitly requests a hard cut.

## Typewriter

Correct:

```json
{
  "property": "typewriterProgress",
  "keyframes": [
    { "timeMs": 0, "value": 0.0, "easing": "linear" },
    { "timeMs": 1200, "value": 1.0, "easing": "linear" }
  ]
}
```

Wrong unless deletion/backspace is explicitly requested:

```json
{
  "property": "typewriterProgress",
  "keyframes": [
    { "timeMs": 0, "value": 1.0 },
    { "timeMs": 1200, "value": 0.0 }
  ]
}
```

## Professional Quality

Reject and rewrite if:

- animation feels random;
- scene looks like a web page translation rather than a native motion
  composition;
- the output contains HTML/CSS/JS/React/Remotion code;
- timing bypasses SpeedyGraph when professional movement was requested;
- effects are invented or unsupported;
- next motion starts before the prior motion resolves;
- text appears in the wrong contrast;
- visible motion is not editable;
- the Director Plan and Scene Program disagree;
- a scene relies on unsupported effects but presents them as real.

## Local Validator

When this repository is available, validate every generated scene before giving
it to a user:

```bash
python3 scripts/validate_scene_program.py skills/refusion-skills/examples/revival-premium-app-demo-60s.json
```

The validator is intentionally stricter than casual JSON parsing. Passing it
does not replace app import testing, but failing it means the scene is not ready
to paste into ReFusion.
