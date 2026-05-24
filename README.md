# typstpy

## Introduction

typstpy is a python package for generating executable [typst](https://typst.app/docs/) codes.
This package is written primarily in functional programming paradigm with some OOP contents.
Each module in this package has greater than 90% unit test coverage.

This package provides interfaces which are as close as possible to typst's native functions.
Through typstpy and other data processing packages, you can generate data report instantly.

Repository on GitHub: [python-typst](https://github.com/beibingyangliuying/python-typst).
Homepage on PyPI: [python-typst](https://pypi.org/project/typstpy/).
Any contributions are welcome.

## Change logs

- _1.4.0-alpha.0_:
  - Improve internal series spread handling for single children.
  - Use explicit exceptions instead of assertions for public argument validation.
  - Fix `import_` without names and `show_(None, ...)` rendering.
  - Refactor: add `render_content()` to IR protocol, removing fragile `strip_brace` char slicing.
  - Refactor: extract `_make_where_func` / `_make_with_func` from `implement` decorator.
  - Clarify spread logic: split `_should_spread_single_child` into dedicated helpers.
  - Add missing `Raises:` sections to docstrings across std modules.
  - Migrate type annotations to Python 3.10+ union syntax (`X | None` etc.).
  - Add `UP` (pyupgrade) to ruff lint ruleset.
  - Add `call_` factory function to `customizations` module.
- _1.3.0_:
  - Support for typst version: 0.14.2.
- _1.2.1_:
  - Clear type annotations.
  - Improved support for the typst 0.13.1 version.
- _1.2.0_:
  - Support for typst version: 0.13.x.
  - Migrate `set_`, `show_` and `import_` to `typstpy.std` module.
- _1.1.1_:
  - Fix: Fix the behavior of `with_`.
- _1.1.0_: Provide `customizations` module to support custom functions.
- _1.0.4_: Implement package `subpar`.
- _1.0.3_:
  - Fix: Fix the behavior of `show_`.
  - Compatibility: The parameters' order of `show_` is flipped compared to previous version.
- _1.0.2_: Improved type annotations.
- _1.0.1_: Implement `set`, `show`, and `import`.
- _1.0.0_: Completed documentation and test cases in `layout`, `model`, `text` and `visualize` modules. Improved functionality.
- _1.0.0-beta.2_: Improved the implementation and documentation of functions in the `layout` module.
- _1.0.0-beta.1_: Completely reconstructed the underlying implementation.

## Installation

```bash
pip install typstpy
```

## How to customize?

typstpy provides the `customizations` module to support defining functions that are not yet supported in typstpy.
The examples are:

```python
>>> from typstpy.customizations import *
>>> pad = normal('pad')
>>> pad(
...     '[Hello, world!]',
...     left='4% + 0pt',
...     top='4% + 0pt',
...     right='4% + 0pt',
...     bottom='4% + 0pt',
... )
'#pad([Hello, world!], left: 4% + 0pt, top: 4% + 0pt, right: 4% + 0pt, bottom: 4% + 0pt)'
>>> pagebreak = normal('pagebreak')
>>> pagebreak(weak=True)
'#pagebreak(weak: true)'
>>> rgb = positional('rgb')
>>> color_lighten = instance('lighten')
>>> color_lighten(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).lighten(50%)'
>>> rgb = positional('rgb')
>>> rgb(255, 255, 255, '50%')
'#rgb(255, 255, 255, 50%)'
>>> table = post_series('table')
>>> table(
...     '[1]',
...     '[2]',
...     '[3]',
...     columns=['1fr', '2fr', '3fr'],
...     rows=['1fr', '2fr', '3fr'],
...     gutter=['1fr', '2fr', '3fr'],
...     column_gutter=['1fr', '2fr', '3fr'],
...     row_gutter=['1fr', '2fr', '3fr'],
...     fill='red',
...     align=['center', 'center', 'center'],
... )
'#table(columns: (1fr, 2fr, 3fr), rows: (1fr, 2fr, 3fr), gutter: (1fr, 2fr, 3fr), column-gutter: (1fr, 2fr, 3fr), row-gutter: (1fr, 2fr, 3fr), fill: red, align: (center, center, center), [1], [2], [3])'
>>> subpar_grid = pre_series('subpar.grid')
>>> subpar_grid(
...     '[]',
...     '[]',
...     columns=('1fr', '1fr'),
...     caption='[A figure composed of two sub figures.]',
...     label='<full>',
... )
'#subpar.grid([], [], columns: (1fr, 1fr), caption: [A figure composed of two sub figures.], label: <full>)'
```

<!-- typstpy-generated-start -->

## Current Supports

| Package's function name | Typst's function name | Documentation on typst | Version |
| --- | --- | --- | --- |
| std.align | align | [https://typst.app/docs/reference/layout/align/](https://typst.app/docs/reference/layout/align/) | 0.14.2 |
| std.bibliography | bibliography | [https://typst.app/docs/reference/model/bibliography/](https://typst.app/docs/reference/model/bibliography/) | 0.14.2 |
| std.block | block | [https://typst.app/docs/reference/layout/block/](https://typst.app/docs/reference/layout/block/) | 0.14.2 |
| std.box | box | [https://typst.app/docs/reference/layout/box/](https://typst.app/docs/reference/layout/box/) | 0.14.2 |
| std.bullet_list | list | [https://typst.app/docs/reference/model/list/](https://typst.app/docs/reference/model/list/) | 0.14.2 |
| std.bullet_list.item | list.item | [https://typst.app/docs/reference/model/list/#definitions-item](https://typst.app/docs/reference/model/list/#definitions-item) | 0.14.2 |
| std.circle | circle | [https://typst.app/docs/reference/visualize/circle/](https://typst.app/docs/reference/visualize/circle/) | 0.14.2 |
| std.cite | cite | [https://typst.app/docs/reference/model/cite/](https://typst.app/docs/reference/model/cite/) | 0.14.2 |
| std.cmyk | cmyk | [https://typst.app/docs/reference/visualize/color/#definitions-cmyk](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) | 0.14.2 |
| std.colbreak | colbreak | [https://typst.app/docs/reference/layout/colbreak/](https://typst.app/docs/reference/layout/colbreak/) | 0.14.2 |
| std.color | color | [https://typst.app/docs/reference/visualize/color/](https://typst.app/docs/reference/visualize/color/) | 0.14.2 |
| std.color.components | components | [https://typst.app/docs/reference/visualize/color/#definitions-components](https://typst.app/docs/reference/visualize/color/#definitions-components) | 0.14.2 |
| std.color.darken | darken | [https://typst.app/docs/reference/visualize/color/#definitions-darken](https://typst.app/docs/reference/visualize/color/#definitions-darken) | 0.14.2 |
| std.color.desaturate | desaturate | [https://typst.app/docs/reference/visualize/color/#definitions-desaturate](https://typst.app/docs/reference/visualize/color/#definitions-desaturate) | 0.14.2 |
| std.color.hsl | color.hsl | [https://typst.app/docs/reference/visualize/color/#definitions-hsl](https://typst.app/docs/reference/visualize/color/#definitions-hsl) | 0.14.2 |
| std.color.hsv | color.hsv | [https://typst.app/docs/reference/visualize/color/#definitions-hsv](https://typst.app/docs/reference/visualize/color/#definitions-hsv) | 0.14.2 |
| std.color.lighten | lighten | [https://typst.app/docs/reference/visualize/color/#definitions-lighten](https://typst.app/docs/reference/visualize/color/#definitions-lighten) | 0.14.2 |
| std.color.linear_rgb | color.linear-rgb | [https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb) | 0.14.2 |
| std.color.map | color.map | [https://typst.app/docs/reference/visualize/color/#predefined-color-maps](https://typst.app/docs/reference/visualize/color/#predefined-color-maps) | 0.14.2 |
| std.color.mix | color.mix | [https://typst.app/docs/reference/visualize/color/#definitions-mix](https://typst.app/docs/reference/visualize/color/#definitions-mix) | 0.14.2 |
| std.color.negate | negate | [https://typst.app/docs/reference/visualize/color/#definitions-negate](https://typst.app/docs/reference/visualize/color/#definitions-negate) | 0.14.2 |
| std.color.opacify | opacify | [https://typst.app/docs/reference/visualize/color/#definitions-opacify](https://typst.app/docs/reference/visualize/color/#definitions-opacify) | 0.14.2 |
| std.color.rotate | rotate | [https://typst.app/docs/reference/visualize/color/#definitions-rotate](https://typst.app/docs/reference/visualize/color/#definitions-rotate) | 0.14.2 |
| std.color.saturate | saturate | [https://typst.app/docs/reference/visualize/color/#definitions-saturate](https://typst.app/docs/reference/visualize/color/#definitions-saturate) | 0.14.2 |
| std.color.space | space | [https://typst.app/docs/reference/visualize/color/#definitions-space](https://typst.app/docs/reference/visualize/color/#definitions-space) | 0.14.2 |
| std.color.to_hex | to-hex | [https://typst.app/docs/reference/visualize/color/#definitions-to-hex](https://typst.app/docs/reference/visualize/color/#definitions-to-hex) | 0.14.2 |
| std.color.transparentize | transparentize | [https://typst.app/docs/reference/visualize/color/#definitions-transparentize](https://typst.app/docs/reference/visualize/color/#definitions-transparentize) | 0.14.2 |
| std.columns | columns | [https://typst.app/docs/reference/layout/columns/](https://typst.app/docs/reference/layout/columns/) | 0.14.2 |
| std.curve | curve | [https://typst.app/docs/reference/visualize/curve/](https://typst.app/docs/reference/visualize/curve/) | 0.14.2 |
| std.curve.close | curve.close | [https://typst.app/docs/reference/visualize/curve/#definitions-close](https://typst.app/docs/reference/visualize/curve/#definitions-close) | 0.14.2 |
| std.curve.cubic | curve.cubic | [https://typst.app/docs/reference/visualize/curve/#definitions-cubic](https://typst.app/docs/reference/visualize/curve/#definitions-cubic) | 0.14.2 |
| std.curve.line | curve.line | [https://typst.app/docs/reference/visualize/curve/#definitions-line](https://typst.app/docs/reference/visualize/curve/#definitions-line) | 0.14.2 |
| std.curve.move | curve.move | [https://typst.app/docs/reference/visualize/curve/#definitions-move](https://typst.app/docs/reference/visualize/curve/#definitions-move) | 0.14.2 |
| std.curve.quad | curve.quad | [https://typst.app/docs/reference/visualize/curve/#definitions-quad](https://typst.app/docs/reference/visualize/curve/#definitions-quad) | 0.14.2 |
| std.document | document | [https://typst.app/docs/reference/model/document/](https://typst.app/docs/reference/model/document/) | 0.14.2 |
| std.ellipse | ellipse | [https://typst.app/docs/reference/visualize/ellipse/](https://typst.app/docs/reference/visualize/ellipse/) | 0.14.2 |
| std.emph | emph | [https://typst.app/docs/reference/model/emph/](https://typst.app/docs/reference/model/emph/) | 0.14.2 |
| std.figure | figure | [https://typst.app/docs/reference/model/figure/](https://typst.app/docs/reference/model/figure/) | 0.14.2 |
| std.figure.caption | figure.caption | [https://typst.app/docs/reference/model/figure/#definitions-caption](https://typst.app/docs/reference/model/figure/#definitions-caption) | 0.14.2 |
| std.footnote | footnote | [https://typst.app/docs/reference/model/footnote/](https://typst.app/docs/reference/model/footnote/) | 0.14.2 |
| std.footnote.entry | footnote.entry | [https://typst.app/docs/reference/model/footnote/#definitions-entry](https://typst.app/docs/reference/model/footnote/#definitions-entry) | 0.14.2 |
| std.gradient | gradient | [https://typst.app/docs/reference/visualize/gradient/](https://typst.app/docs/reference/visualize/gradient/) | 0.14.2 |
| std.gradient.angle | angle | [https://typst.app/docs/reference/visualize/gradient/#definitions-angle](https://typst.app/docs/reference/visualize/gradient/#definitions-angle) | 0.14.2 |
| std.gradient.center | center | [https://typst.app/docs/reference/visualize/gradient/#definitions-center](https://typst.app/docs/reference/visualize/gradient/#definitions-center) | 0.14.2 |
| std.gradient.conic | gradient.conic | [https://typst.app/docs/reference/visualize/gradient/#definitions-conic](https://typst.app/docs/reference/visualize/gradient/#definitions-conic) | 0.14.2 |
| std.gradient.focal_center | focal-center | [https://typst.app/docs/reference/visualize/gradient/#definitions-focal-center](https://typst.app/docs/reference/visualize/gradient/#definitions-focal-center) | 0.14.2 |
| std.gradient.focal_radius | focal-radius | [https://typst.app/docs/reference/visualize/gradient/#definitions-focal-radius](https://typst.app/docs/reference/visualize/gradient/#definitions-focal-radius) | 0.14.2 |
| std.gradient.kind | kind | [https://typst.app/docs/reference/visualize/gradient/#definitions-kind](https://typst.app/docs/reference/visualize/gradient/#definitions-kind) | 0.14.2 |
| std.gradient.linear | gradient.linear | [https://typst.app/docs/reference/visualize/gradient/#definitions-linear](https://typst.app/docs/reference/visualize/gradient/#definitions-linear) | 0.14.2 |
| std.gradient.radial | gradient.radial | [https://typst.app/docs/reference/visualize/gradient/#definitions-radial](https://typst.app/docs/reference/visualize/gradient/#definitions-radial) | 0.14.2 |
| std.gradient.radius | radius | [https://typst.app/docs/reference/visualize/gradient/#definitions-radius](https://typst.app/docs/reference/visualize/gradient/#definitions-radius) | 0.14.2 |
| std.gradient.relative | relative | [https://typst.app/docs/reference/visualize/gradient/#definitions-relative](https://typst.app/docs/reference/visualize/gradient/#definitions-relative) | 0.14.2 |
| std.gradient.repeat | repeat | [https://typst.app/docs/reference/visualize/gradient/#definitions-repeat](https://typst.app/docs/reference/visualize/gradient/#definitions-repeat) | 0.14.2 |
| std.gradient.sample | sample | [https://typst.app/docs/reference/visualize/gradient/#definitions-sample](https://typst.app/docs/reference/visualize/gradient/#definitions-sample) | 0.14.2 |
| std.gradient.samples | samples | [https://typst.app/docs/reference/visualize/gradient/#definitions-samples](https://typst.app/docs/reference/visualize/gradient/#definitions-samples) | 0.14.2 |
| std.gradient.sharp | sharp | [https://typst.app/docs/reference/visualize/gradient/#definitions-sharp](https://typst.app/docs/reference/visualize/gradient/#definitions-sharp) | 0.14.2 |
| std.gradient.space | space | [https://typst.app/docs/reference/visualize/gradient/#definitions-space](https://typst.app/docs/reference/visualize/gradient/#definitions-space) | 0.14.2 |
| std.gradient.stops | stops | [https://typst.app/docs/reference/visualize/gradient/#definitions-stops](https://typst.app/docs/reference/visualize/gradient/#definitions-stops) | 0.14.2 |
| std.grid | grid | [https://typst.app/docs/reference/layout/grid/](https://typst.app/docs/reference/layout/grid/) | 0.14.2 |
| std.grid.cell | grid.cell | [https://typst.app/docs/reference/layout/grid/#definitions-cell](https://typst.app/docs/reference/layout/grid/#definitions-cell) | 0.14.2 |
| std.grid.footer | grid.footer | [https://typst.app/docs/reference/layout/grid/#definitions-footer](https://typst.app/docs/reference/layout/grid/#definitions-footer) | 0.14.2 |
| std.grid.header | grid.header | [https://typst.app/docs/reference/layout/grid/#definitions-header](https://typst.app/docs/reference/layout/grid/#definitions-header) | 0.14.2 |
| std.grid.hline | grid.hline | [https://typst.app/docs/reference/layout/grid/#definitions-hline](https://typst.app/docs/reference/layout/grid/#definitions-hline) | 0.14.2 |
| std.grid.vline | grid.vline | [https://typst.app/docs/reference/layout/grid/#definitions-vline](https://typst.app/docs/reference/layout/grid/#definitions-vline) | 0.14.2 |
| std.heading | heading | [https://typst.app/docs/reference/model/heading/](https://typst.app/docs/reference/model/heading/) | 0.14.2 |
| std.hide | hide | [https://typst.app/docs/reference/layout/hide/](https://typst.app/docs/reference/layout/hide/) | 0.14.2 |
| std.highlight | highlight | [https://typst.app/docs/reference/text/highlight/](https://typst.app/docs/reference/text/highlight/) | 0.14.2 |
| std.hspace | h | [https://typst.app/docs/reference/layout/h/](https://typst.app/docs/reference/layout/h/) | 0.14.2 |
| std.image | image | [https://typst.app/docs/reference/visualize/image/](https://typst.app/docs/reference/visualize/image/) | 0.14.2 |
| std.layout | layout | [https://typst.app/docs/reference/layout/layout/](https://typst.app/docs/reference/layout/layout/) | 0.14.2 |
| std.line | line | [https://typst.app/docs/reference/visualize/line/](https://typst.app/docs/reference/visualize/line/) | 0.14.2 |
| std.linebreak | linebreak | [https://typst.app/docs/reference/text/linebreak/](https://typst.app/docs/reference/text/linebreak/) | 0.14.2 |
| std.link | link | [https://typst.app/docs/reference/model/link/](https://typst.app/docs/reference/model/link/) | 0.14.2 |
| std.lorem | lorem | [https://typst.app/docs/reference/text/lorem/](https://typst.app/docs/reference/text/lorem/) | 0.14.2 |
| std.lower | lower | [https://typst.app/docs/reference/text/lower/](https://typst.app/docs/reference/text/lower/) | 0.14.2 |
| std.luma | luma | [https://typst.app/docs/reference/visualize/color/#definitions-luma](https://typst.app/docs/reference/visualize/color/#definitions-luma) | 0.14.2 |
| std.measure | measure | [https://typst.app/docs/reference/layout/measure/](https://typst.app/docs/reference/layout/measure/) | 0.14.2 |
| std.move | move | [https://typst.app/docs/reference/layout/move/](https://typst.app/docs/reference/layout/move/) | 0.14.2 |
| std.numbered_list | enum | [https://typst.app/docs/reference/model/enum/](https://typst.app/docs/reference/model/enum/) | 0.14.2 |
| std.numbered_list.item | enum.item | [https://typst.app/docs/reference/model/enum/#definitions-item](https://typst.app/docs/reference/model/enum/#definitions-item) | 0.14.2 |
| std.numbering | numbering | [https://typst.app/docs/reference/model/numbering/](https://typst.app/docs/reference/model/numbering/) | 0.14.2 |
| std.oklab | oklab | [https://typst.app/docs/reference/visualize/color/#definitions-oklab](https://typst.app/docs/reference/visualize/color/#definitions-oklab) | 0.14.2 |
| std.oklch | oklch | [https://typst.app/docs/reference/visualize/color/#definitions-oklch](https://typst.app/docs/reference/visualize/color/#definitions-oklch) | 0.14.2 |
| std.outline | outline | [https://typst.app/docs/reference/model/outline/](https://typst.app/docs/reference/model/outline/) | 0.14.2 |
| std.outline.body | body | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body) | 0.14.2 |
| std.outline.entry | outline.entry | [https://typst.app/docs/reference/model/outline/#definitions-entry](https://typst.app/docs/reference/model/outline/#definitions-entry) | 0.14.2 |
| std.outline.indented | indented | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented) | 0.14.2 |
| std.outline.inner | inner | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner) | 0.14.2 |
| std.outline.page | page | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page) | 0.14.2 |
| std.outline.prefix | prefix | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix) | 0.14.2 |
| std.overline | overline | [https://typst.app/docs/reference/text/overline/](https://typst.app/docs/reference/text/overline/) | 0.14.2 |
| std.pad | pad | [https://typst.app/docs/reference/layout/pad/](https://typst.app/docs/reference/layout/pad/) | 0.14.2 |
| std.page | page | [https://typst.app/docs/reference/layout/page/](https://typst.app/docs/reference/layout/page/) | 0.14.2 |
| std.pagebreak | pagebreak | [https://typst.app/docs/reference/layout/pagebreak/](https://typst.app/docs/reference/layout/pagebreak/) | 0.14.2 |
| std.par | par | [https://typst.app/docs/reference/model/par/](https://typst.app/docs/reference/model/par/) | 0.14.2 |
| std.par.line | par.line | [https://typst.app/docs/reference/model/par/#definitions-line](https://typst.app/docs/reference/model/par/#definitions-line) | 0.14.2 |
| std.parbreak | parbreak | [https://typst.app/docs/reference/model/parbreak/](https://typst.app/docs/reference/model/parbreak/) | 0.14.2 |
| std.place | place | [https://typst.app/docs/reference/layout/place/](https://typst.app/docs/reference/layout/place/) | 0.14.2 |
| std.place.flush | place.flush | [https://typst.app/docs/reference/layout/place/#definitions-flush](https://typst.app/docs/reference/layout/place/#definitions-flush) | 0.14.2 |
| std.polygon | polygon | [https://typst.app/docs/reference/visualize/polygon/](https://typst.app/docs/reference/visualize/polygon/) | 0.14.2 |
| std.polygon.regular | polygon.regular | [https://typst.app/docs/reference/visualize/polygon/#definitions-regular](https://typst.app/docs/reference/visualize/polygon/#definitions-regular) | 0.14.2 |
| std.quote | quote | [https://typst.app/docs/reference/model/quote/](https://typst.app/docs/reference/model/quote/) | 0.14.2 |
| std.raw | raw | [https://typst.app/docs/reference/text/raw/](https://typst.app/docs/reference/text/raw/) | 0.14.2 |
| std.raw.line | raw.line | [https://typst.app/docs/reference/text/raw/#definitions-line](https://typst.app/docs/reference/text/raw/#definitions-line) | 0.14.2 |
| std.rect | rect | [https://typst.app/docs/reference/visualize/rect/](https://typst.app/docs/reference/visualize/rect/) | 0.14.2 |
| std.ref | ref | [https://typst.app/docs/reference/model/ref/](https://typst.app/docs/reference/model/ref/) | 0.14.2 |
| std.repeat | repeat | [https://typst.app/docs/reference/layout/repeat/](https://typst.app/docs/reference/layout/repeat/) | 0.14.2 |
| std.rgb | rgb | [https://typst.app/docs/reference/visualize/color/#definitions-rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb) | 0.14.2 |
| std.rotate | rotate | [https://typst.app/docs/reference/layout/rotate/](https://typst.app/docs/reference/layout/rotate/) | 0.14.2 |
| std.scale | scale | [https://typst.app/docs/reference/layout/scale/](https://typst.app/docs/reference/layout/scale/) | 0.14.2 |
| std.skew | skew | [https://typst.app/docs/reference/layout/skew/](https://typst.app/docs/reference/layout/skew/) | 0.14.2 |
| std.smallcaps | smallcaps | [https://typst.app/docs/reference/text/smallcaps/](https://typst.app/docs/reference/text/smallcaps/) | 0.14.2 |
| std.smartquote | smartquote | [https://typst.app/docs/reference/text/smartquote/](https://typst.app/docs/reference/text/smartquote/) | 0.14.2 |
| std.square | square | [https://typst.app/docs/reference/visualize/square/](https://typst.app/docs/reference/visualize/square/) | 0.14.2 |
| std.stack | stack | [https://typst.app/docs/reference/layout/stack/](https://typst.app/docs/reference/layout/stack/) | 0.14.2 |
| std.strike | strike | [https://typst.app/docs/reference/text/strike/](https://typst.app/docs/reference/text/strike/) | 0.14.2 |
| std.strong | strong | [https://typst.app/docs/reference/model/strong/](https://typst.app/docs/reference/model/strong/) | 0.14.2 |
| std.subscript | sub | [https://typst.app/docs/reference/text/sub/](https://typst.app/docs/reference/text/sub/) | 0.14.2 |
| std.superscript | super | [https://typst.app/docs/reference/text/super/](https://typst.app/docs/reference/text/super/) | 0.14.2 |
| std.table | table | [https://typst.app/docs/reference/model/table/](https://typst.app/docs/reference/model/table/) | 0.14.2 |
| std.table.cell | table.cell | [https://typst.app/docs/reference/model/table/#definitions-cell](https://typst.app/docs/reference/model/table/#definitions-cell) | 0.14.2 |
| std.table.footer | table.footer | [https://typst.app/docs/reference/model/table/#definitions-footer](https://typst.app/docs/reference/model/table/#definitions-footer) | 0.14.2 |
| std.table.header | table.header | [https://typst.app/docs/reference/model/table/#definitions-header](https://typst.app/docs/reference/model/table/#definitions-header) | 0.14.2 |
| std.table.hline | table.hline | [https://typst.app/docs/reference/model/table/#definitions-hline](https://typst.app/docs/reference/model/table/#definitions-hline) | 0.14.2 |
| std.table.vline | table.vline | [https://typst.app/docs/reference/model/table/#definitions-vline](https://typst.app/docs/reference/model/table/#definitions-vline) | 0.14.2 |
| std.terms | terms | [https://typst.app/docs/reference/model/terms/](https://typst.app/docs/reference/model/terms/) | 0.14.2 |
| std.terms.item | terms.item | [https://typst.app/docs/reference/model/terms/#definitions-item](https://typst.app/docs/reference/model/terms/#definitions-item) | 0.14.2 |
| std.text | text | [https://typst.app/docs/reference/text/text/](https://typst.app/docs/reference/text/text/) | 0.14.2 |
| std.tiling | tiling | [https://typst.app/docs/reference/visualize/tiling/](https://typst.app/docs/reference/visualize/tiling/) | 0.14.2 |
| std.title | title | [https://typst.app/docs/reference/model/title/](https://typst.app/docs/reference/model/title/) | 0.14.2 |
| std.underline | underline | [https://typst.app/docs/reference/text/underline/](https://typst.app/docs/reference/text/underline/) | 0.14.2 |
| std.upper | upper | [https://typst.app/docs/reference/text/upper/](https://typst.app/docs/reference/text/upper/) | 0.14.2 |
| std.visualize._image_decode | image.decode | [https://typst.app/docs/reference/visualize/image/#definitions-decode](https://typst.app/docs/reference/visualize/image/#definitions-decode) | 0.14.2 |
| std.visualize.path | path | [https://typst.app/docs/reference/visualize/path/](https://typst.app/docs/reference/visualize/path/) | 0.14.2 |
| std.visualize.pattern | pattern | [https://typst.app/docs/reference/visualize/tiling/#compatibility](https://typst.app/docs/reference/visualize/tiling/#compatibility) | 0.14.2 |
| std.vspace | v | [https://typst.app/docs/reference/layout/v/](https://typst.app/docs/reference/layout/v/) | 0.14.2 |
| subpar.grid | subpar.grid | [https://typst.app/universe/package/subpar](https://typst.app/universe/package/subpar) | None |

## Examples

`std.align`:

```python
>>> align('"Hello, World!"', 'center')
'#align(center, "Hello, World!")'
>>> align('[Hello, World!]', 'center')
'#align(center, [Hello, World!])'
>>> align(lorem(20), 'center')
'#align(center, lorem(20))'
```

`std.bibliography`:

```python
>>> bibliography('"bibliography.bib"', style='"cell"')
'#bibliography("bibliography.bib", style: "cell")'
```

`std.block`:

```python
>>> block('"Hello, World!"')
'#block("Hello, World!")'
>>> block('[Hello, World!]')
'#block([Hello, World!])'
>>> block(lorem(20))
'#block(lorem(20))'
>>> block(lorem(20), width='100%')
'#block(lorem(20), width: 100%)'
```

`std.box`:

```python
>>> box('"Hello, World!"')
'#box("Hello, World!")'
>>> box('[Hello, World!]')
'#box([Hello, World!])'
>>> box(lorem(20))
'#box(lorem(20))'
>>> box(lorem(20), width='100%')
'#box(lorem(20), width: 100%)'
```

`std.bullet_list`:

```python
>>> bullet_list(lorem(20), lorem(20), lorem(20))
'#list(lorem(20), lorem(20), lorem(20))'
>>> bullet_list(lorem(20), lorem(20), lorem(20), tight=False)
'#list(tight: false, lorem(20), lorem(20), lorem(20))'
```

`std.bullet_list.item`:

```python
>>> bullet_list.item('[Hello, World!]')
'#list.item([Hello, World!])'
```

`std.circle`:

```python
>>> circle('[Hello, world!]')
'#circle([Hello, world!])'
>>> circle('[Hello, world!]', radius='10pt')
'#circle([Hello, world!], radius: 10pt)'
>>> circle('[Hello, world!]', width='100%')
'#circle([Hello, world!], width: 100%)'
```

`std.cite`:

```python
>>> cite('<label>')
'#cite(<label>)'
>>> cite('<label>', supplement='[Hello, World!]')
'#cite(<label>, supplement: [Hello, World!])'
>>> cite('<label>', form='"prose"')
'#cite(<label>, form: "prose")'
>>> cite('<label>', style='"annual-reviews"')
'#cite(<label>, style: "annual-reviews")'
```

`std.cmyk`:

```python
>>> cmyk('0%', '0%', '0%', '0%')
'#cmyk(0%, 0%, 0%, 0%)'
>>> cmyk('50%', '50%', '50%', '50%')
'#cmyk(50%, 50%, 50%, 50%)'
```

`std.colbreak`:

```python
>>> colbreak()
'#colbreak()'
>>> colbreak(weak=True)
'#colbreak(weak: true)'
```

`std.color`:

```python
>>> color()
'#color'
```

`std.color.components`:

```python
>>> color.components(rgb(255, 255, 255))
'#rgb(255, 255, 255).components()'
```

`std.color.darken`:

```python
>>> color.darken(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).darken(50%)'
```

`std.color.desaturate`:

```python
>>> color.desaturate(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).desaturate(50%)'
```

`std.color.hsl`:

```python
>>> color.hsl('0deg', '50%', '50%', '50%')
'#color.hsl(0deg, 50%, 50%, 50%)'
>>> color.hsl('0deg', '50%', '50%')
'#color.hsl(0deg, 50%, 50%)'
```

`std.color.hsv`:

```python
>>> color.hsv('0deg', '50%', '50%', '50%')
'#color.hsv(0deg, 50%, 50%, 50%)'
>>> color.hsv('0deg', '50%', '50%')
'#color.hsv(0deg, 50%, 50%)'
```

`std.color.lighten`:

```python
>>> color.lighten(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).lighten(50%)'
```

`std.color.linear_rgb`:

```python
>>> color.linear_rgb(255, 255, 255)
'#color.linear-rgb(255, 255, 255)'
>>> color.linear_rgb('50%', '50%', '50%', '50%')
'#color.linear-rgb(50%, 50%, 50%, 50%)'
```

`std.color.map`:

```python
>>> color.map('turbo')
'#color.map.turbo'
```

`std.color.mix`:

```python
>>> color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space='oklch')
'#color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space: oklch)'
```

`std.color.negate`:

```python
>>> color.negate(rgb(255, 255, 255))
'#rgb(255, 255, 255).negate()'
>>> color.negate(rgb(255, 255, 255), space='oklch')
'#rgb(255, 255, 255).negate(space: oklch)'
```

`std.color.opacify`:

```python
>>> color.opacify(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).opacify(50%)'
```

`std.color.rotate`:

```python
>>> color.rotate(rgb(255, 255, 255), '90deg')
'#rgb(255, 255, 255).rotate(90deg)'
```

`std.color.saturate`:

```python
>>> color.saturate(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).saturate(50%)'
```

`std.color.space`:

```python
>>> color.space(rgb(255, 255, 255))
'#rgb(255, 255, 255).space()'
```

`std.color.to_hex`:

```python
>>> color.to_hex(rgb(255, 255, 255))
'#rgb(255, 255, 255).to-hex()'
```

`std.color.transparentize`:

```python
>>> color.transparentize(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).transparentize(50%)'
```

`std.columns`:

```python
>>> columns(lorem(20))
'#columns(lorem(20))'
>>> columns(lorem(20), 3)
'#columns(3, lorem(20))'
>>> columns(lorem(20), 3, gutter='8% + 0pt')
'#columns(3, lorem(20), gutter: 8% + 0pt)'
```

`std.curve`:

```python
>>> curve(
...     curve.move(('0pt', '50pt')),
...     curve.line(('100pt', '50pt')),
...     curve.cubic(None, ('90pt', '0pt'), ('50pt', '0pt')),
...     curve.close(),
...     stroke='blue',
... )
'#curve(stroke: blue, curve.move((0pt, 50pt)), curve.line((100pt, 50pt)), curve.cubic(none, (90pt, 0pt), (50pt, 0pt)), curve.close())'
```

`std.curve.close`:

```python
>>> curve.close(mode='"smooth"')
'#curve.close()'
>>> curve.close(mode='"straight"')
'#curve.close(mode: "straight")'
```

`std.curve.cubic`:

```python
>>> curve.cubic(('10pt', '10pt'), ('20pt', '20pt'), ('30pt', '30pt'))
'#curve.cubic((10pt, 10pt), (20pt, 20pt), (30pt, 30pt))'
>>> curve.cubic(
...     ('10pt', '10pt'), ('20pt', '20pt'), ('30pt', '30pt'), relative=True
... )
'#curve.cubic((10pt, 10pt), (20pt, 20pt), (30pt, 30pt), relative: true)'
```

`std.curve.line`:

```python
>>> curve.line(('10pt', '10pt'))
'#curve.line((10pt, 10pt))'
>>> curve.line(('10pt', '10pt'), relative=True)
'#curve.line((10pt, 10pt), relative: true)'
```

`std.curve.move`:

```python
>>> curve.move(('10pt', '10pt'))
'#curve.move((10pt, 10pt))'
>>> curve.move(('10pt', '10pt'), relative=True)
'#curve.move((10pt, 10pt), relative: true)'
```

`std.curve.quad`:

```python
>>> curve.quad(('10pt', '10pt'), ('20pt', '20pt'))
'#curve.quad((10pt, 10pt), (20pt, 20pt))'
>>> curve.quad(('10pt', '10pt'), ('20pt', '20pt'), relative=True)
'#curve.quad((10pt, 10pt), (20pt, 20pt), relative: true)'
```

`std.ellipse`:

```python
>>> ellipse('[Hello, World!]')
'#ellipse([Hello, World!])'
>>> ellipse('[Hello, World!]', width='100%')
'#ellipse([Hello, World!], width: 100%)'
```

`std.emph`:

```python
>>> emph('"Hello, World!"')
'#emph("Hello, World!")'
>>> emph('[Hello, World!]')
'#emph([Hello, World!])'
```

`std.figure`:

```python
>>> figure(image('"image.png"'))
'#figure(image("image.png"))'
>>> figure(image('"image.png"'), caption='[Hello, World!]')
'#figure(image("image.png"), caption: [Hello, World!])'
```

`std.figure.caption`:

```python
>>> figure.caption('[Hello, World!]')
'#figure.caption([Hello, World!])'
>>> figure.caption('[Hello, World!]', position='top', separator='[---]')
'#figure.caption([Hello, World!], position: top, separator: [---])'
```

`std.footnote`:

```python
>>> footnote('[Hello, World!]')
'#footnote([Hello, World!])'
>>> footnote('[Hello, World!]', numbering='"a"')
'#footnote([Hello, World!], numbering: "a")'
```

`std.gradient`:

```python
>>> gradient()
'#gradient'
```

`std.gradient.angle`:

```python
>>> gradient.angle(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).angle()'
```

`std.gradient.center`:

```python
>>> gradient.center(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).center()'
```

`std.gradient.conic`:

```python
>>> gradient.conic(color.map('viridis'), angle='90deg', center=('10%', '40%'))
'#gradient.conic(..color.map.viridis, angle: 90deg, center: (10%, 40%))'
```

`std.gradient.focal_center`:

```python
>>> gradient.focal_center(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).focal-center()'
```

`std.gradient.focal_radius`:

```python
>>> gradient.focal_radius(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).focal-radius()'
```

`std.gradient.kind`:

```python
>>> gradient.kind(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).kind()'
```

`std.gradient.linear`:

```python
>>> gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))
'#gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))'
```

`std.gradient.radial`:

```python
>>> gradient.radial(
...     color.map('viridis'), focal_center=('10%', '40%'), focal_radius='5%'
... )
'#gradient.radial(..color.map.viridis, focal-center: (10%, 40%), focal-radius: 5%)'
```

`std.gradient.radius`:

```python
>>> gradient.radius(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).radius()'
```

`std.gradient.relative`:

```python
>>> gradient.relative(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).relative()'
```

`std.gradient.repeat`:

```python
>>> gradient.repeat(gradient.radial('aqua', 'white'), 4, mirror=True)
'#gradient.radial(aqua, white).repeat(4, mirror: true)'
```

`std.gradient.sharp`:

```python
>>> gradient.sharp(gradient.linear(color.map('rainbow')), 5, smoothness='50%')
'#gradient.linear(..color.map.rainbow).sharp(5, smoothness: 50%)'
```

`std.gradient.space`:

```python
>>> gradient.space(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).space()'
```

`std.gradient.stops`:

```python
>>> gradient.stops(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).stops()'
```

`std.grid`:

```python
>>> grid(lorem(20), lorem(20), lorem(20), align=('center',) * 3)
'#grid(align: (center, center, center), lorem(20), lorem(20), lorem(20))'
```

`std.grid.cell`:

```python
>>> grid.cell(lorem(20), x=3, y=3)
'#grid.cell(lorem(20), x: 3, y: 3)'
```

`std.heading`:

```python
>>> heading('[Hello, World!]')
'#heading([Hello, World!])'
>>> heading('[Hello, World!]', level=1)
'#heading([Hello, World!], level: 1)'
>>> heading('[Hello, World!]', level=1, depth=2)
'#heading([Hello, World!], level: 1, depth: 2)'
>>> heading('[Hello, World!]', level=1, depth=2, offset=10)
'#heading([Hello, World!], level: 1, depth: 2, offset: 10)'
>>> heading('[Hello, World!]', level=1, depth=2, offset=10, numbering='"a"')
'#heading([Hello, World!], level: 1, depth: 2, offset: 10, numbering: "a")'
>>> heading(
...     '[Hello, World!]',
...     level=1,
...     depth=2,
...     offset=10,
...     numbering='"a"',
...     supplement='"Supplement"',
... )
'#heading([Hello, World!], level: 1, depth: 2, offset: 10, numbering: "a", supplement: "Supplement")'
```

`std.hide`:

```python
>>> hide(lorem(20))
'#hide(lorem(20))'
```

`std.highlight`:

```python
>>> highlight('"Hello, world!"', fill=rgb('"#ffffff"'))
'#highlight("Hello, world!", fill: rgb("#ffffff"))'
>>> highlight('"Hello, world!"', fill=rgb('"#ffffff"'), stroke=rgb('"#000000"'))
'#highlight("Hello, world!", fill: rgb("#ffffff"), stroke: rgb("#000000"))'
>>> highlight(
...     '"Hello, world!"',
...     fill=rgb('"#ffffff"'),
...     stroke=rgb('"#000000"'),
...     top_edge='"bounds"',
...     bottom_edge='"bounds"',
... )
'#highlight("Hello, world!", fill: rgb("#ffffff"), stroke: rgb("#000000"), top-edge: "bounds", bottom-edge: "bounds")'
```

`std.hspace`:

```python
>>> hspace('1em')
'#h(1em)'
>>> hspace('1em', weak=True)
'#h(1em, weak: true)'
```

`std.image`:

```python
>>> image('"image.png"')
'#image("image.png")'
>>> image('"image.png"', fit='"contain"')
'#image("image.png", fit: "contain")'
```

`std.line`:

```python
>>> line()
'#line()'
>>> line(end=('100% + 0pt', '100% + 0pt'))
'#line(end: (100% + 0pt, 100% + 0pt))'
>>> line(angle='90deg')
'#line(angle: 90deg)'
>>> line(stroke='1pt + red')
'#line(stroke: 1pt + red)'
```

`std.linebreak`:

```python
>>> linebreak()
'#linebreak()'
>>> linebreak(justify=True)
'#linebreak(justify: true)'
```

`std.link`:

```python
>>> link('"https://typst.app"')
'#link("https://typst.app")'
>>> link('"https://typst.app"', '"Typst"')
'#link("https://typst.app", "Typst")'
```

`std.lorem`:

```python
>>> lorem(10)
'#lorem(10)'
```

`std.lower`:

```python
>>> lower('"Hello, World!"')
'#lower("Hello, World!")'
>>> lower('[Hello, World!]')
'#lower([Hello, World!])'
>>> lower(upper('"Hello, World!"'))
'#lower(upper("Hello, World!"))'
```

`std.luma`:

```python
>>> luma('50%')
'#luma(50%)'
>>> luma('50%', '50%')
'#luma(50%, 50%)'
```

`std.move`:

```python
>>> move(lorem(20), dx='50% + 10pt', dy='10% + 5pt')
'#move(lorem(20), dx: 50% + 10pt, dy: 10% + 5pt)'
```

`std.numbered_list`:

```python
>>> numbered_list(lorem(20), lorem(20), lorem(20))
'#enum(lorem(20), lorem(20), lorem(20))'
>>> numbered_list(lorem(20), lorem(20), lorem(20), tight=False)
'#enum(tight: false, lorem(20), lorem(20), lorem(20))'
```

`std.numbered_list.item`:

```python
>>> numbered_list.item('[Hello, World!]', number=2)
'#enum.item(2, [Hello, World!])'
```

`std.numbering`:

```python
>>> numbering('"1.1)"', 1, 2)
'#numbering("1.1)", 1, 2)'
```

`std.oklab`:

```python
>>> oklab('50%', '0%', '0%')
'#oklab(50%, 0%, 0%)'
>>> oklab('50%', '0%', '0%', '50%')
'#oklab(50%, 0%, 0%, 50%)'
```

`std.oklch`:

```python
>>> oklch('50%', '0%', '0deg')
'#oklch(50%, 0%, 0deg)'
>>> oklch('50%', '0%', '0deg', '50%')
'#oklch(50%, 0%, 0deg, 50%)'
```

`std.outline`:

```python
>>> outline()
'#outline()'
>>> outline(title='"Hello, World!"', target=heading.where(outlined=True))
'#outline(title: "Hello, World!", target: heading.where(outlined: true))'
```

`std.overline`:

```python
>>> overline('"Hello, World!"')
'#overline("Hello, World!")'
>>> overline('[Hello, World!]')
'#overline([Hello, World!])'
>>> overline(
...     upper('"Hello, World!"'),
...     stroke='red',
...     offset='0pt',
...     extent='0pt',
...     evade=False,
...     background=True,
... )
'#overline(upper("Hello, World!"), stroke: red, offset: 0pt, evade: false, background: true)'
```

`std.pad`:

```python
>>> pad(
...     lorem(20),
...     left='4% + 0pt',
...     top='4% + 0pt',
...     right='4% + 0pt',
...     bottom='4% + 0pt',
... )
'#pad(lorem(20), left: 4% + 0pt, top: 4% + 0pt, right: 4% + 0pt, bottom: 4% + 0pt)'
```

`std.page`:

```python
>>> page(lorem(20))
'#page(lorem(20))'
>>> page(lorem(20), paper='"a0"', width='8.5in', height='11in')
'#page(lorem(20), paper: "a0", width: 8.5in, height: 11in)'
```

`std.pagebreak`:

```python
>>> pagebreak()
'#pagebreak()'
>>> pagebreak(weak=True)
'#pagebreak(weak: true)'
>>> pagebreak(to='"even"')
'#pagebreak(to: "even")'
```

`std.par`:

```python
>>> par('"Hello, World!"')
'#par("Hello, World!")'
>>> par('[Hello, World!]')
'#par([Hello, World!])'
>>> par(
...     '[Hello, World!]',
...     leading='0.1em',
...     spacing='0.5em',
...     justify=True,
...     linebreaks='"simple"',
...     first_line_indent='0.2em',
...     hanging_indent='0.3em',
... )
'#par([Hello, World!], leading: 0.1em, spacing: 0.5em, justify: true, linebreaks: "simple", first-line-indent: 0.2em, hanging-indent: 0.3em)'
```

`std.parbreak`:

```python
>>> parbreak()
'#parbreak()'
```

`std.place`:

```python
>>> place(lorem(20))
'#place(lorem(20))'
>>> place(lorem(20), 'top')
'#place(top, lorem(20))'
```

`std.place.flush`:

```python
>>> place.flush()
'#place.flush()'
```

`std.quote`:

```python
>>> quote('"Hello, World!"')
'#quote("Hello, World!")'
>>> quote('"Hello, World!"', block=True)
'#quote("Hello, World!", block: true)'
>>> quote('"Hello, World!"', quotes=False)
'#quote("Hello, World!", quotes: false)'
>>> quote('"Hello, World!"', attribution='"John Doe"')
'#quote("Hello, World!", attribution: "John Doe")'
```

`std.raw`:

```python
>>> raw('"Hello, World!"')
'#raw("Hello, World!")'
>>> raw('"Hello, World!"', block=True, align='center')
'#raw("Hello, World!", block: true, align: center)'
>>> raw('"Hello, World!"', lang='"rust"')
'#raw("Hello, World!", lang: "rust")'
>>> raw('"Hello, World!"', tab_size=4)
'#raw("Hello, World!", tab-size: 4)'
```

`std.raw.line`:

```python
>>> raw.line(1, 1, '"Hello, World!"', '"Hello, World!"')
'#raw.line(1, 1, "Hello, World!", "Hello, World!")'
```

`std.ref`:

```python
>>> ref('<label>')
'#ref(<label>)'
>>> ref('<label>', supplement='[Hello, World!]')
'#ref(<label>, supplement: [Hello, World!])'
```

`std.repeat`:

```python
>>> repeat(lorem(20), gap='0.5em')
'#repeat(lorem(20), gap: 0.5em)'
>>> repeat(lorem(20), gap='0.5em', justify=False)
'#repeat(lorem(20), gap: 0.5em, justify: false)'
```

`std.rgb`:

```python
>>> rgb(255, 255, 255)
'#rgb(255, 255, 255)'
>>> rgb('50%', '50%', '50%', '50%')
'#rgb(50%, 50%, 50%, 50%)'
>>> rgb('"#ffffff"')
'#rgb("#ffffff")'
```

`std.rotate`:

```python
>>> rotate(lorem(20), '20deg')
'#rotate(20deg, lorem(20))'
>>> rotate(lorem(20), '20deg', origin='left + horizon')
'#rotate(20deg, lorem(20), origin: left + horizon)'
```

`std.scale`:

```python
>>> scale(lorem(20), '50%')
'#scale(50%, lorem(20))'
>>> scale(lorem(20), x='50%', y='50%')
'#scale(lorem(20), x: 50%, y: 50%)'
>>> scale(lorem(20), '50%', x='50%', y='50%')
'#scale(50%, lorem(20), x: 50%, y: 50%)'
```

`std.skew`:

```python
>>> skew(lorem(20), ax='10deg', ay='20deg')
'#skew(lorem(20), ax: 10deg, ay: 20deg)'
>>> skew(
...     lorem(20), ax='10deg', ay='20deg', origin='left + horizon', reflow=True
... )
'#skew(lorem(20), ax: 10deg, ay: 20deg, origin: left + horizon, reflow: true)'
```

`std.smallcaps`:

```python
>>> smallcaps('"Hello, World!"')
'#smallcaps("Hello, World!")'
>>> smallcaps('[Hello, World!]')
'#smallcaps([Hello, World!])'
>>> smallcaps('"Hello, World!"', all=True)
'#smallcaps("Hello, World!", all: true)'
```

`std.smartquote`:

```python
>>> smartquote(double=False, enabled=False, alternative=True, quotes='"()"')
'#smartquote(double: false, enabled: false, alternative: true, quotes: "()")'
>>> smartquote(quotes=('"()"', '"dict()"'))
'#smartquote(quotes: ("()", "dict()"))'
```

`std.stack`:

```python
>>> stack(rect(width='40pt'), dir='btt')
'#stack(dir: btt, rect(width: 40pt))'
>>> stack(
...     rect(width='40pt'), rect(width='120pt'), rect(width='90pt'), dir='btt'
... )
'#stack(dir: btt, rect(width: 40pt), rect(width: 120pt), rect(width: 90pt))'
>>> stack(
...     (rect(width='40pt'), rect(width='120pt'), rect(width='90pt')), dir='btt'
... )
'#stack(dir: btt, ..(rect(width: 40pt), rect(width: 120pt), rect(width: 90pt)))'
```

`std.strike`:

```python
>>> strike('"Hello, World!"')
'#strike("Hello, World!")'
>>> strike('[Hello, World!]')
'#strike([Hello, World!])'
>>> strike(
...     upper('"Hello, World!"'),
...     stroke='red',
...     offset='0.1em',
...     extent='0.2em',
...     background=True,
... )
'#strike(upper("Hello, World!"), stroke: red, offset: 0.1em, extent: 0.2em, background: true)'
```

`std.strong`:

```python
>>> strong('"Hello, World!"')
'#strong("Hello, World!")'
>>> strong('[Hello, World!]', delta=400)
'#strong([Hello, World!], delta: 400)'
```

`std.subscript`:

```python
>>> subscript('"Hello, World!"')
'#sub("Hello, World!")'
>>> subscript('[Hello, World!]')
'#sub([Hello, World!])'
>>> subscript(
...     '[Hello, World!]', typographic=False, baseline='0.3em', size='0.7em'
... )
'#sub([Hello, World!], typographic: false, baseline: 0.3em, size: 0.7em)'
```

`std.superscript`:

```python
>>> superscript('"Hello, World!"')
'#super("Hello, World!")'
>>> superscript('[Hello, World!]')
'#super([Hello, World!])'
>>> superscript(
...     '[Hello, World!]', typographic=False, baseline='-0.4em', size='0.7em'
... )
'#super([Hello, World!], typographic: false, baseline: -0.4em, size: 0.7em)'
```

`std.table`:

```python
>>> table('[1]')
'#table([1])'
>>> table('[1]', '[2]', '[3]')
'#table([1], [2], [3])'
>>> table(
...     '[1]',
...     '[2]',
...     '[3]',
...     columns=['1fr', '2fr', '3fr'],
...     rows=['1fr', '2fr', '3fr'],
...     gutter=['1fr', '2fr', '3fr'],
...     column_gutter=['1fr', '2fr', '3fr'],
...     row_gutter=['1fr', '2fr', '3fr'],
...     fill='red',
...     align=['center', 'center', 'center'],
... )
'#table(columns: (1fr, 2fr, 3fr), rows: (1fr, 2fr, 3fr), gutter: (1fr, 2fr, 3fr), column-gutter: (1fr, 2fr, 3fr), row-gutter: (1fr, 2fr, 3fr), fill: red, align: (center, center, center), [1], [2], [3])'
```

`std.terms`:

```python
>>> terms(('[1]', lorem(20)))
'#terms(([1], lorem(20)))'
>>> terms(('[1]', lorem(20)), ('[1]', lorem(20)))
'#terms(([1], lorem(20)), ([1], lorem(20)))'
>>> terms(('[1]', lorem(20)), ('[1]', lorem(20)), tight=False)
'#terms(tight: false, ([1], lorem(20)), ([1], lorem(20)))'
>>> terms(terms.item('[1]', lorem(20)), terms.item('[1]', lorem(20)))
'#terms(terms.item([1], lorem(20)), terms.item([1], lorem(20)))'
```

`std.terms.item`:

```python
>>> terms.item('"term"', '"description"')
'#terms.item("term", "description")'
```

`std.text`:

```python
>>> text('"Hello, World!"')
'#text("Hello, World!")'
>>> text('[Hello, World!]')
'#text([Hello, World!])'
>>> text('[Hello, World!]', font='"Times New Roman"')
'#text([Hello, World!], font: "Times New Roman")'
```

`std.tiling`:

```python
>>> from typstpy.std.layout import place
>>> tiling(
...     f'[{place(line(start=("0%", "0%"), end=("100%", "100%")))}, {place(line(start=("0%", "100%"), end=("100%", "0%")))}]',
...     size=('30pt', '30pt'),
... )
'#tiling([#place(line(start: (0%, 0%), end: (100%, 100%))), #place(line(start: (0%, 100%), end: (100%, 0%)))], size: (30pt, 30pt))'
```

`std.title`:

```python
>>> title()
'#title()'
>>> title('[My Thesis]')
'#title([My Thesis])'
```

`std.underline`:

```python
>>> underline('"Hello, World!"')
'#underline("Hello, World!")'
>>> underline('[Hello, World!]')
'#underline([Hello, World!])'
>>> underline(
...     '[Hello, World!]',
...     stroke='1pt + red',
...     offset='0pt',
...     extent='1pt',
...     evade=False,
...     background=True,
... )
'#underline([Hello, World!], stroke: 1pt + red, offset: 0pt, extent: 1pt, evade: false, background: true)'
```

`std.upper`:

```python
>>> upper('"Hello, World!"')
'#upper("Hello, World!")'
>>> upper('[Hello, World!]')
'#upper([Hello, World!])'
>>> upper(lower('"Hello, World!"'))
'#upper(lower("Hello, World!"))'
```

`std.visualize.path`:

```python
>>> path(('0%', '0%'), ('100%', '0%'), ('100%', '100%'), ('0%', '100%'))
'#path((0%, 0%), (100%, 0%), (100%, 100%), (0%, 100%))'
>>> path(
...     ('0%', '0%'),
...     ('100%', '0%'),
...     ('100%', '100%'),
...     ('0%', '100%'),
...     fill='red',
... )
'#path(fill: red, (0%, 0%), (100%, 0%), (100%, 100%), (0%, 100%))'
>>> path(
...     ('0%', '0%'),
...     ('100%', '0%'),
...     ('100%', '100%'),
...     ('0%', '100%'),
...     fill='red',
...     stroke='blue',
... )
'#path(fill: red, stroke: blue, (0%, 0%), (100%, 0%), (100%, 100%), (0%, 100%))'
```

`std.vspace`:

```python
>>> vspace('1em')
'#v(1em)'
>>> vspace('1em', weak=True)
'#v(1em, weak: true)'
```

`subpar.grid`:

```python
>>> grid(
...     figure(image('"image.png"')),
...     '<a>',
...     figure(image('"image.png"')),
...     '<b>',
...     columns=('1fr', '1fr'),
...     caption='[A figure composed of two sub figures.]',
...     label='<full>',
... )
'#subpar.grid(figure(image("image.png")), <a>, figure(image("image.png")), <b>, columns: (1fr, 1fr), caption: [A figure composed of two sub figures.], label: <full>)'
```

<!-- typstpy-generated-end -->
