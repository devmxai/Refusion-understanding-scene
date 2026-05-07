# Modern Motion Design Recipes

Use this rule when the user asks for a professional modern scene, ad, intro,
app promo, title card, social post, or motion graphic.

## Design First, Then Motion

Build the hero frame mentally before animating:

1. What should the viewer see at the strongest frame?
2. What is the main subject?
3. What is the text hierarchy?
4. What is the one accent move?
5. What needs a readable hold?

Then animate into that frame.

## Premium App Promo

Components:

- background canvas;
- phone/card/device-like shape;
- product area;
- headline;
- subtitle;
- CTA;
- accent shape or ring.

Motion:

- card enters with y + scale, `slowFastSlow`;
- headline reveals after card is understandable;
- CTA lands with `fastSlow`;
- final hold 700-1200ms;
- optional Motion Blur on fast card entrance.

## Social Ad Scene

Components:

- high-contrast background;
- product object or abstract hero shape;
- short headline;
- proof badge;
- CTA strip.

Motion:

- establish background;
- hero object enters first;
- headline follows;
- proof badge snaps with `whip`;
- CTA lands softly;
- final frame reads as a complete social poster.

## Kinetic Title

Components:

- oversized title;
- mask/reveal shape;
- accent line or trim path;
- optional secondary caption.

Motion:

- title uses word or letter range reveal when supported;
- mask/wipe uses one matte-like shape or mask element;
- accent line uses trimEnd when supported;
- avoid one layer per letter unless specifically requested.

## Prompt / AI Scene

Components:

- prompt shell;
- prompt text;
- send button;
- reveal shape or circle;
- result card.

Motion:

- shell enters;
- text uses one `typewriterProgress` channel;
- send button press uses scale with `whip`;
- reveal shape expands using `slowFastSlow`;
- result card holds.

## Spin / Rotation Scene

Components:

- source visual;
- optional mirrored fill;
- optional blur;
- target/final state.

Motion:

- rotate around visual center;
- use `slowFastSlow`;
- add Motion Tile before Motion Blur when blank corners are possible;
- do not let Motion Tile change the pivot;
- final state must settle.

## Anti-AI-Slop Rules

Avoid:

- generic purple-blue gradient;
- too many rounded cards;
- emoji as icons;
- random metrics;
- text with no readable hold;
- all layers animating at once;
- same easing on every object;
- decorative motion with no story purpose.

Use:

- one strong visual idea;
- restrained palette;
- stable geometry;
- intentional typography;
- controlled staggering;
- readable final frame.
