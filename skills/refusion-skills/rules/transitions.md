# Transition Authoring Rule

Use this rule when a prompt asks for a transition between two clips, scenes, or
Scene Clip containers.

## Boundary Truth

A transition is a boundary effect between an outgoing source and an incoming
source. It is not an independent fake clip.

For camera, zoom, blur, push, whip, flash, or matte transitions, always reason
from the seam:

- outgoing source A contributes the playing end of A before the seam;
- incoming source B contributes the playing beginning of B after the seam;
- exact boundary frames are still useful as AI seeds and non-live fallbacks, but
  a live-video transition must not replace playback with frozen thumbnails;
- progress is normalized over the transition window;
- the seam is normally at `0.5` unless an explicit alignment says otherwise;
- all motion curves are evaluated from this one progress value.

## Zoom In Camera Contract

For a professional zoom-in camera transition:

- keep the visual action fast, centered, and seam-aware;
- outgoing A should accelerate into the cut;
- incoming B should continue the perceived camera motion and settle after the
  cut;
- avoid slow dissolves unless the user explicitly asks for a dissolve;
- hide the cut with peak velocity, motion blur, and a small deterministic
  impact shake;
- use live-surface zoom/blur/impact cues for preview. Do not render the whole
  transition as static first/last-frame images.

Baseline normalized recipe:

```text
duration: 4 seconds by default, 1.2s..5.0s allowed
seam: 0.5
outgoing scale: 1.0 -> 3.0 by seam, ease-in
incoming scale: 0.28 -> 1.0 after seam, ease-out
opacity handoff: 0.42..0.58
incoming lead: none as frozen pre-roll; B becomes live at the seam
motion blur peak: 18
impact shake: 5
bridge darkness: 0.12
```

## Professional Timing Rules

- Do not show a transition before both boundary sources are known.
- Do not use the first frame of source A for an outgoing seam preview; use the
  last visible frame of A.
- Do not use a generic thumbnail as the final transition source if a
  boundary-frame source is available.
- Do not use boundary-frame stills for Zoom In Camera when live video playback
  is available.
- Do not let the incoming layer appear as a rounded card unless the prompt asks
  for a card transition.
- Motion blur and shake must be deterministic so preview and export can match.
  The current app preview uses live-surface blur plus speed-line cues; true
  directional temporal blur belongs in the future native renderer/export path.

## Current Engine Support

The current ReFusion engine supports a preview-side `Zoom In Camera` preset that
animates the native video preview surface over a 4s two-sided window, avoids
generic thumbnail fallback, and uses exact boundary-frame extraction only for
AI seeds or non-live fallback transitions.

Export parity for this preset is still a required future step. Until export
parity is documented as complete, do not promise that every transition effect
exports exactly like preview.
