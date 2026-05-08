# Scene Migration v1 To v2

Use this rule when upgrading legacy direct SceneProgram authoring to the
VERSION 2 semantic-authoring path.

## Goal

Keep runtime compatibility while moving authoring quality from "JSON-valid" to
"component-safe + visually safe + deterministic".

## Keep As-Is

- Existing `refusion.scene-program/v1` scenes remain importable.
- Existing layer/element/channel runtime paths remain native.
- Existing SpeedyGraph/easing semantics remain unchanged.

## Migrate In Authoring Layer

Move agent-authored scenes to semantic blueprint intent first:

1. declare components from the registry;
2. bind children by parent/slot contracts;
3. enforce bounded `textFrame` for bounded UI text;
4. bind important motion to beats with enter/hold/exit;
5. compile timing through SpeedyGraph truth compiler;
6. run visual QA probe checks;
7. run deterministic compile checks.

## Minimum Migration Checklist

- no loose text over card/input components;
- no bounded text without finite `textFrame` dimensions;
- no unsupported component ids or variants;
- no unowned overlap across cards/panels;
- no important motion outside beat ownership;
- no SpeedyGraph bypass;
- no non-deterministic lowering output for same blueprint input.

## Diagnostics Expected

```text
TF_SCENE_BLUEPRINT_COMPILER_PROOF
TF_SCENE_TOKEN_REGISTRY_PROOF
TF_SCENE_COMPONENT_REGISTRY_PROOF
TF_SCENE_TEXT_GEOMETRY_PROOF
TF_SCENE_LAYOUT_SOLVER_PROOF
TF_SCENE_BEAT_GRAMMAR_PROOF
TF_SCENE_DETERMINISM_PROOF
TF_SCENE_VISUAL_FRAME_QA_PROOF
TF_SCENE_REPAIR_LOOP_PROOF
```

## Stop Conditions

- Do not switch to HTML/CSS/JS as a migration shortcut.
- Do not rewrite runtime engine contracts.
- Do not claim migrated success if visual QA still reports overflow/clipping.
