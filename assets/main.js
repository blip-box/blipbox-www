/* blipbox site script: project sprites and the sluggi demo. No dependencies. */
(function () {
  "use strict";

  /* Project sprites --------------------------------------------------------
     Every blipbox project gets a 5x5 pixel mark generated from its name:
     FNV-1a hashes the lowercased name, an xorshift32 stream is seeded with it,
     and the first 32-bit word whose left 3 columns (mirrored to 5) light up
     between 9 and 16 of the 25 cells becomes the sprite. Deterministic, so
     any tool in the factory can reproduce it. */

  function fnv1a(str) {
    var h = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = Math.imul(h, 0x01000193) >>> 0;
    }
    return h >>> 0;
  }

  function xorshift32(seed) {
    var x = seed || 0x9e3779b9;
    return function () {
      x ^= x << 13; x >>>= 0;
      x ^= x >>> 17;
      x ^= x << 5;  x >>>= 0;
      return x;
    };
  }

  function spriteCells(name) {
    var next = xorshift32(fnv1a(name.trim().toLowerCase()));
    var cells = [];
    for (var attempt = 0; attempt < 64; attempt++) {
      var bits = next();
      cells = [];
      var lit = 0;
      for (var r = 0; r < 5; r++) {
        var row = [];
        for (var c = 0; c < 3; c++) {
          var on = (bits >>> (r * 3 + c)) & 1;
          row.push(on);
          lit += on * (c === 2 ? 1 : 2);
        }
        cells.push(row);
      }
      if (lit >= 9 && lit <= 16) break;
    }
    return cells;
  }

  function renderSprite(svg, name) {
    var cells = spriteCells(name);
    var ns = "http://www.w3.org/2000/svg";
    svg.setAttribute("viewBox", "-0.5 -0.5 6 6");
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var title = document.createElementNS(ns, "title");
    title.textContent = name + " mark";
    svg.appendChild(title);
    for (var r = 0; r < 5; r++) {
      for (var c = 0; c < 5; c++) {
        var src = c < 3 ? c : 4 - c;
        if (!cells[r][src]) continue;
        var rect = document.createElementNS(ns, "rect");
        rect.setAttribute("x", c + 0.06);
        rect.setAttribute("y", r + 0.06);
        rect.setAttribute("width", 0.88);
        rect.setAttribute("height", 0.88);
        rect.setAttribute("rx", 0.16);
        rect.setAttribute("fill", "#FFCB25");
        svg.appendChild(rect);
      }
    }
  }

  document.querySelectorAll("svg[data-sprite]").forEach(function (svg) {
    renderSprite(svg, svg.getAttribute("data-sprite"));
  });

  /* sluggi demo -------------------------------------------------------------
     An in-browser approximation of sluggi's default pipeline:
     normalize (NFKD, strip marks) -> transliterate -> lowercase ->
     extract words -> join with the separator. Emoji are dropped, as in
     sluggi's default (process_emoji=False). */

  var MAP = {
    "ı": "i", "ß": "ss", "æ": "ae", "ø": "o", "œ": "oe", "đ": "d", "ł": "l", "þ": "th", "ð": "d",
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "zh", "з": "z",
    "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
    "α": "a", "β": "b", "γ": "g", "δ": "d", "ε": "e", "ζ": "z", "η": "i", "θ": "th", "ι": "i",
    "κ": "k", "λ": "l", "μ": "m", "ν": "n", "ξ": "x", "ο": "o", "π": "p", "ρ": "r", "σ": "s",
    "ς": "s", "τ": "t", "υ": "y", "φ": "f", "χ": "ch", "ψ": "ps", "ω": "o"
  };

  function slugify(text, separator) {
    var t = text.normalize("NFKD").replace(/[̀-ͯ]/g, "").toLowerCase();
    var out = "";
    for (var i = 0; i < t.length; i++) {
      var ch = t[i];
      out += Object.prototype.hasOwnProperty.call(MAP, ch) ? MAP[ch] : ch;
    }
    var words = out.match(/[a-z0-9]+/g) || [];
    return words.join(separator || "-");
  }

  var input = document.getElementById("slug-in");
  var output = document.getElementById("slug-out");
  if (input && output) {
    var update = function () { output.textContent = slugify(input.value); };
    input.addEventListener("input", update);
    update();
  }

  window.blipbox = { slugify: slugify, spriteCells: spriteCells };
})();
