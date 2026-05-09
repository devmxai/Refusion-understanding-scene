# Motion Recipe Library v2

Professional scenes must use tokenized motion recipes from registry, not ad hoc
opacity-only channels.

## Recipe Families

- Entrance: slide, scale, bounce, rotate, blur, morph, typewriter, stamp.
- Exit: directional slide out, push back, scale out, dissolve.
- Group: cascade variants and mirrored entry.
- Attention: pulse, pointing emphasis, underline sweep.

## Minimum Variety Rule

For sibling cards in one beat:

- At most 60% can share the same recipe.
- Entrance and exit cannot be identical for all siblings.
- At least one supporting element must use non-fade motion.

## Required Token Use

- `motionRecipe`: `$motion.*`
- `componentChoreography.enterRecipe`: `$motion.*`
- `componentChoreography.exitRecipe`: `$motion.*`

Do not author raw bezier strings in brief-level output; rely on recipe tokens.
