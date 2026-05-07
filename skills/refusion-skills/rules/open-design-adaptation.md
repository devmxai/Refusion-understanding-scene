# Open Design Adaptation

Use this rule when adapting Open Design skills, design briefs, visual systems,
or critique methods into ReFusion scenes.

## What To Borrow

Borrow:

- skill structure;
- design brief thinking;
- mood/density/palette/typography decisions;
- anti-AI-slop rules;
- design-system tokens;
- critique rubrics;
- layout-before-animation;
- progressive disclosure;
- template-as-recipe thinking.

## What Not To Borrow

Do not output:

- HTML artifacts;
- CSS;
- JavaScript;
- GSAP;
- iframe previews;
- web templates as final scenes;
- website sections as direct ReFusion structures.

## Translation Table

| Open Design | ReFusion |
|---|---|
| skill prompt | agent authoring rule |
| DESIGN.md | ReFusion design token guidance |
| section layout | beat/component recipe |
| card/div | shape/text/image/video layer |
| CSS animation | keyframes + SpeedyGraph |
| artifact | DirectorPlan + SceneProgram JSON |
| critique report | QA of DirectorPlan/SceneProgram |
| template | reusable motion recipe |

## Design Token Guidance

When a prompt gives brand/style information, resolve:

- canvas background;
- text primary/secondary;
- accent color;
- display/body/mono typography intent;
- density: compact, balanced, spacious;
- mood: editorial, cinematic, utility, brutalist, soft, premium, playful;
- constraints: no gradients, no stock images, no busy motion, etc.

Then express these as SceneProgram shape/text properties and motion decisions,
not CSS variables.

## Critique Criteria

Before returning a scene, review:

- philosophy consistency;
- hierarchy;
- detail execution;
- functionality/editability;
- innovation.

Translate critique into scene fixes:

- adjust shapes;
- adjust text size/position;
- adjust timing;
- add holds;
- reduce layer noise;
- improve SpeedyGraph;
- remove unsupported effects.

## Main Rule

Open Design improves taste. ReFusion contracts control execution.
