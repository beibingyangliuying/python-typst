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

## Current Supports

| Package's function name | Typst's function name | Documentation on typst | Version |
| --- | --- | --- | --- |
| std.visualize.circle | circle | [https://typst.app/docs/reference/visualize/circle/](https://typst.app/docs/reference/visualize/circle/) | 0.13.x |
| std.visualize._color_map | color.map | [https://typst.app/docs/reference/visualize/color/#predefined-color-maps](https://typst.app/docs/reference/visualize/color/#predefined-color-maps) | 0.13.x |
| std.visualize.luma | luma | [https://typst.app/docs/reference/visualize/color/#definitions-luma](https://typst.app/docs/reference/visualize/color/#definitions-luma) | 0.13.x |
| std.visualize.oklab | oklab | [https://typst.app/docs/reference/visualize/color/#definitions-oklab](https://typst.app/docs/reference/visualize/color/#definitions-oklab) | 0.13.x |
| std.visualize.oklch | oklch | [https://typst.app/docs/reference/visualize/color/#definitions-oklch](https://typst.app/docs/reference/visualize/color/#definitions-oklch) | 0.13.x |
| std.visualize._color_linear_rgb | color.linear-rgb | [https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb) | 0.13.x |
| std.visualize.rgb | rgb | [https://typst.app/docs/reference/visualize/color/#definitions-rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb) | 0.13.x |
| std.visualize.cmyk | cmyk | [https://typst.app/docs/reference/visualize/color/#definitions-cmyk](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) | 0.13.x |
| std.visualize._color_hsl | color.hsl | [https://typst.app/docs/reference/visualize/color/#definitions-hsl](https://typst.app/docs/reference/visualize/color/#definitions-hsl) | 0.13.x |
| std.visualize._color_hsv | color.hsv | [https://typst.app/docs/reference/visualize/color/#definitions-hsv](https://typst.app/docs/reference/visualize/color/#definitions-hsv) | 0.13.x |
| std.visualize._color_components | components | [https://typst.app/docs/reference/visualize/color/#definitions-components](https://typst.app/docs/reference/visualize/color/#definitions-components) | 0.13.x |
| std.visualize._color_space | space | [https://typst.app/docs/reference/visualize/color/#definitions-space](https://typst.app/docs/reference/visualize/color/#definitions-space) | 0.13.x |
| std.visualize._color_to_hex | to-hex | [https://typst.app/docs/reference/visualize/color/#definitions-to-hex](https://typst.app/docs/reference/visualize/color/#definitions-to-hex) | 0.13.x |
| std.visualize._color_lighten | lighten | [https://typst.app/docs/reference/visualize/color/#definitions-lighten](https://typst.app/docs/reference/visualize/color/#definitions-lighten) | 0.13.x |
| std.visualize._color_darken | darken | [https://typst.app/docs/reference/visualize/color/#definitions-darken](https://typst.app/docs/reference/visualize/color/#definitions-darken) | 0.13.x |
| std.visualize._color_saturate | saturate | [https://typst.app/docs/reference/visualize/color/#definitions-saturate](https://typst.app/docs/reference/visualize/color/#definitions-saturate) | 0.13.x |
| std.visualize._color_desaturate | desaturate | [https://typst.app/docs/reference/visualize/color/#definitions-desaturate](https://typst.app/docs/reference/visualize/color/#definitions-desaturate) | 0.13.x |
| std.visualize._color_negate | negate | [https://typst.app/docs/reference/visualize/color/#definitions-negate](https://typst.app/docs/reference/visualize/color/#definitions-negate) | 0.13.x |
| std.visualize._color_rotate | rotate | [https://typst.app/docs/reference/visualize/color/#definitions-rotate](https://typst.app/docs/reference/visualize/color/#definitions-rotate) | 0.13.x |
| std.visualize._color_mix | color.mix | [https://typst.app/docs/reference/visualize/color/#definitions-mix](https://typst.app/docs/reference/visualize/color/#definitions-mix) | 0.13.x |
| std.visualize._color_transparentize | transparentize | [https://typst.app/docs/reference/visualize/color/#definitions-transparentize](https://typst.app/docs/reference/visualize/color/#definitions-transparentize) | 0.13.x |
| std.visualize._color_opacify | opacify | [https://typst.app/docs/reference/visualize/color/#definitions-opacify](https://typst.app/docs/reference/visualize/color/#definitions-opacify) | 0.13.x |
| std.visualize.color | color | [https://typst.app/docs/reference/visualize/color/](https://typst.app/docs/reference/visualize/color/) | 0.13.x |
| std.visualize._curve_move | curve.move | [https://typst.app/docs/reference/visualize/curve/#definitions-move](https://typst.app/docs/reference/visualize/curve/#definitions-move) | 0.13.x |
| std.visualize._curve_line | curve.line | [https://typst.app/docs/reference/visualize/curve/#definitions-line](https://typst.app/docs/reference/visualize/curve/#definitions-line) | 0.13.x |
| std.visualize._curve_quad | curve.quad | [https://typst.app/docs/reference/visualize/curve/#definitions-quad](https://typst.app/docs/reference/visualize/curve/#definitions-quad) | 0.13.x |
| std.visualize._curve_cubic | curve.cubic | [https://typst.app/docs/reference/visualize/curve/#definitions-cubic](https://typst.app/docs/reference/visualize/curve/#definitions-cubic) | 0.13.x |
| std.visualize._curve_close | curve.close | [https://typst.app/docs/reference/visualize/curve/#definitions-close](https://typst.app/docs/reference/visualize/curve/#definitions-close) | 0.13.x |
| std.visualize.curve | curve | [https://typst.app/docs/reference/visualize/curve/](https://typst.app/docs/reference/visualize/curve/) | 0.13.x |
| std.visualize.ellipse | ellipse | [https://typst.app/docs/reference/visualize/ellipse/](https://typst.app/docs/reference/visualize/ellipse/) | 0.13.x |
| std.visualize._gradient_linear | gradient.linear | [https://typst.app/docs/reference/visualize/gradient/#definitions-linear](https://typst.app/docs/reference/visualize/gradient/#definitions-linear) | 0.13.x |
| std.visualize._gradient_radial | gradient.radial | [https://typst.app/docs/reference/visualize/gradient/#definitions-radial](https://typst.app/docs/reference/visualize/gradient/#definitions-radial) | 0.13.x |
| std.visualize._gradient_conic | gradient.conic | [https://typst.app/docs/reference/visualize/gradient/#definitions-conic](https://typst.app/docs/reference/visualize/gradient/#definitions-conic) | 0.13.x |
| std.visualize._gradient_sharp | sharp | [https://typst.app/docs/reference/visualize/gradient/#definitions-sharp](https://typst.app/docs/reference/visualize/gradient/#definitions-sharp) | 0.13.x |
| std.visualize._gradient_repeat | repeat | [https://typst.app/docs/reference/visualize/gradient/#definitions-repeat](https://typst.app/docs/reference/visualize/gradient/#definitions-repeat) | 0.13.x |
| std.visualize._gradient_kind | kind | [https://typst.app/docs/reference/visualize/gradient/#definitions-kind](https://typst.app/docs/reference/visualize/gradient/#definitions-kind) | 0.13.x |
| std.visualize._gradient_stops | stops | [https://typst.app/docs/reference/visualize/gradient/#definitions-stops](https://typst.app/docs/reference/visualize/gradient/#definitions-stops) | 0.13.x |
| std.visualize._gradient_space | space | [https://typst.app/docs/reference/visualize/gradient/#definitions-space](https://typst.app/docs/reference/visualize/gradient/#definitions-space) | 0.13.x |
| std.visualize._gradient_relative | relative | [https://typst.app/docs/reference/visualize/gradient/#definitions-relative](https://typst.app/docs/reference/visualize/gradient/#definitions-relative) | 0.13.x |
| std.visualize._gradient_angle | angle | [https://typst.app/docs/reference/visualize/gradient/#definitions-angle](https://typst.app/docs/reference/visualize/gradient/#definitions-angle) | 0.13.x |
| std.visualize._gradient_center | center | [https://typst.app/docs/reference/visualize/gradient/#definitions-center](https://typst.app/docs/reference/visualize/gradient/#definitions-center) | 0.13.x |
| std.visualize._gradient_radius | radius | [https://typst.app/docs/reference/visualize/gradient/#definitions-radius](https://typst.app/docs/reference/visualize/gradient/#definitions-radius) | 0.13.x |
| std.visualize._gradient_focal_center | focal-center | [https://typst.app/docs/reference/visualize/gradient/#definitions-focal-center](https://typst.app/docs/reference/visualize/gradient/#definitions-focal-center) | 0.13.x |
| std.visualize._gradient_focal_radius | focal-radius | [https://typst.app/docs/reference/visualize/gradient/#definitions-focal-radius](https://typst.app/docs/reference/visualize/gradient/#definitions-focal-radius) | 0.13.x |
| std.visualize._gradient_sample | sample | [https://typst.app/docs/reference/visualize/gradient/#definitions-sample](https://typst.app/docs/reference/visualize/gradient/#definitions-sample) | 0.13.x |
| std.visualize._gradient_samples | samples | [https://typst.app/docs/reference/visualize/gradient/#definitions-samples](https://typst.app/docs/reference/visualize/gradient/#definitions-samples) | 0.13.x |
| std.visualize.gradient | gradient | [https://typst.app/docs/reference/visualize/gradient/](https://typst.app/docs/reference/visualize/gradient/) | 0.13.x |
| std.visualize._image_decode | image.decode | [https://typst.app/docs/reference/visualize/image/#definitions-decode](https://typst.app/docs/reference/visualize/image/#definitions-decode) | 0.13.x |
| std.visualize.image | image | [https://typst.app/docs/reference/visualize/image/](https://typst.app/docs/reference/visualize/image/) | 0.13.x |
| std.visualize.line | line | [https://typst.app/docs/reference/visualize/line/](https://typst.app/docs/reference/visualize/line/) | 0.13.x |
| std.visualize.path | path | [https://typst.app/docs/reference/visualize/path/](https://typst.app/docs/reference/visualize/path/) | 0.13.x |
| std.visualize.pattern | pattern | [https://typst.app/docs/reference/visualize/pattern/](https://typst.app/docs/reference/visualize/pattern/) | 0.13.x |
| std.visualize._polygon_regular | polygon.regular | [https://typst.app/docs/reference/visualize/polygon/#definitions-regular](https://typst.app/docs/reference/visualize/polygon/#definitions-regular) | 0.13.x |
| std.visualize.polygon | polygon | [https://typst.app/docs/reference/visualize/polygon/](https://typst.app/docs/reference/visualize/polygon/) | 0.13.x |
| std.visualize.rect | rect | [https://typst.app/docs/reference/visualize/rect/](https://typst.app/docs/reference/visualize/rect/) | 0.13.x |
| std.visualize.square | square | [https://typst.app/docs/reference/visualize/square/](https://typst.app/docs/reference/visualize/square/) | 0.13.x |
| std.visualize.tiling | tiling | [https://typst.app/docs/reference/visualize/tiling/](https://typst.app/docs/reference/visualize/tiling/) | 0.13.x |
| std.text.highlight | highlight | [https://typst.app/docs/reference/text/highlight/](https://typst.app/docs/reference/text/highlight/) | 0.13.x |
| std.text.linebreak | linebreak | [https://typst.app/docs/reference/text/linebreak/](https://typst.app/docs/reference/text/linebreak/) | 0.13.x |
| std.text.lorem | lorem | [https://typst.app/docs/reference/text/lorem/](https://typst.app/docs/reference/text/lorem/) | 0.13.x |
| std.text.lower | lower | [https://typst.app/docs/reference/text/lower/](https://typst.app/docs/reference/text/lower/) | 0.13.x |
| std.text.overline | overline | [https://typst.app/docs/reference/text/overline/](https://typst.app/docs/reference/text/overline/) | 0.13.x |
| std.text._raw_line | raw.line | [https://typst.app/docs/reference/text/raw/#definitions-line](https://typst.app/docs/reference/text/raw/#definitions-line) | 0.13.x |
| std.text.raw | raw | [https://typst.app/docs/reference/text/raw/](https://typst.app/docs/reference/text/raw/) | 0.13.x |
| std.text.smallcaps | smallcaps | [https://typst.app/docs/reference/text/smallcaps/](https://typst.app/docs/reference/text/smallcaps/) | 0.13.x |
| std.text.smartquote | smartquote | [https://typst.app/docs/reference/text/smartquote/](https://typst.app/docs/reference/text/smartquote/) | 0.13.x |
| std.text.strike | strike | [https://typst.app/docs/reference/text/strike/](https://typst.app/docs/reference/text/strike/) | 0.13.x |
| std.text.subscript | sub | [https://typst.app/docs/reference/text/sub/](https://typst.app/docs/reference/text/sub/) | 0.13.x |
| std.text.superscript | super | [https://typst.app/docs/reference/text/super/](https://typst.app/docs/reference/text/super/) | 0.13.x |
| std.text.text | text | [https://typst.app/docs/reference/text/text/](https://typst.app/docs/reference/text/text/) | 0.13.x |
| std.text.underline | underline | [https://typst.app/docs/reference/text/underline/](https://typst.app/docs/reference/text/underline/) | 0.13.x |
| std.text.upper | upper | [https://typst.app/docs/reference/text/upper/](https://typst.app/docs/reference/text/upper/) | 0.13.x |
| std.layout.align | align | [https://typst.app/docs/reference/layout/align/](https://typst.app/docs/reference/layout/align/) | 0.13.x |
| std.layout.block | block | [https://typst.app/docs/reference/layout/block/](https://typst.app/docs/reference/layout/block/) | 0.13.x |
| std.layout.box | box | [https://typst.app/docs/reference/layout/box/](https://typst.app/docs/reference/layout/box/) | 0.13.x |
| std.layout.colbreak | colbreak | [https://typst.app/docs/reference/layout/colbreak/](https://typst.app/docs/reference/layout/colbreak/) | 0.13.x |
| std.layout.columns | columns | [https://typst.app/docs/reference/layout/columns/](https://typst.app/docs/reference/layout/columns/) | 0.13.x |
| std.layout._grid_cell | grid.cell | [https://typst.app/docs/reference/layout/grid/#definitions-cell](https://typst.app/docs/reference/layout/grid/#definitions-cell) | 0.13.x |
| std.layout._grid_hline | grid.hline | [https://typst.app/docs/reference/layout/grid/#definitions-hline](https://typst.app/docs/reference/layout/grid/#definitions-hline) | 0.13.x |
| std.layout._grid_vline | grid.vline | [https://typst.app/docs/reference/layout/grid/#definitions-vline](https://typst.app/docs/reference/layout/grid/#definitions-vline) | 0.13.x |
| std.layout._grid_header | grid.header | [https://typst.app/docs/reference/layout/grid/#definitions-header](https://typst.app/docs/reference/layout/grid/#definitions-header) | 0.13.x |
| std.layout._grid_footer | grid.footer | [https://typst.app/docs/reference/layout/grid/#definitions-footer](https://typst.app/docs/reference/layout/grid/#definitions-footer) | 0.13.x |
| std.layout.grid | grid | [https://typst.app/docs/reference/layout/grid/](https://typst.app/docs/reference/layout/grid/) | 0.13.x |
| std.layout.hide | hide | [https://typst.app/docs/reference/layout/hide/](https://typst.app/docs/reference/layout/hide/) | 0.13.x |
| std.layout.layout | layout | [https://typst.app/docs/reference/layout/layout/](https://typst.app/docs/reference/layout/layout/) | 0.13.x |
| std.layout.measure | measure | [https://typst.app/docs/reference/layout/measure/](https://typst.app/docs/reference/layout/measure/) | 0.13.x |
| std.layout.move | move | [https://typst.app/docs/reference/layout/move/](https://typst.app/docs/reference/layout/move/) | 0.13.x |
| std.layout.pad | pad | [https://typst.app/docs/reference/layout/pad/](https://typst.app/docs/reference/layout/pad/) | 0.13.x |
| std.layout.page | page | [https://typst.app/docs/reference/layout/page/](https://typst.app/docs/reference/layout/page/) | 0.13.x |
| std.layout.pagebreak | pagebreak | [https://typst.app/docs/reference/layout/pagebreak/](https://typst.app/docs/reference/layout/pagebreak/) | 0.13.x |
| std.layout._place_flush | place.flush | [https://typst.app/docs/reference/layout/place/#definitions-flush](https://typst.app/docs/reference/layout/place/#definitions-flush) | 0.13.x |
| std.layout.place | place | [https://typst.app/docs/reference/layout/place/](https://typst.app/docs/reference/layout/place/) | 0.13.x |
| std.layout.repeat | repeat | [https://typst.app/docs/reference/layout/repeat/](https://typst.app/docs/reference/layout/repeat/) | 0.13.x |
| std.layout.rotate | rotate | [https://typst.app/docs/reference/layout/rotate/](https://typst.app/docs/reference/layout/rotate/) | 0.13.x |
| std.layout.scale | scale | [https://typst.app/docs/reference/layout/scale/](https://typst.app/docs/reference/layout/scale/) | 0.13.x |
| std.layout.skew | skew | [https://typst.app/docs/reference/layout/skew/](https://typst.app/docs/reference/layout/skew/) | 0.13.x |
| std.layout.hspace | h | [https://typst.app/docs/reference/layout/h/](https://typst.app/docs/reference/layout/h/) | 0.13.x |
| std.layout.vspace | v | [https://typst.app/docs/reference/layout/v/](https://typst.app/docs/reference/layout/v/) | 0.13.x |
| std.layout.stack | stack | [https://typst.app/docs/reference/layout/stack/](https://typst.app/docs/reference/layout/stack/) | 0.13.x |
| std.model.bibliography | bibliography | [https://typst.app/docs/reference/model/bibliography/](https://typst.app/docs/reference/model/bibliography/) | 0.13.x |
| std.model._bullet_list_item | list.item | [https://typst.app/docs/reference/model/list/#definitions-item](https://typst.app/docs/reference/model/list/#definitions-item) | 0.13.x |
| std.model.bullet_list | list | [https://typst.app/docs/reference/model/list/](https://typst.app/docs/reference/model/list/) | 0.13.x |
| std.model.cite | cite | [https://typst.app/docs/reference/model/cite/](https://typst.app/docs/reference/model/cite/) | 0.13.x |
| std.model.document | document | [https://typst.app/docs/reference/model/document/](https://typst.app/docs/reference/model/document/) | 0.13.x |
| std.model.emph | emph | [https://typst.app/docs/reference/model/emph/](https://typst.app/docs/reference/model/emph/) | 0.13.x |
| std.model._figure_caption | figure.caption | [https://typst.app/docs/reference/model/figure/#definitions-caption](https://typst.app/docs/reference/model/figure/#definitions-caption) | 0.13.x |
| std.model.figure | figure | [https://typst.app/docs/reference/model/figure/](https://typst.app/docs/reference/model/figure/) | 0.13.x |
| std.model._footnote_entry | footnote.entry | [https://typst.app/docs/reference/model/footnote/#definitions-entry](https://typst.app/docs/reference/model/footnote/#definitions-entry) | 0.13.x |
| std.model.footnote | footnote | [https://typst.app/docs/reference/model/footnote/](https://typst.app/docs/reference/model/footnote/) | 0.13.x |
| std.model.heading | heading | [https://typst.app/docs/reference/model/heading/](https://typst.app/docs/reference/model/heading/) | 0.13.x |
| std.model.link | link | [https://typst.app/docs/reference/model/link/](https://typst.app/docs/reference/model/link/) | 0.13.x |
| std.model._numbered_list_item | enum.item | [https://typst.app/docs/reference/model/enum/#definitions-item](https://typst.app/docs/reference/model/enum/#definitions-item) | 0.13.x |
| std.model.numbered_list | enum | [https://typst.app/docs/reference/model/enum/](https://typst.app/docs/reference/model/enum/) | 0.13.x |
| std.model.numbering | numbering | [https://typst.app/docs/reference/model/numbering/](https://typst.app/docs/reference/model/numbering/) | 0.13.x |
| std.model._outline_entry | outline.entry | [https://typst.app/docs/reference/model/outline/#definitions-entry](https://typst.app/docs/reference/model/outline/#definitions-entry) | 0.13.x |
| std.model._outline_indented | indented | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-indented) | 0.13.x |
| std.model._outline_prefix | prefix | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-prefix) | 0.13.x |
| std.model._outline_inner | inner | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-inner) | 0.13.x |
| std.model._outline_body | body | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-body) | 0.13.x |
| std.model._outline_page | page | [https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page](https://typst.app/docs/reference/model/outline/#definitions-entry-definitions-page) | 0.13.x |
| std.model.outline | outline | [https://typst.app/docs/reference/model/outline/](https://typst.app/docs/reference/model/outline/) | 0.13.x |
| std.model._par_line | par.line | [https://typst.app/docs/reference/model/par/#definitions-line](https://typst.app/docs/reference/model/par/#definitions-line) | 0.13.x |
| std.model.par | par | [https://typst.app/docs/reference/model/par/](https://typst.app/docs/reference/model/par/) | 0.13.x |
| std.model.parbreak | parbreak | [https://typst.app/docs/reference/model/parbreak/](https://typst.app/docs/reference/model/parbreak/) | 0.13.x |
| std.model.quote | quote | [https://typst.app/docs/reference/model/quote/](https://typst.app/docs/reference/model/quote/) | 0.13.x |
| std.model.ref | ref | [https://typst.app/docs/reference/model/ref/](https://typst.app/docs/reference/model/ref/) | 0.13.x |
| std.model.strong | strong | [https://typst.app/docs/reference/model/strong/](https://typst.app/docs/reference/model/strong/) | 0.13.x |
| std.model._table_cell | table.cell | [https://typst.app/docs/reference/model/table/#definitions-cell](https://typst.app/docs/reference/model/table/#definitions-cell) | 0.13.x |
| std.model._table_hline | table.hline | [https://typst.app/docs/reference/model/table/#definitions-hline](https://typst.app/docs/reference/model/table/#definitions-hline) | 0.13.x |
| std.model._table_vline | table.vline | [https://typst.app/docs/reference/model/table/#definitions-vline](https://typst.app/docs/reference/model/table/#definitions-vline) | 0.13.x |
| std.model._table_header | table.header | [https://typst.app/docs/reference/model/table/#definitions-header](https://typst.app/docs/reference/model/table/#definitions-header) | 0.13.x |
| std.model._table_footer | table.footer | [https://typst.app/docs/reference/model/table/#definitions-footer](https://typst.app/docs/reference/model/table/#definitions-footer) | 0.13.x |
| std.model.table | table | [https://typst.app/docs/reference/model/table/](https://typst.app/docs/reference/model/table/) | 0.13.x |
| std.model._terms_item | terms.item | [https://typst.app/docs/reference/model/terms/#definitions-item](https://typst.app/docs/reference/model/terms/#definitions-item) | 0.13.x |
| std.model.terms | terms | [https://typst.app/docs/reference/model/terms/](https://typst.app/docs/reference/model/terms/) | 0.13.x |
| subpar.grid | subpar.grid | [https://typst.app/universe/package/subpar](https://typst.app/universe/package/subpar) | None |

## Examples

`std.visualize.circle`:

```python
>>> circle('[Hello, world!]')
'#circle([Hello, world!])'
>>> circle('[Hello, world!]', radius='10pt')
'#circle([Hello, world!], radius: 10pt)'
>>> circle('[Hello, world!]', width='100%', height='100%')
'#circle([Hello, world!], width: 100%, height: 100%)'
```

`std.visualize._color_map`:

```python
>>> color.map('turbo')
'#color.map.turbo'
```

`std.visualize.luma`:

```python
>>> luma('50%')
'#luma(50%)'
>>> luma('50%', '50%')
'#luma(50%, 50%)'
```

`std.visualize.oklab`:

```python
>>> oklab('50%', '0%', '0%')
'#oklab(50%, 0%, 0%)'
>>> oklab('50%', '0%', '0%', '50%')
'#oklab(50%, 0%, 0%, 50%)'
```

`std.visualize.oklch`:

```python
>>> oklch('50%', '0%', '0deg')
'#oklch(50%, 0%, 0deg)'
>>> oklch('50%', '0%', '0deg', '50%')
'#oklch(50%, 0%, 0deg, 50%)'
```

`std.visualize._color_linear_rgb`:

```python
>>> color.linear_rgb(255, 255, 255)
'#color.linear-rgb(255, 255, 255)'
>>> color.linear_rgb('50%', '50%', '50%', '50%')
'#color.linear-rgb(50%, 50%, 50%, 50%)'
```

`std.visualize.rgb`:

```python
>>> rgb(255, 255, 255)
'#rgb(255, 255, 255)'
>>> rgb('50%', '50%', '50%', '50%')
'#rgb(50%, 50%, 50%, 50%)'
>>> rgb('"#ffffff"')
'#rgb("#ffffff")'
```

`std.visualize.cmyk`:

```python
>>> cmyk('0%', '0%', '0%', '0%')
'#cmyk(0%, 0%, 0%, 0%)'
>>> cmyk('50%', '50%', '50%', '50%')
'#cmyk(50%, 50%, 50%, 50%)'
```

`std.visualize._color_hsl`:

```python
>>> color.hsl('0deg', '50%', '50%', '50%')
'#color.hsl(0deg, 50%, 50%, 50%)'
>>> color.hsl('0deg', '50%', '50%')
'#color.hsl(0deg, 50%, 50%)'
```

`std.visualize._color_hsv`:

```python
>>> color.hsv('0deg', '50%', '50%', '50%')
'#color.hsv(0deg, 50%, 50%, 50%)'
>>> color.hsv('0deg', '50%', '50%')
'#color.hsv(0deg, 50%, 50%)'
```

`std.visualize._color_components`:

```python
>>> color.components(rgb(255, 255, 255))
'#rgb(255, 255, 255).components()'
```

`std.visualize._color_space`:

```python
>>> color.space(rgb(255, 255, 255))
'#rgb(255, 255, 255).space()'
```

`std.visualize._color_to_hex`:

```python
>>> color.to_hex(rgb(255, 255, 255))
'#rgb(255, 255, 255).to-hex()'
```

`std.visualize._color_lighten`:

```python
>>> color.lighten(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).lighten(50%)'
```

`std.visualize._color_darken`:

```python
>>> color.darken(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).darken(50%)'
```

`std.visualize._color_saturate`:

```python
>>> color.saturate(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).saturate(50%)'
```

`std.visualize._color_desaturate`:

```python
>>> color.desaturate(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).desaturate(50%)'
```

`std.visualize._color_negate`:

```python
>>> color.negate(rgb(255, 255, 255))
'#rgb(255, 255, 255).negate()'
>>> color.negate(rgb(255, 255, 255), space='oklch')
'#rgb(255, 255, 255).negate(space: oklch)'
```

`std.visualize._color_rotate`:

```python
>>> color.rotate(rgb(255, 255, 255), '90deg')
'#rgb(255, 255, 255).rotate(90deg)'
```

`std.visualize._color_mix`:

```python
>>> color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space='oklch')
'#color.mix(rgb(255, 255, 255), rgb(0, 0, 0), space: oklch)'
```

`std.visualize._color_transparentize`:

```python
>>> color.transparentize(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).transparentize(50%)'
```

`std.visualize._color_opacify`:

```python
>>> color.opacify(rgb(255, 255, 255), '50%')
'#rgb(255, 255, 255).opacify(50%)'
```

`std.visualize.color`:

```python
>>> color()
'#color'
```

`std.visualize._curve_move`:

```python
>>> curve.move(('10pt', '10pt'))
'#curve.move((10pt, 10pt))'
>>> curve.move(('10pt', '10pt'), relative=True)
'#curve.move((10pt, 10pt), relative: true)'
```

`std.visualize._curve_line`:

```python
>>> curve.line(('10pt', '10pt'))
'#curve.line((10pt, 10pt))'
>>> curve.line(('10pt', '10pt'), relative=True)
'#curve.line((10pt, 10pt), relative: true)'
```

`std.visualize._curve_quad`:

```python
>>> curve.quad(('10pt', '10pt'), ('20pt', '20pt'))
'#curve.quad((10pt, 10pt), (20pt, 20pt))'
>>> curve.quad(('10pt', '10pt'), ('20pt', '20pt'), relative=True)
'#curve.quad((10pt, 10pt), (20pt, 20pt), relative: true)'
```

`std.visualize._curve_cubic`:

```python
>>> curve.cubic(('10pt', '10pt'), ('20pt', '20pt'), ('30pt', '30pt'))
'#curve.cubic((10pt, 10pt), (20pt, 20pt), (30pt, 30pt))'
>>> curve.cubic(
...     ('10pt', '10pt'), ('20pt', '20pt'), ('30pt', '30pt'), relative=True
... )
'#curve.cubic((10pt, 10pt), (20pt, 20pt), (30pt, 30pt), relative: true)'
```

`std.visualize._curve_close`:

```python
>>> curve.close(mode='"smooth"')
'#curve.close()'
>>> curve.close(mode='"straight"')
'#curve.close(mode: "straight")'
```

`std.visualize.curve`:

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

`std.visualize.ellipse`:

```python
>>> ellipse('[Hello, World!]')
'#ellipse([Hello, World!])'
>>> ellipse('[Hello, World!]', width='100%')
'#ellipse([Hello, World!], width: 100%)'
```

`std.visualize._gradient_linear`:

```python
>>> gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))
'#gradient.linear(rgb(255, 255, 255), rgb(0, 0, 0))'
```

`std.visualize._gradient_radial`:

```python
>>> gradient.radial(
...     color.map('viridis'), focal_center=('10%', '40%'), focal_radius='5%'
... )
'#gradient.radial(..color.map.viridis, focal-center: (10%, 40%), focal-radius: 5%)'
```

`std.visualize._gradient_conic`:

```python
>>> gradient.conic(color.map('viridis'), angle='90deg', center=('10%', '40%'))
'#gradient.conic(..color.map.viridis, angle: 90deg, center: (10%, 40%))'
```

`std.visualize._gradient_sharp`:

```python
>>> gradient.sharp(gradient.linear(color.map('rainbow')), 5, smoothness='50%')
'#gradient.linear(..color.map.rainbow).sharp(5, smoothness: 50%)'
```

`std.visualize._gradient_repeat`:

```python
>>> gradient.repeat(gradient.radial('aqua', 'white'), 4, mirror=True)
'#gradient.radial(aqua, white).repeat(4, mirror: true)'
```

`std.visualize._gradient_kind`:

```python
>>> gradient.kind(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).kind()'
```

`std.visualize._gradient_stops`:

```python
>>> gradient.stops(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).stops()'
```

`std.visualize._gradient_space`:

```python
>>> gradient.space(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).space()'
```

`std.visualize._gradient_relative`:

```python
>>> gradient.relative(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).relative()'
```

`std.visualize._gradient_angle`:

```python
>>> gradient.angle(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).angle()'
```

`std.visualize._gradient_center`:

```python
>>> gradient.center(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).center()'
```

`std.visualize._gradient_radius`:

```python
>>> gradient.radius(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).radius()'
```

`std.visualize._gradient_focal_center`:

```python
>>> gradient.focal_center(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).focal-center()'
```

`std.visualize._gradient_focal_radius`:

```python
>>> gradient.focal_radius(gradient.linear('red', 'blue'))
'#gradient.linear(red, blue).focal-radius()'
```

`std.visualize.gradient`:

```python
>>> gradient()
'#gradient'
```

`std.visualize.image`:

```python
>>> image('"image.png"')
'#image("image.png")'
>>> image('"image.png"', fit='"contain"')
'#image("image.png", fit: "contain")'
```

`std.visualize.line`:

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

`std.visualize.tiling`:

```python
>>> from typstpy.std.layout import place
>>> tiling(
...     f'[{place(line(start=("0%", "0%"), end=("100%", "100%")))}, {place(line(start=("0%", "100%"), end=("100%", "0%")))}]',
...     size=('30pt', '30pt'),
... )
'#tiling([#place(line(start: (0%, 0%), end: (100%, 100%))), #place(line(start: (0%, 100%), end: (100%, 0%)))], size: (30pt, 30pt))'
```

`std.text.highlight`:

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

`std.text.linebreak`:

```python
>>> linebreak()
'#linebreak()'
>>> linebreak(justify=True)
'#linebreak(justify: true)'
```

`std.text.lorem`:

```python
>>> lorem(10)
'#lorem(10)'
```

`std.text.lower`:

```python
>>> lower('"Hello, World!"')
'#lower("Hello, World!")'
>>> lower('[Hello, World!]')
'#lower([Hello, World!])'
>>> lower(upper('"Hello, World!"'))
'#lower(upper("Hello, World!"))'
```

`std.text.overline`:

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

`std.text._raw_line`:

```python
>>> raw.line(1, 1, '"Hello, World!"', '"Hello, World!"')
'#raw.line(1, 1, "Hello, World!", "Hello, World!")'
```

`std.text.raw`:

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

`std.text.smallcaps`:

```python
>>> smallcaps('"Hello, World!"')
'#smallcaps("Hello, World!")'
>>> smallcaps('[Hello, World!]')
'#smallcaps([Hello, World!])'
>>> smallcaps('"Hello, World!"', all=True)
'#smallcaps("Hello, World!", all: true)'
```

`std.text.smartquote`:

```python
>>> smartquote(double=False, enabled=False, alternative=True, quotes='"()"')
'#smartquote(double: false, enabled: false, alternative: true, quotes: "()")'
>>> smartquote(quotes=('"()"', '"dict()"'))
'#smartquote(quotes: ("()", "dict()"))'
```

`std.text.strike`:

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

`std.text.subscript`:

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

`std.text.superscript`:

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

`std.text.text`:

```python
>>> text('"Hello, World!"')
'#text("Hello, World!")'
>>> text('[Hello, World!]')
'#text([Hello, World!])'
>>> text('[Hello, World!]', font='"Times New Roman"')
'#text([Hello, World!], font: "Times New Roman")'
```

`std.text.underline`:

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

`std.text.upper`:

```python
>>> upper('"Hello, World!"')
'#upper("Hello, World!")'
>>> upper('[Hello, World!]')
'#upper([Hello, World!])'
>>> upper(lower('"Hello, World!"'))
'#upper(lower("Hello, World!"))'
```

`std.layout.align`:

```python
>>> align('"Hello, World!"', 'center')
'#align("Hello, World!", center)'
>>> align('[Hello, World!]', 'center')
'#align([Hello, World!], center)'
>>> align(lorem(20), 'center')
'#align(lorem(20), center)'
```

`std.layout.block`:

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

`std.layout.box`:

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

`std.layout.colbreak`:

```python
>>> colbreak()
'#colbreak()'
>>> colbreak(weak=True)
'#colbreak(weak: true)'
```

`std.layout.columns`:

```python
>>> columns(lorem(20))
'#columns(lorem(20))'
>>> columns(lorem(20), 3)
'#columns(lorem(20), 3)'
>>> columns(lorem(20), 3, gutter='8% + 0pt')
'#columns(lorem(20), 3, gutter: 8% + 0pt)'
```

`std.layout._grid_cell`:

```python
>>> grid.cell(lorem(20), x=3, y=3)
'#grid.cell(lorem(20), x: 3, y: 3)'
```

`std.layout.grid`:

```python
>>> grid(lorem(20), lorem(20), lorem(20), align=('center',) * 3)
'#grid(align: (center, center, center), lorem(20), lorem(20), lorem(20))'
```

`std.layout.hide`:

```python
>>> hide(lorem(20))
'#hide(lorem(20))'
```

`std.layout.move`:

```python
>>> move(lorem(20), dx='50% + 10pt', dy='10% + 5pt')
'#move(lorem(20), dx: 50% + 10pt, dy: 10% + 5pt)'
```

`std.layout.pad`:

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

`std.layout.page`:

```python
>>> page(lorem(20))
'#page(lorem(20))'
>>> page(lorem(20), paper='"a0"', width='8.5in', height='11in')
'#page(lorem(20), paper: "a0", width: 8.5in, height: 11in)'
```

`std.layout.pagebreak`:

```python
>>> pagebreak()
'#pagebreak()'
>>> pagebreak(weak=True)
'#pagebreak(weak: true)'
>>> pagebreak(to='"even"')
'#pagebreak(to: "even")'
```

`std.layout._place_flush`:

```python
>>> place.flush()
'#place.flush()'
```

`std.layout.place`:

```python
>>> place(lorem(20))
'#place(lorem(20))'
>>> place(lorem(20), 'top')
'#place(lorem(20), top)'
```

`std.layout.repeat`:

```python
>>> repeat(lorem(20), gap='0.5em')
'#repeat(lorem(20), gap: 0.5em)'
>>> repeat(lorem(20), gap='0.5em', justify=False)
'#repeat(lorem(20), gap: 0.5em, justify: false)'
```

`std.layout.rotate`:

```python
>>> rotate(lorem(20), '20deg')
'#rotate(lorem(20), 20deg)'
>>> rotate(lorem(20), '20deg', origin='left + horizon')
'#rotate(lorem(20), 20deg, origin: left + horizon)'
```

`std.layout.scale`:

```python
>>> scale(lorem(20), '50%')
'#scale(lorem(20), 50%)'
>>> scale(lorem(20), x='50%', y='50%')
'#scale(lorem(20), x: 50%, y: 50%)'
>>> scale(lorem(20), '50%', x='50%', y='50%')
'#scale(lorem(20), 50%, x: 50%, y: 50%)'
```

`std.layout.skew`:

```python
>>> skew(lorem(20), ax='10deg', ay='20deg')
'#skew(lorem(20), ax: 10deg, ay: 20deg)'
>>> skew(
...     lorem(20), ax='10deg', ay='20deg', origin='left + horizon', reflow=True
... )
'#skew(lorem(20), ax: 10deg, ay: 20deg, origin: left + horizon, reflow: true)'
```

`std.layout.hspace`:

```python
>>> hspace('1em')
'#h(1em)'
>>> hspace('1em', weak=True)
'#h(1em, weak: true)'
```

`std.layout.vspace`:

```python
>>> vspace('1em')
'#v(1em)'
>>> vspace('1em', weak=True)
'#v(1em, weak: true)'
```

`std.layout.stack`:

```python
>>> stack(
...     rect(width='40pt'), rect(width='120pt'), rect(width='90pt'), dir='btt'
... )
'#stack(dir: btt, rect(width: 40pt), rect(width: 120pt), rect(width: 90pt))'
>>> stack(
...     (rect(width='40pt'), rect(width='120pt'), rect(width='90pt')), dir='btt'
... )
'#stack(dir: btt, ..(rect(width: 40pt), rect(width: 120pt), rect(width: 90pt)))'
```

`std.model.bibliography`:

```python
>>> bibliography('"bibliography.bib"', style='"cell"')
'#bibliography("bibliography.bib", style: "cell")'
```

`std.model._bullet_list_item`:

```python
>>> bullet_list.item('[Hello, World!]')
'#list.item([Hello, World!])'
```

`std.model.bullet_list`:

```python
>>> bullet_list(lorem(20), lorem(20), lorem(20))
'#list(lorem(20), lorem(20), lorem(20))'
>>> bullet_list(lorem(20), lorem(20), lorem(20), tight=False)
'#list(tight: false, lorem(20), lorem(20), lorem(20))'
```

`std.model.cite`:

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

`std.model.emph`:

```python
>>> emph('"Hello, World!"')
'#emph("Hello, World!")'
>>> emph('[Hello, World!]')
'#emph([Hello, World!])'
```

`std.model._figure_caption`:

```python
>>> figure.caption('[Hello, World!]')
'#figure.caption([Hello, World!])'
>>> figure.caption('[Hello, World!]', position='top', separator='[---]')
'#figure.caption([Hello, World!], position: top, separator: [---])'
```

`std.model.figure`:

```python
>>> figure(image('"image.png"'))
'#figure(image("image.png"))'
>>> figure(image('"image.png"'), caption='[Hello, World!]')
'#figure(image("image.png"), caption: [Hello, World!])'
```

`std.model.footnote`:

```python
>>> footnote('[Hello, World!]')
'#footnote([Hello, World!])'
>>> footnote('[Hello, World!]', numbering='"a"')
'#footnote([Hello, World!], numbering: "a")'
```

`std.model.heading`:

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

`std.model.link`:

```python
>>> link('"https://typst.app"')
'#link("https://typst.app")'
>>> link('"https://typst.app"', '"Typst"')
'#link("https://typst.app", "Typst")'
```

`std.model._numbered_list_item`:

```python
>>> numbered_list.item('[Hello, World!]', number=2)
'#enum.item([Hello, World!], number: 2)'
```

`std.model.numbered_list`:

```python
>>> numbered_list(lorem(20), lorem(20), lorem(20))
'#enum(lorem(20), lorem(20), lorem(20))'
>>> numbered_list(lorem(20), lorem(20), lorem(20), tight=False)
'#enum(tight: false, lorem(20), lorem(20), lorem(20))'
```

`std.model.numbering`:

```python
>>> numbering('"1.1)"', 1, 2)
'#numbering("1.1)", 1, 2)'
```

`std.model.outline`:

```python
>>> outline()
'#outline()'
>>> outline(title='"Hello, World!"', target=heading.where(outlined=True))
'#outline(title: "Hello, World!", target: heading.where(outlined: true))'
```

`std.model.par`:

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

`std.model.parbreak`:

```python
>>> parbreak()
'#parbreak()'
```

`std.model.quote`:

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

`std.model.ref`:

```python
>>> ref('<label>')
'#ref(<label>)'
>>> ref('<label>', supplement='[Hello, World!]')
'#ref(<label>, supplement: [Hello, World!])'
```

`std.model.strong`:

```python
>>> strong('"Hello, World!"')
'#strong("Hello, World!")'
>>> strong('[Hello, World!]', delta=400)
'#strong([Hello, World!], delta: 400)'
```

`std.model.table`:

```python
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

`std.model._terms_item`:

```python
>>> terms.item('"term"', '"description"')
'#terms.item("term", "description")'
```

`std.model.terms`:

```python
>>> terms(('[1]', lorem(20)), ('[1]', lorem(20)))
'#terms(([1], lorem(20)), ([1], lorem(20)))'
>>> terms(('[1]', lorem(20)), ('[1]', lorem(20)), tight=False)
'#terms(tight: false, ([1], lorem(20)), ([1], lorem(20)))'
>>> terms(terms.item('[1]', lorem(20)), terms.item('[1]', lorem(20)))
'#terms(terms.item([1], lorem(20)), terms.item([1], lorem(20)))'
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
