---
name: refusion-skills
description: Use when generating, repairing, validating, or reviewing ReFusion motion scenes, Scene Program JSON, Director Plans, tutorial-derived motion capabilities, professional timing, editable keyframes, or agent-authored animation scripts for the ReFusion engine.
metadata:
  tags: refusion, motion-graphics, scene-program, keyframes, timing, choreography
---

# ReFusion Skills

Use this skill whenever a task involves ReFusion scene generation, motion
script authoring, tutorial-to-capability extraction, timing review, JSON
repair, modern motion design, SpeedyGraph timing, effects authoring, or
external-agent scene direction for the ReFusion engine.

## Core Rule

Return complete ReFusion JSON only when the user asks for a scene. Do not return
Markdown around the JSON. Do not use executable code, JSX, CSS, functions,
imports, shader code, remote code, or comments.

The most common app rejection is incomplete paste. Before returning a scene,
verify the response starts with the first `{` and ends with the final `}` of the
same JSON object. Never split a JSON scene across multiple chat messages. For
long 50-60 second scenes, prefer a compact scene with reusable layers and, when
the environment supports files, write a `.json` file rather than asking the user
to copy a truncated chat fragment.

ReFusion is not an HTML design surface. It is a native editable video/motion
scene engine. Use Shapes, Text, Image, Video, Scene Program layers, channels,
keyframes, SpeedyGraph, and official effects. Treat Open Design and Remotion as
sources of design/motion discipline only; do not copy their HTML/React execution
surface into ReFusion output.

Preferred root shape:

```json
{
  "directorPlan": {},
  "sceneProgram": {}
}
```

`directorPlan` is the choreography contract. `sceneProgram` is the editable
executable scene.

## Required Workflow

1. Understand the visual goal.
2. Run the Creative Director role: define visual thesis, hierarchy, mood, and
   semantic components.
3. Run the Motion Director role: plan ordered beats, primitives, holds,
   handoffs, and timing.
4. Run the Technical Scene Writer role: compile primitives into real layers,
   elements, channels, keyframes, SpeedyGraph timing, and official effects.
5. Run the QA Critic role: validate timing, holds, contrast, effects,
   editability, and professional taste.
6. Return only complete JSON.

If this repository is available locally, run this before delivery:

```bash
python3 scripts/validate_scene_program.py path/to/scene.json
```

If the validator fails, repair the JSON first. Do not tell the user to paste a
scene that has not passed JSON integrity checks.

## Load Rules As Needed

- For native scene intelligence, component-safe prompt/card/panel contracts,
  closed vocabulary planning, Beat Grammar, and Visual Closure preparation, read
  [rules/native-scene-intelligence.md](rules/native-scene-intelligence.md).
- For schema, coordinates, supported properties, icons, and examples, read
  [rules/scene-program-json.md](rules/scene-program-json.md).
- For the ReFusion-native authoring pipeline, four internal production roles,
  JSON-only output, and Open Design/Remotion exclusion rules, read
  [rules/native-motion-scene-author.md](rules/native-motion-scene-author.md).
- For SpeedyGraph, Bezier execution truth, Easy Ease/F9, Slow-Fast-Slow,
  velocity/influence, and Motion Blur velocity semantics, read
  [rules/speedygraph.md](rules/speedygraph.md).
- For official effects such as Motion Blur, Motion Tile / Edge Fill, Gaussian
  Blur, and shader/renderer boundaries, read
  [rules/effects-and-renderer.md](rules/effects-and-renderer.md).
- For modern After Effects/Alight Motion style scene recipes, social ads,
  app promos, kinetic titles, prompt scenes, and premium motion language, read
  [rules/modern-motion-design.md](rules/modern-motion-design.md).
- For translating useful Remotion ideas into ReFusion without React/HTML,
  read [rules/remotion-principles-for-refusion.md](rules/remotion-principles-for-refusion.md).
- For adapting Open Design skills/design systems into ReFusion-native shapes
  and motion scenes, read
  [rules/open-design-adaptation.md](rules/open-design-adaptation.md).
- For professional time ownership, holds, completion, layer lifetime, and
  future contract requirements, read
  [rules/professional-timing-contract.md](rules/professional-timing-contract.md).
- For motion direction, readable holds, handoffs, and anti-random animation
  rules, read [rules/choreography.md](rules/choreography.md).
- For composition-first workflow, Scene Clip containers, root/scene/layer scope
  responsibilities, and editing existing scenes or mentioned elements, read
  [rules/composition-workspace.md](rules/composition-workspace.md).
- For transitions between clips/scenes, boundary-frame truth, and the
  professional Zoom In Camera contract, read
  [rules/transitions.md](rules/transitions.md).
- For supported and planned capabilities, categories, and how new tutorial
  tools should be registered, read
  [rules/capability-registry.md](rules/capability-registry.md).
- For converting After Effects or motion tutorials into reusable engine
  capability, read [rules/tutorial-intake.md](rules/tutorial-intake.md).
- For preflight checks before returning JSON, read
  [rules/validation.md](rules/validation.md).

If your environment cannot open these relative rule files, use the repository
root file `REFUSION_SCENE_SKILL_FULL.md` instead. It contains this skill, every
rule file, and the example JSON in one document.

## Non-Negotiable Professional Rules

- Do not create random simultaneous animation.
- Do not output HTML, CSS, JSX, JavaScript, GSAP, Remotion code, or Open Design
  artifacts as the ReFusion scene source of truth.
- Do not translate a website template directly. Translate design intelligence
  into editable Shapes/Text/Image/Video layers.
- Do not author prompt bars, search bars, cards, or panels as loose text placed
  over random rectangles when a component contract exists. Use parent/slot,
  textFrame, contentInsets, and readable hold rules.
- Do not bypass SpeedyGraph or MotionInterpolation truth when authoring timing.
- Do not write velocity metadata without executable Bezier or approved timing
  truth.
- Do not invent unsupported effects or claim parity for planned effects.
- Do not let a scene end before all child motion completes.
- Important text must have a readable hold unless the user asks for kinetic
  typography.
- If two motions touch the same component/property, they must be one ordered
  track or an explicit handoff.
- A layer's visual lifetime must cover its keyframes.
- Typewriter text uses one full text element plus `typewriterProgress`.
- Scene Program must implement the Director Plan; they may not disagree.
- Every visible motion must be represented by editable keyframes.
- A generated scene should become one editable Scene Clip container; do not
  scatter one scene across many root timeline clips.
- Existing-scene or `@mention` edits must target stable existing IDs and must
  not create unrelated new elements.
- Transitions must be seam-aware boundary effects. For live video presets such
  as Zoom In Camera, animate the live video surface over the transition window
  rather than freezing boundary-frame thumbnails. Boundary frames are exact
  seeds/fallbacks for AI and non-live transitions, not a substitute for live
  playback.
- New preset/AI video transition creation is locked until the native
  professional compositor reports complete interactive readiness: dual video
  sampling, temporal motion blur, mirror-edge tiling, preview parity, Live
  Scrub parity, and playback parity. Manual may open only as an authoring
  scope in the existing focused TimelinePanel. Legacy native
  `manualTransform` compositor rendering must stay disabled for Manual
  authoring in preview/liveScrub/playback. Manual lanes must not suppress
  Stage5 native preview ownership in any interactive mode. Manual transition
  authoring still writes real graph/keyframe data; runtime visual execution for
  preview/playback/Live Scrub must come from the Stage5 master path before
  parity can be claimed. Do not claim export parity until export consumes the
  same compositor output.
  Current runtime status: Manual Transition transform/opacity now route through a
  dedicated Stage5 visual runtime state bridge (Master Clock -> master
  evaluation -> live scrub program -> Stage5 runtime state), and the runtime
  state is applied to both scrub overlay and visible player-surface ownership
  paths. Runtime follow-up rule: evaluate Manual Transition visuals against the
  effective motion project plus explicit preview-time clock override, push
  runtime visual source config during active scrub sessions (do not wait for
  scrub end), and reject Add Key when the playhead is outside the real active
  transition window (no silent clamp). Manual FX shader parity still requires
  dedicated native/Media3 slices.
  Transition-focus runtime rule: when Manual Transition scope is active, seam
  time and source-window descriptors must resolve in root timeline time before
  runtime projection to avoid local/root drift in Stage5 visual state
  application.
  Transition-focus keyframe-time rule: Manual Transition keyframe authoring
  must use the same visible active transition window shown in the focused
  timeline. Do not expose a wider editor range that can scrub visually while
  Add Key validates against a narrower hidden window.
  Transition-focus value-write rule: keyframe value edits in Manual Transition
  scope must resolve and persist through scoped transition identity
  (`transitionId + sourceSceneId`) rather than root-track-only lookup. UI value
  changes that bypass scoped transition identity are invalid.
  Transition-focus compact-clip rule: when manual transition windows become
  very narrow, timeline clip chrome must degrade gracefully without `RenderFlex`
  overflow banners or hidden hit areas; preserve time truth and keep Add Key
  scoped to the exact visible transition window.
  Transition-focus visual-width rule: narrow transition windows may use
  minimum clip visual width in UI layout for legibility, but this must never
  alter active transition start/end times or keyframe time truth.
  Scene-scope video truth rule: scene-scope video timeline entries used by
  manual transition authoring must remain real media clips (not placeholder
  shells) so scoped outgoing/incoming preview-source windows bind to actual
  media and Stage5 runtime state applies to the correct sources.
- Professional Canva layer unification is the next binding architecture rule:
  video, image, text, shape, masks, and future generated objects must all
  resolve to composition-layer truth before Animate/FX/Key/Value/Graph can
  claim parity. Video must resolve through `MotionLayerKind.video` +
  `MotionElementKind.videoClip` + source binding, not raw transport/player clip
  identity. Manual Transition Add Key must use the same transition-local time
  domain shown to the user. Manual Transition Scale/Opacity/Position/Rotation
  must target outgoing/incoming/both layer instances through a unified target
  resolver, then flow through Master Clock, Value Truth, and a shared Visual
  Layer Program before preview/playback/Live Scrub/export renderer adapters.
  Do not treat a PlayerView transform, thumbnail, poster, or boundary-frame
  preview as final layer parity.

## Current Engine Boundary

ReFusion is moving toward a Professional Scene Timing Contract. Until that
contract is fully implemented, be conservative:

- use explicit beats and components;
- use readable holds;
- keep same-property motion in one channel when authoring Scene Program JSON;
- avoid ambiguous overlaps;
- avoid claiming unsupported effects are real.

## Prompt Template

```text
You are a ReFusion Scene Director.
Read the ReFusion Skills instructions.
Return exactly one complete JSON object with directorPlan and sceneProgram.
Use schemaVersion refusion.motion-director/v1 and refusion.scene-program/v1.
Use numeric startMs, endMs, durationMs, timeMs, and frameRate.
Use center-origin 1080x1920 canvas unless asked otherwise.
Plan ordered beats, semantic components, primitives, then editable layers,
elements, channels, and keyframes.
Use component-safe contracts for prompt bars, cards, panels, and input fields.
Use SpeedyGraph timing for cinematic motion.
Use official ReFusion effects only when needed.
Do not use executable code, Markdown, comments, URLs, JSX, CSS, React,
Remotion code, GSAP, or imports.
```
