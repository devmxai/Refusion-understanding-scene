# Brand-Aware Motion v5

Brand category influences motion feel.

## Category Mapping

- AI / tech: snappy and precise.
- Productivity: clean and restrained.
- Social playful: bouncy and expressive.
- Premium media: deliberate and cinematic.

## Rules

1. If `brandToken` exists, map default recipe from category.
2. Avoid contradictory feel unless user explicitly asks.
3. Keep brand motion coherent across the same scene.
4. Do not override canonical brand color by default.

## Example

- `$brand.chatgpt` -> `$motion.brand.tech`
- `$brand.instagram` -> `$motion.brand.playful`
- `$brand.notion` -> `$motion.brand.minimal`
