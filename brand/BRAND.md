# blipbox identity

blipbox is the open-source software factory of nimbous. This is the working
identity guide: what the name means, how the brand looks and sounds, and the
rules that let agents and people produce on-brand output without asking.

The code in this repository is MIT-licensed. The blipbox name, the wordmark,
and the cube mark are not: they belong to Nimbous. You may use them to refer to
blipbox and its projects. You may not use them as your own brand, in a way that
suggests endorsement, or on a modified version of the mark. See
[brand/LICENSE.md](LICENSE.md).

## The idea

The name reads literally.

- A **blip** is a small, sharp signal. In blipbox, a blip is a release: a
  tagged version with a changelog, small enough to read in one sitting.
- A **box** is a self-contained thing that ships. In blipbox, a box is a
  project: one job, done completely, MIT-licensed.

The mark already tells this story: a shipping-crate cube with yellow signal
pixels on a red face. The whole identity is derived from it.

## Positioning

**One line.** Open source, built in blips.

**Two lines.** blipbox is an open-source software factory: agents draft, an
engineer reads every change and signs the release. Each release is a blip,
kept small enough to read in one sitting.

**Paragraph.** blipbox is an initiative by nimbous, an engineering consultancy
that has solved hard machine learning, AI, infrastructure, and data
engineering problems for business customers since 2018. blipbox is where that
experience goes into open source, and where we learn, in public, how an
agentic software factory should work. First out of the box: sluggi, a Python
library and CLI for clean, URL-safe slugs.

**Relationship to nimbous.** Say "an initiative by nimbous". Never "a division
of" or "a product of".

## Where blipbox lives

- Web: blipbox.io (blip-box.com redirects there)
- Code: github.com/blip-box
- X: x.com/blip_box, handle `@blip_box`
- Packages: pypi.org/project/sluggi

## Claims

A tagline may have an adjective. A claim may not. A claim is a sentence about
the product or the process, and it is either measured, a promise with a date,
or not made.

- **Claim now, because it is true and visible.** Agents draft in pull requests.
  An engineer reads every change before it merges; every change arrives as a
  pull request with CI passing, and the branch rules are public. Every box is MIT. Every release is signed with
  Sigstore and carries the engineer's name in the changelog.
- **Claim once measured.** Share of lines drafted by agents. Spec-to-release
  time. Review hours per release. Defects after release. Publish the numbers
  first, then the sentence.
- **Never claim.** Autonomous. Self-driving. 10x. AI-powered. Replaces
  developers. Enterprise-grade. Any speed word without the benchmark beside it.

Product facts follow the same rule: "20,000 strings in 0.74 seconds on the
included benchmark", not "blazing fast"; "Latin, Greek, and Cyrillic", not
"dozens of scripts".

## Vocabulary

| Say | Not |
| --- | --- |
| blipbox (one word, always lowercase, even at the start of a sentence) | BlipBox, Blip Box, Blipbox |
| a blip (a release) | a drop, a launch, v2.0-final-final |
| a box (a project) | a repo, a package, a product |
| the belt (the pipeline from intake to release) | the SDLC, the workflow |
| the factory (the agentic system plus the people who run it) | the platform, the AI |
| agents draft, an engineer signs | AI-powered, autonomous, human-in-the-loop |

## Voice

Plain, confident, specific, occasionally playful. Engineer to engineer.

1. **Say what it does.** "Turns any text into a clean, URL-safe slug." Not
   "a next-generation slugification solution".
2. **Numbers over adjectives.** "20,000 strings in 0.74 seconds" beats
   "blazing fast". If there is no number, use a concrete example.
3. **Agents are tools, not colleagues.** They draft, generate, and run. They
   do not think, believe, or decide. People review, decide, and sign off.
4. **Short sentences. Active voice. Sentence case.** No exclamation marks.
   No emoji in copy. Emoji in README feature lists are tolerated, not loved.
5. **Honest about state.** "More boxes are on the belt" is fine. A grid of
   fake projects is not.

## Color

Sampled from the mark. Four colors do all the work.

| Token | Hex | Role |
| --- | --- | --- |
| paper | `#FCFBF9` | The page. A warm white, not a cream. |
| ink | `#0D0D0B` | Text, rules, outlines, the primary button. |
| signal red | `#EF2720` | A surface: the box face, the hero mark, the "Ship" step. Text on it only at display sizes. |
| blip yellow | `#FFCB25` | A signal: pixels, bullets, focus rings, underlines on hover. |

Supporting neutrals: paper-2 `#F3F1EC` (sunken surfaces, inline code),
ink-2 `#4A4744` (secondary text), ink-3 `#706A64` (faint text, the lightest
grey that still passes 4.5:1 on paper),
line `rgba(13,13,11,.14)` (the only hairline, used inside lists).

**Red is a surface, yellow is a signal.** Red appears as large blocks. Yellow
never appears larger than a pixel unit except inside the mark itself. Do not
put body text on red. Do not use yellow as a text color.

Deep red `#C81C16` carries text at body sizes, such as the primary button on
hover, because the signal red only reaches 4.1:1 against paper.

Dark theme: paper `#131211`, ink `#F4F2EE`, ink-3 `#8F8982`, red `#F5342C`,
yellow unchanged.
The mark keeps its own black outline in both themes.

## Type

One family, two jobs. **Archivo** (variable, from Google Fonts) with the width
axis doing the work:

- Headlines: weight 800, width 112%, letter-spacing -0.035em, line-height 0.95.
- Body: weight 400, width 100%, 17px, line-height 1.55, max 65 characters.
- Small labels: weight 600, width 90%, sentence case. Never all caps.

**Azeret Mono** for code, install commands, and slug output. Never for labels
or eyebrows.

Scale (rem): 0.8125, 0.9375, 1.0625, 1.25, 1.5625, 2, 2.625, and a display
size of `clamp(2.9rem, 1.2rem + 6.6vw, 6.6rem)`.

## Structure: the box in three numbers

Everything on the page is built from three numbers taken from the mark:

- **Stroke: 3px.** Section rules, borders, and the belt line. No hairlines
  except inside lists.
- **Radius: 12px** (20px for a whole box). Corners are rounded like the
  mark's pixels, never square, never pill-shaped.
- **Pixel: 8px.** The spacing grid, the size of a bullet, the unit for
  emitted blips.

A border on the page means "this is a shipped box". Nothing else gets a
border, and nothing gets a shadow.

## The mark

`brand/logo.svg` is the static mark, `brand/logo-animated.svg` emits blips.
Both are drawn on a 1024 grid with a 30-unit outline, so the outline is
about 3% of the mark's width at any size. The cube is an oblique
projection: the front face is a 426-unit square and both the top and the
right face extend along the same depth vector, 140 right and 96 up. Keep
that single vector if you ever redraw it; two different depth directions
is what makes a box stop looking like a cube.

- Clear space: one pixel unit (1/16 of the mark's width) on all sides.
- Minimum size: 24px. Below that use the favicon variant with the 34-unit
  outline (the nav and footer marks in `index.html`).
- Backgrounds: paper, ink, or a photograph. Never on red or yellow.
- The wordmark is the word "blipbox" set in Archivo 800 at width 112%,
  letter-spacing -0.02em, placed to the right of the mark with a gap of
  one third of the mark's height, baseline-aligned to the mark's front face.

Do not recolor, outline, rotate more than the hover tilt, add a gradient, or
redraw the glyph on the face.

## Project marks

Every box gets a 5×5 pixel sprite generated from its name, rendered as blip
yellow on signal red. The reference implementation is `spriteCells` in
`assets/main.js`:

1. FNV-1a (32-bit) hash of the trimmed, lowercased name.
2. Seed an xorshift32 generator with the hash.
3. Take 32-bit words until one lights between 9 and 16 of the 25 cells,
   where the left three columns come from the bits (row-major, 3 per row)
   and columns 4 and 5 mirror columns 2 and 1.
4. Draw each lit cell as a rounded square (inset 0.06, radius 0.16 on a
   unit grid).

The sprite is deterministic, so a README, a PyPI page, and the website all
show the same mark without storing an image.

## Motion

One moment, always the mark. The hero cube lands on page load (a 18px rise
with a slight overshoot, 0.8s) and then emits blips: small yellow squares
that rise out of the top face and fade, one every 1.5s, three sizes.
On hover the whole cube tilts 4° and lifts 8px.

Nothing else moves on its own. Hover states change a color or an underline.
`prefers-reduced-motion` stops the blips, the landing, and the tilt.

## Files

- `brand/tokens.css` — all tokens, light and dark.
- `brand/logo.svg` — static mark.
- `brand/logo-animated.svg` — mark with emitted blips, safe to use in an `<img>`.
- `assets/favicon.svg` — the mark, for browser tabs.
- `brand/social-card.html` — the 1200×630 Open Graph card; `scripts/render-og.py`
  renders it to `assets/og.png`. Re-render after any change to the mark or tagline.
- `assets/main.js` — project sprite generator and the sluggi demo.
- `.local/blipbox-logo.png` — the original raster draft the SVG was traced
  from. `.local/` is not in the repository.
