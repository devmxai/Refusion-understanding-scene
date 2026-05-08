# Native Motion Scene Author

Use this rule when an agent must create a professional ReFusion scene from a
prompt.

## Core Identity

ReFusion is a native editable video/motion scene engine, not an HTML design
surface.

Think like:

```text
After Effects / Alight Motion / Premiere-style editable composition
```

Do not think like:

```text
web page -> HTML artifact -> rendered iframe
```

## Final Output

For scene creation, output a single complete JSON object:

```json
{
  "directorPlan": {},
  "sceneProgram": {}
}
```

Do not output:

- HTML
- CSS
- JavaScript
- JSX
- React / Remotion code
- GSAP
- shader source
- remote imports
- Markdown wrapped around the JSON
- rendered video as the source of truth

For long product demos, do not let the platform truncate the response. A valid
ReFusion scene must be complete from the first `{` to the final `}`. If you can
write files, create a `.json` artifact and validate it with
`scripts/validate_scene_program.py` before delivery.

## Four Internal Roles

If you are one agent, run these roles internally. If a system supports multiple
agents, assign one role per agent.

### 1. Creative Director

Define:

- scene thesis;
- audience and format;
- mood and visual language;
- hierarchy of attention;
- semantic components;
- what must not happen.

Output should sound like:

```text
A premium vertical app-promo scene where a dark product card floats into view,
the headline types on, and the CTA settles with one controlled pulse.
```

Not:

```text
A modern webpage with cards and gradients.
```

### 2. Motion Director

Define:

- beats;
- component lifetimes;
- motion primitives;
- overlaps and handoffs;
- readable holds;
- timing style.

Good beat pattern:

```text
0-420ms      establish background
220-980ms    hero card enters
860-1700ms   title reveals
1580-2200ms  CTA settles
2200-3200ms  readable hold
```

### 3. Technical Scene Writer

Write:

- `directorPlan`;
- `sceneProgram`;
- shape/text/image/video layers;
- elements;
- channels;
- keyframes;
- SpeedyGraph timing;
- official effects.

Every visible motion must be editable.

### 4. QA Critic

Reject and revise if:

- JSON is incomplete or does not end with the final root `}`;
- DirectorPlan and SceneProgram disagree;
- important text has no readable hold;
- motion feels random;
- keyframes are hidden or non-editable;
- effects are unsupported;
- timing is accidentally linear;
- scene depends on HTML/CSS/JS behavior.

## Translation Mental Model

| Web/Open Design idea | ReFusion-native equivalent |
|---|---|
| page | composition/canvas |
| section | beat |
| div/card | shape/text/image/video layer |
| CSS token | ReFusion design token |
| CSS animation | channel/keyframes/SpeedyGraph |
| HTML artifact | DirectorPlan + SceneProgram JSON |
| critique | DirectorPlan/SceneProgram QA |
| template | motion recipe |

## Professional Bar

The result must feel inspectable by a motion designer:

- clear component names;
- stable IDs;
- intentional timing;
- few strong motions;
- readable final frame;
- editable layers;
- no black-box runtime tricks.
