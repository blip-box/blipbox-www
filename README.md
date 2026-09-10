# blipbox-www

The home page and identity for **blipbox**, the open-source software factory
of [nimbous](https://nimbous.co). Live at blipbox.io (blip-box.com redirects).

Static HTML, CSS, and a little JavaScript. No build step, no framework, so an
agent or a person can change one file and ship.

## Layout

```
index.html            the page
assets/site.css       page styles
assets/main.js        project sprites and the sluggi demo
assets/favicon.svg
assets/og.png         social preview card, 1200x630
brand/BRAND.md        identity guide: name, claims, voice, color, type, motion, sprites
brand/LICENSE.md      what the MIT license does not cover: the name and the mark
brand/tokens.css      design tokens (light and dark)
brand/logo.svg        static mark
brand/logo-animated.svg
brand/social-card.html    source of the social card
scripts/build-single.py   bundles the page into dist/ as one file
scripts/render-og.py      renders the social card with headless Chrome
scripts/md-to-page.py     renders a Markdown doc as a page in the brand style
.agents/skills/       agent skills installed for this repo (ui-skills-root), with skills-lock.json
CNAME, .nojekyll      GitHub Pages: custom domain, serve files as they are
LICENSE               MIT, for the code
.local/               not in git: the raster logo draft and local notes
```

## Preview

```bash
python3 -m http.server 8080
```

Then open http://localhost:8080.

## Single-file build

```bash
python3 scripts/build-single.py
```

Writes `dist/index.html` (a self-contained page with CSS, JS, and the mark
inlined) and `dist/artifact.html` (the same page as a body fragment, for
hosts that supply their own document shell).

## Social card

```bash
python3 scripts/render-og.py
```

Renders `brand/social-card.html` to `assets/og.png`. Needs Chrome or Chromium
on the machine. Run it again whenever the mark or the tagline changes.

## Deploy

Any static host works. Two reasonable options:

- **GitHub Pages** under the `blip-box` organization: push this repo as
  `blip-box/blipbox-www`, enable Pages from the `main` branch root, add a
  `CNAME` file containing `blipbox.io`, and point the domain's DNS at GitHub
  Pages. Redirect blip-box.com at the registrar.
- **Cloudflare Pages** with the repo root as the output directory.


## Analytics

Two trackers, both declared in `index.html`. Cloudflare Web Analytics is
cookieless and always on. Google Analytics loads with every storage type
denied and only sets cookies after a visitor accepts the small opt-in that
appears once they scroll or click a button; the answer is kept in local
storage.

## License

Code is MIT, see [LICENSE](LICENSE). The blipbox name, wordmark, and cube mark
belong to Nimbous and are not covered by it, see [brand/LICENSE.md](brand/LICENSE.md).

## Next

- A `projects.json` the factory can append to, so new boxes appear on the
  page without editing HTML.
- Sprites in the sluggi README, generated with the same algorithm.
