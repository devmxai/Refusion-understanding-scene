# Native Scene Intelligence

Use this rule when authoring scenes that must feel deliberately designed,
component-safe, and reliable on first import.

## Principle

ReFusion scene authoring uses:

```text
Closed Vocabulary + Component Contracts + Beat Grammar + Visual Closure Prep
```

Runtime quality gate in VERSION 4:

```text
QA truth == Preview truth == Apply gate truth
```

This is implemented through a shared evaluated-frame contract. Agent-authored
scenes should assume that containment, overlap, safe-area, and continuity are
verified from the same evaluated geometry that preview renders.

The agent should not guess raw layout numbers when a known component contract
exists. Use semantic vocabulary during planning, then lower it into valid native
Scene Program JSON with concrete editable values.

Important distinction:

- agent-facing blueprints should prefer closed vocabulary tokens;
- lowered `refusion.scene-program/v1` may contain resolved native numbers,
  colors, and keyframes;
- do not require every lowered Scene Program value to remain a token.

## Coordinate Canon (Center-Origin V1)

Canonical scene space:

```text
origin: canvas center
+X: right
+Y: down
unit: design pixels
position: element center by default
```

For a 1080x1920 canvas:

```text
left  = -540
right = 540
top   = -960
bottom= 960
```

Convert top-left specs to center-origin before authoring:

```text
centerX = left + width/2 - canvasWidth/2
centerY = top + height/2 - canvasHeight/2
```

Example:

```text
top-left rect: left=120, top=280, width=840, height=128
canvas: 1080x1920
=> centerX = 120 + 420 - 540 = 0
=> centerY = 280 + 64 - 960 = -616
```

Never output top-left coordinates directly unless you explicitly converted.

## Closed Vocabulary For Agent-Facing Plans

Prefer these references in planning notes, DirectorPlan labels, component roles,
and internal reasoning before lowering to Scene Program values.

### Components

```text
$component.PromptInputBar
$component.AppIconIntro
$component.FeatureCard
$component.ResultCard
$component.MotionTextBlock
$component.IconButton
$component.DashboardPanel
$component.TimelineStrip
$component.AudioWaveform
$component.ColorGradePanel
```

### Spacing

```text
$spacing.xs   compact internal gap
$spacing.sm   small grouped gap
$spacing.md   default component gap
$spacing.lg   safe readable padding
$spacing.xl   section spacing
$spacing.2xl  hero spacing
$spacing.3xl  scene spacing
```

### Typography

```text
$typography.caption
$typography.body
$typography.input
$typography.title
$typography.headline
$typography.hero
```

### Duration

```text
$duration.instant
$duration.fast
$duration.medium
$duration.slow
$duration.deliberate
```

### Easing / SpeedyGraph

```text
$easing.linear
$easing.easyEase
$easing.fastSlow
$easing.slowFast
$easing.slowFastSlow
$easing.snappy
$easing.expressive
```

Lower easing to supported Scene Program timing names such as `linear`,
`easyEase`, `fastSlow`, `slowFast`, and `slowFastSlow`.

### Motion

```text
$motion.softFadeUp
$motion.scaleFromOrigin
$motion.morphFromIcon
$motion.typewriterFixedFrame
$motion.cardStackIn
$motion.sendPressResolve
```

### Beats

```text
$beat.intro
$beat.prompt
$beat.feature
$beat.proof
$beat.outro
```

## PromptInputBar Contract

Use `PromptInputBar` whenever the scene asks for a chatbot text input, prompt
field, search bar, compose box, or command input.

Required pieces:

```text
prompt-shell   shape container
prompt-text    text child in primary/content slot
send-button    trailing accessory shape
send-icon      trailing accessory icon
```

The shell must declare:

```json
{
  "layoutRole": "container",
  "layoutMode": "absolute",
  "contentInsets": { "left": 48, "right": 128, "top": 24, "bottom": 24 },
  "width": 860,
  "height": 112
}
```

The prompt text must declare:

```json
{
  "parentId": "prompt-shell",
  "layout": {
    "role": "content",
    "slot": "primaryText",
    "align": "centerLeft"
  },
  "textFrame": {
    "width": 640,
    "height": 54,
    "maxLines": 1,
    "overflow": "ellipsis",
    "fitPolicy": "shrinkToFit",
    "measure": "fullText"
  }
}
```

Rules:

- text belongs inside the shell content rect, not visually on top of it;
- reserve right-side space for the send button;
- use one full text element plus `typewriterProgress`;
- never create one text element per character;
- font size must be smaller than the text frame height;
- prompt text must complete early enough to leave a readable hold;
- send press should happen after the readable hold, not while the text is still
  typing;
- if the icon becomes the input bar, describe continuity as a handoff or morph.
  Do not claim true geometric morph if the authored channels only fade/scale.

## Executable Hierarchy Rule (HCT-Aware)

- `parentId` is allowed only when the target contract supports executable
  hierarchy (PromptInputBar, FeatureCard, FeedbackCard, and similar grouped
  components).
- Children must live inside real slots or content bounds, not free-floating
  visual placements.
- Child motion should inherit parent motion by hierarchy whenever possible.
- Do not author independent competing transforms for parent and child unless
  the beat explicitly requires a handoff.

If a component contract does not support executable hierarchy, fail closed:
author it as explicit independent elements with clear containment and timing.

## Component Good/Bad Patterns

### PromptInputBar

Good:

- one `prompt-shell` container;
- `prompt-text` bound to content slot + `textFrame`;
- trailing `send-button` and `send-icon` in accessory slot;
- typewriter uses `typewriterProgress` in fixed text frame.

Bad:

- text visually on top of a shell with no slot/textFrame;
- send icon not parented/related to send button;
- text font larger than frame height;
- per-character layers.

### FeatureCard

Good:

- card shell as parent container;
- title/body/icon each in explicit slots;
- card width/height chosen for readable hold and safe area;
- body max lines + overflow policy set.

Bad:

- card text positioned with free absolute values only;
- title/body overlap during hold frame;
- icon outside card bounds at any probe frame.

### FeedbackCard

Good:

- header row slot (platform icon + source label);
- content slot with bounded paragraph text;
- consistent insets and max text width.

Bad:

- body text crossing card edge;
- multiple label texts stacked in same position unintentionally;
- card grid extending beyond safe area.

## Beat Grammar

Every important visual action belongs to a beat.

Each major beat should have intent:

```text
enter -> hold -> exit/resolve
```

Example prompt scene:

```text
0-1200ms    establish icon
1200-2600ms icon handoff to prompt shell
2600-4700ms type prompt
4700-5600ms prompt readable hold
5600-7600ms send press and result resolve
7600-9200ms final readable hold
```

Rules:

- no important motion outside a beat;
- no random parallel motion;
- overlap requires explicit parallel or handoff intent;
- motion uses SpeedyGraph timing names, not silent linear timing;
- professional text reveals always leave readable hold.

## Visual Closure Preparation

Before returning JSON, run this mental preflight. It prepares the scene for the
future Visual Closure Loop and prevents known first-import failures.

### Layout Check

- Is every known component represented by a component contract?
- Does every child declare a real parent when the layout depends on a parent?
- Does text fit inside its container at the hold frame?
- Are safe areas respected?
- Are icon/accessory slots reserved?

### Text Fit Check

- Text frame width is wide enough for the full text or has `shrinkToFit`.
- `fontSize <= textFrame.height`.
- `maxLines` is explicit for prompt/search/input text.
- Typewriter reveals the full text inside a fixed frame.

### Timing Check

- Every keyframe is inside the owning layer duration.
- Reveal finishes before the hold.
- Final action resolves before the scene ends.
- There is no accidental same-property overlap.

### Continuity Check

- Handoffs name source and target components.
- Disappearing elements fade/scale as part of a beat.
- A component does not teleport without an intentional transition.

### Contrast Check

- Text has high contrast against its background during readable hold.
- Important text is not tiny, moving too quickly, or covered by effects.

## Structured Repair Codes

If reviewing or repairing a scene, use these failure codes:

```text
TEXT_OVERFLOW_RIGHT
TEXT_OVERFLOW_HEIGHT
MISSING_PARENT_SLOT
CARD_CHILD_FLOATING
UNSUPPORTED_ICON
UNSUPPORTED_COMPONENT
UNSUPPORTED_VARIANT
SAFE_AREA_VIOLATION
DUPLICATE_PROPERTY_CHANNEL
UNREADABLE_HOLD
UNFINISHED_BOUNDARY_MOTION
SPEEDYGRAPH_BYPASS
NON_DETERMINISTIC_COMPILATION
```

Repair scenes by changing component contracts, timing, and supported native
properties. Do not repair by switching to HTML/CSS/JS or by inventing effects.

### Structured Repair Example (EvaluatedFrameTruth)

Input error payload:

```json
{
  "code": "TEXT_OVERFLOW_RIGHT",
  "frameMs": 5050,
  "componentId": "prompt-shell",
  "elementId": "prompt-text",
  "measured": {
    "containerWidth": 640,
    "textWidth": 688,
    "overflowPx": 48
  },
  "suggestedAction": {
    "path": "properties.textFrame.fitPolicy",
    "value": "shrinkToFit"
  }
}
```

Repair action:

- keep the same component and beat;
- reduce text width pressure through `textFrame.width`, `maxLines: 1`, and
  `fitPolicy: "shrinkToFit"`;
- do not move text outside the shell or bypass the component.

## Deterministic Compile Rule

For semantic-blueprint authoring, keep this contract:

- same normalized semantic blueprint => same lowered SceneProgram hash;
- reject raw numeric authoring values by default in blueprint mode;
- allow raw values only with explicit `rawValueOverride` intent;
- lowered SceneProgram can contain resolved native numeric values.

Expected proof in diagnostics:

```text
TF_SCENE_DETERMINISM_PROOF
```

with `blueprintHash`, `sceneProgramHash`, `tokenResolutionHash`,
`rawValuesDetected`, `rawValueOverrides`, and `passed`.

## Migration Rule (v1 -> v2)

- Existing direct `refusion.scene-program/v1` JSON remains importable.
- Prefer new scenes as semantic blueprints that lower into native SceneProgram.
- Do not regress old scenes by removing compatibility paths.
- When migrating old scenes, keep timing/easing semantics and upgrade only
  structure: components, slots, textFrame, and beat ownership.

## Stop List

- Do not use raw loose coordinates for a prompt/search/input bar when
  `PromptInputBar` applies.
- Do not let text be larger than its field.
- Do not place input text on a separate visual layer with no parent/slot.
- Do not animate typing by replacing strings or creating per-character layers.
- Do not output token-only pseudo-scenes that the app cannot import.
- Do not claim Visual Closure Loop completion until rendered probes and
  structured repair payloads exist in the app.
- Do not use top-left coordinates directly in authored Scene Program values.
- Do not assume QA uses a different coordinate interpretation than preview.
