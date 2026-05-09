# Scene Composition v5

Use composition intents and safe areas instead of loose coordinates.

## Composition Intent Tokens

- `$composition.heroPrompt`
- `$composition.featureGrid`
- `$composition.testimonialWall`
- `$composition.splitBeforeAfter`

## Rules

1. Solve layout with safe area and aspect-aware grid.
2. Keep card groups balanced in available canvas.
3. Maintain optical center for hero icon and title clusters.
4. Reject placements outside safe area.

## Aspect Guidance

- 9:16: prioritize vertical rhythm.
- 16:9: widen card groups and preserve breathing room.
- 1:1: avoid edge crowding and keep central anchor strong.
