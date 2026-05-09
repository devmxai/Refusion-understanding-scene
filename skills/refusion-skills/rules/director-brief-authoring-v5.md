# Director Brief Authoring v5

This rule makes authoring Director-first. Agents must start with a Director
Brief, not a loose element list.

## Required Root Contract

```json
{
  "directorBrief": {
    "intent": "string",
    "audience": "string",
    "mood": "string",
    "primaryFocus": "string",
    "rhythm": "string",
    "aspect": "$canvas.vertical9x16",
    "durationIntent": "$duration.deliberate",
    "elements": []
  }
}
```

## Mandatory Fields

- `intent`: explicit business or storytelling goal.
- `audience`: who the scene is for.
- `mood`: professional mood token or approved phrase.
- `primaryFocus`: exactly one dominant focal target per beat.
- `rhythm`: human-readable pacing narrative.
- `aspect`: token, not raw ratio text.
- `durationIntent`: token, not raw milliseconds.
- `elements`: semantic blocks (`title`, `subtitle`, `featureCardGroup`, etc).

## Authoring Rules

1. Declare visual thesis first, then motion thesis.
2. Define hierarchy (`primary`, `secondary`, `supporting`).
3. Use tokens for motion, text fit, composition intent, and taste profile.
4. Never start from raw x/y numbers unless explicitly requested for debug.
5. For feature groups, include `primaryCardIndex`.
6. Prefer four-beat structure: intro, expand, hold, exit.

## Forbidden

- Raw element arrays as first-class authoring surface.
- Mixed coordinate systems in one brief.
- Multiple conflicting `primaryFocus` values in same beat.
- Brand name usage without registry token or fallback policy.
