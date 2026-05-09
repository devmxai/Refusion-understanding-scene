# Refusion Skills

Status: official agent skill pack for ReFusion scene authoring.

This repository teaches external agents how to write professional, editable
ReFusion motion scenes. It is intentionally structured like a skill pack:

```text
skills/refusion-skills/
├── SKILL.md
├── rules/
│   ├── native-motion-scene-author.md
│   ├── native-scene-intelligence.md
│   ├── migration-v1-to-v2.md
│   ├── speedygraph.md
│   ├── effects-and-renderer.md
│   ├── modern-motion-design.md
│   ├── remotion-principles-for-refusion.md
│   ├── open-design-adaptation.md
│   ├── scene-program-json.md
│   ├── professional-timing-contract.md
│   ├── choreography.md
│   ├── composition-workspace.md
│   ├── transitions.md
│   ├── capability-registry.md
│   ├── tutorial-intake.md
│   ├── validation.md
│   ├── director-brief-authoring-v5.md
│   ├── director-plan-validator-v5.md
│   ├── motion-recipe-library-v2.md
│   ├── brand-aware-motion-v5.md
│   ├── brand-icon-usage-v5.md
│   ├── brand-asset-legal-fallback-v5.md
│   ├── component-internal-choreography-v5.md
│   ├── inter-component-choreography-v5.md
│   ├── background-semantic-pairing-v5.md
│   ├── text-layout-v5.md
│   ├── scene-composition-v5.md
│   ├── rhythm-density-principles-v5.md
│   ├── professional-taste-checklist-v5.md
│   └── repair-loop-examples-v5.md
└── examples/
    ├── basic-typewriter-intro.json
    ├── premium-app-promo-scene.json
    ├── revival-premium-app-demo-60s.json
    └── v5/
        ├── README.md
        ├── good/ (10 director-brief examples)
        └── bad/ (10 rejected examples)
scripts/
└── validate_scene_program.py
```

Give `skills/refusion-skills/SKILL.md` to any coding or design agent before
asking it to create a ReFusion scene. The skill then tells the agent which rule
files to load for the task.

If the agent cannot browse repository folders, cannot resolve relative links, or
says it cannot access `rules/`, give it this single file instead:

```text
REFUSION_SCENE_SKILL_FULL.md
```

That file contains the skill entry point, every rule file, and the example JSON
in one self-contained document.

Before giving a scene to the app, validate it locally:

```bash
python3 scripts/validate_scene_program.py skills/refusion-skills/examples/revival-premium-app-demo-60s.json
```

The most common app rejection is incomplete paste: the text starts with `{` but
does not include the final `}`. The validator catches that before a user sees
`Scene program rejected`.

Canonical GitHub paths:

```text
Repo:
https://github.com/devmxai/refusion-skills

Skill entry:
skills/refusion-skills/SKILL.md

All-in-one fallback:
REFUSION_SCENE_SKILL_FULL.md

Rules:
skills/refusion-skills/rules/scene-program-json.md
skills/refusion-skills/rules/professional-timing-contract.md
skills/refusion-skills/rules/choreography.md
skills/refusion-skills/rules/composition-workspace.md
skills/refusion-skills/rules/transitions.md
skills/refusion-skills/rules/capability-registry.md
skills/refusion-skills/rules/tutorial-intake.md
skills/refusion-skills/rules/validation.md
skills/refusion-skills/rules/director-brief-authoring-v5.md
skills/refusion-skills/rules/director-plan-validator-v5.md
skills/refusion-skills/rules/motion-recipe-library-v2.md
skills/refusion-skills/rules/brand-aware-motion-v5.md
skills/refusion-skills/rules/brand-icon-usage-v5.md
skills/refusion-skills/rules/brand-asset-legal-fallback-v5.md
skills/refusion-skills/rules/component-internal-choreography-v5.md
skills/refusion-skills/rules/inter-component-choreography-v5.md
skills/refusion-skills/rules/background-semantic-pairing-v5.md
skills/refusion-skills/rules/text-layout-v5.md
skills/refusion-skills/rules/scene-composition-v5.md
skills/refusion-skills/rules/rhythm-density-principles-v5.md
skills/refusion-skills/rules/professional-taste-checklist-v5.md
skills/refusion-skills/rules/repair-loop-examples-v5.md
skills/refusion-skills/examples/v5/README.md
scripts/validate_scene_program.py
```

Direct browser links:

- [Skill entry](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/SKILL.md)
- [All-in-one fallback](https://github.com/devmxai/refusion-skills/blob/main/REFUSION_SCENE_SKILL_FULL.md)
- [Native Motion Scene Author](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/native-motion-scene-author.md)
- [Native Scene Intelligence](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/native-scene-intelligence.md)
- [Scene Migration v1 To v2](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/migration-v1-to-v2.md)
- [SpeedyGraph](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/speedygraph.md)
- [Effects And Renderer](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/effects-and-renderer.md)
- [Modern Motion Design](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/modern-motion-design.md)
- [Remotion Principles For ReFusion](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/remotion-principles-for-refusion.md)
- [Open Design Adaptation](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/open-design-adaptation.md)
- [Scene Program JSON](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/scene-program-json.md)
- [Professional Timing Contract](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/professional-timing-contract.md)
- [Choreography](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/choreography.md)
- [Composition Workspace](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/composition-workspace.md)
- [Transitions](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/transitions.md)
- [Capability Registry](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/capability-registry.md)
- [Tutorial Intake](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/tutorial-intake.md)
- [Validation](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/validation.md)
- [Director Brief Authoring v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/director-brief-authoring-v5.md)
- [Director Plan Validator v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/director-plan-validator-v5.md)
- [Motion Recipe Library v2](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/motion-recipe-library-v2.md)
- [Brand-Aware Motion v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/brand-aware-motion-v5.md)
- [Brand Icon Usage v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/brand-icon-usage-v5.md)
- [Brand Asset Legal Fallback v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/brand-asset-legal-fallback-v5.md)
- [Component Internal Choreography v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/component-internal-choreography-v5.md)
- [Inter-Component Choreography v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/inter-component-choreography-v5.md)
- [Background Semantic Pairing v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/background-semantic-pairing-v5.md)
- [Text Layout v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/text-layout-v5.md)
- [Scene Composition v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/scene-composition-v5.md)
- [Rhythm and Density Principles v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/rhythm-density-principles-v5.md)
- [Professional Taste Checklist v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/professional-taste-checklist-v5.md)
- [Repair Loop Examples v5](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/rules/repair-loop-examples-v5.md)
- [Revival Premium App Demo 60s](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/examples/revival-premium-app-demo-60s.json)
- [VERSION 5 Examples Catalog](https://github.com/devmxai/refusion-skills/blob/main/skills/refusion-skills/examples/v5/README.md)
- [Scene Program Validator](https://github.com/devmxai/refusion-skills/blob/main/scripts/validate_scene_program.py)

## Mission

The target is not merely valid JSON. The target is professional motion:

- ReFusion-native scenes, not HTML artifacts;
- real editable layers, elements, channels, and keyframes;
- DirectorPlan-first creative and motion direction;
- Native Scene Intelligence contracts for prompt bars, cards, text fit, Beat
  Grammar, and Visual Closure preparation;
- center-origin coordinate canon with explicit top-left conversion before final
  authoring;
- shared evaluated-frame truth expectations so QA and preview read the same
  geometry;
- SpeedyGraph / Bezier timing truth;
- official editable effects only;
- deterministic timing;
- readable holds;
- no random overlap;
- no early cuts;
- no hidden UI-only motion;
- Scene Program output that can be inspected and edited after import.

This repository intentionally borrows useful discipline from Open Design and
Remotion while excluding their execution surfaces. Open Design contributes
design brief, taste, critique, and anti-slop thinking. Remotion contributes
composition, sequence, frame-accurate timing, and reusable-scene thinking.
Neither HTML/CSS/JS nor React/Remotion code is valid ReFusion output.

## Mandatory Maintenance Rule

Every time the ReFusion engine gains a new capability, effect, timing rule,
validation rule, export behavior, or known limitation, this repository must be
updated in the same checkpoint family.

The app engine and this skill pack must not drift.

If the engine supports a feature but the skill does not document it, agents will
produce weaker scenes. If the skill claims a feature that the engine does not
support, generated scenes will fail or look fake.

## Repository Rename

This repository is being converted from `Refusion-understanding-scene` into the
broader `refusion-skills` concept. The content now represents the permanent
skill source for ReFusion scene understanding, timing, choreography, and future
tutorial-derived capabilities.
