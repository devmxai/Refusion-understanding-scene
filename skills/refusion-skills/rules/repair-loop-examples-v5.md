# Visual Closure Repair Examples v5

These examples show the expected repair behavior.

## Example: Motion Variety Low

- Error: `MOTION_VARIETY_LOW`
- Suggested path: `components.cards.motionRecipe`
- Suggested alternatives:
  - `$motion.slideInFromLeft`
  - `$motion.slideInFromRight`
  - `$motion.scaleInBounce`
  - `$motion.rotateIn`

## Example: Mid-Phrase Text Cut

- Error: `BAD_PHRASE_CUT`
- Suggested path: `components.cardA.slots.body.textFrame.fitPolicy`
- Suggested value: `$textFit.shorten`

## Example: Optical Alignment

- Error: `ICON_OPTICAL_CENTER_OFF`
- Suggested path:
  `components.promptAppIcon.componentChoreography.opticalAlignment`
- Suggested value: `auto`
