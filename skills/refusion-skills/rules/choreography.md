# Choreography Rules

Use this rule when a scene must feel designed rather than randomly animated.

## Professional Beat Shape

Most compact scenes should follow:

```text
enter
-> reveal
-> readable hold
-> action / transformation
-> resolve / exit
```

Example:

```text
0-400ms      background enters
220-1000ms  prompt bar enters
1000-2200ms text types
2200-2600ms readable hold
2600-3000ms send press
3000-4200ms circle cover / next screen reveal
```

## No Random Simultaneous Motion

Do not animate many properties at once just because motion is possible.

Good:

- one main subject moves;
- supporting elements settle;
- text remains readable;
- next action begins after the viewer understands the current state.

Bad:

- opacity flickers;
- text moves while being typed without reason;
- scene transitions before current motion finishes;
- elements disappear because their layer duration ended early.

## Handoff Discipline

When one shape becomes another:

1. complete the first idea enough for the viewer to recognize it;
2. morph or move the leading object;
3. reveal the next content through that object;
4. hold the new state before the next action.

For matte/wipe style reveals, the text is normally already present but hidden by
a moving mask or covering shape. Do not simulate this with typewriter unless the
visual goal is keyboard typing.

## Readability

Text must contrast with its background during its readable window.

Avoid:

- white text on white background;
- black text on dark background;
- tiny text in fast motion;
- final titles that appear after the scene is already ending.

## Timing Taste

Practical defaults:

```text
small button press: 180-320ms
shape entrance: 500-900ms
text typewriter: 800-1600ms depending on length
text/label readable hold: 400-900ms
large scene transition: 700-1400ms
hero title reveal: 900-1800ms
```

## Layer Count

Prefer semantic layers:

- one background layer;
- one shell/container layer;
- one text layer per semantic text block;
- one icon/button layer group if needed;
- one transition mask/cover layer if needed.

Do not create one layer per character unless the engine specifically supports a
text range selector or the user asks for per-letter kinetic typography.
