# Refusion Skills

Status: official agent skill pack for ReFusion scene authoring.

This repository teaches external agents how to write professional, editable
ReFusion motion scenes. It is intentionally structured like a skill pack:

```text
skills/refusion-skills/
├── SKILL.md
├── rules/
│   ├── scene-program-json.md
│   ├── professional-timing-contract.md
│   ├── choreography.md
│   ├── capability-registry.md
│   ├── tutorial-intake.md
│   └── validation.md
└── examples/
    └── basic-typewriter-intro.json
```

Give `skills/refusion-skills/SKILL.md` to any coding or design agent before
asking it to create a ReFusion scene. The skill then tells the agent which rule
files to load for the task.

## Mission

The target is not merely valid JSON. The target is professional motion:

- real editable layers, elements, channels, and keyframes;
- deterministic timing;
- readable holds;
- no random overlap;
- no early cuts;
- no hidden UI-only motion;
- Scene Program output that can be inspected and edited after import.

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
