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

| Package's function name             | Typst's function name | Documentation on typst                                                                                                                                       |
| ----------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| std.visualize.circle                | circle                | [https://typst.app/docs/reference/visualize/circle/](https://typst.app/docs/reference/visualize/circle/)                                                     |
| std.visualize._color_map            | color.map             | [https://typst.app/docs/reference/visualize/color/#predefined-color-maps](https://typst.app/docs/reference/visualize/color/#predefined-color-maps)           |
| std.visualize.luma                  | luma                  | [https://typst.app/docs/reference/visualize/color/#definitions-luma](https://typst.app/docs/reference/visualize/color/#definitions-luma)                     |
| std.visualize.oklab                 | oklab                 | [https://typst.app/docs/reference/visualize/color/#definitions-oklab](https://typst.app/docs/reference/visualize/color/#definitions-oklab)                   |
| std.visualize.oklch                 | oklch                 | [https://typst.app/docs/reference/visualize/color/#definitions-oklch](https://typst.app/docs/reference/visualize/color/#definitions-oklch)                   |
| std.visualize._color_linear_rgb     | color.linear-rgb      | [https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb)         |
| std.visualize.rgb                   | rgb                   | [https://typst.app/docs/reference/visualize/color/#definitions-rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb)                       |
| std.visualize.cmyk                  | cmyk                  | [https://typst.app/docs/reference/visualize/color/#definitions-cmyk](https://typst.app/docs/reference/visualize/color/#definitions-cmyk)                     |
| std.visualize._color_hsl            | color.hsl             | [https://typst.app/docs/reference/visualize/color/#definitions-hsl](https://typst.app/docs/reference/visualize/color/#definitions-hsl)                       |
| std.visualize._color_hsv            | color.hsv             | [https://typst.app/docs/reference/visualize/color/#definitions-hsv](https://typst.app/docs/reference/visualize/color/#definitions-hsv)                       |
| std.visualize._color_components     | components            | [https://typst.app/docs/reference/visualize/color/#definitions-components](https://typst.app/docs/reference/visualize/color/#definitions-components)         |
| std.visualize._color_space          | space                 | [https://typst.app/docs/reference/visualize/color/#definitions-space](https://typst.app/docs/reference/visualize/color/#definitions-space)                   |
| std.visualize._color_to_hex         | to-hex                | [https://typst.app/docs/reference/visualize/color/#definitions-to-hex](https://typst.app/docs/reference/visualize/color/#definitions-to-hex)                 |
| std.visualize._color_lighten        | lighten               | [https://typst.app/docs/reference/visualize/color/#definitions-lighten](https://typst.app/docs/reference/visualize/color/#definitions-lighten)               |
| std.visualize._color_darken         | darken                | [https://typst.app/docs/reference/visualize/color/#definitions-darken](https://typst.app/docs/reference/visualize/color/#definitions-darken)                 |
| std.visualize._color_saturate       | saturate              | [https://typst.app/docs/reference/visualize/color/#definitions-saturate](https://typst.app/docs/reference/visualize/color/#definitions-saturate)             |
| std.visualize._color_desaturate     | desaturate            | [https://typst.app/docs/reference/visualize/color/#definitions-desaturate](https://typst.app/docs/reference/visualize/color/#definitions-desaturate)         |
| std.visualize._color_negate         | negate                | [https://typst.app/docs/reference/visualize/color/#definitions-negate](https://typst.app/docs/reference/visualize/color/#definitions-negate)                 |
| std.visualize._color_rotate         | rotate                | [https://typst.app/docs/reference/visualize/color/#definitions-rotate](https://typst.app/docs/reference/visualize/color/#definitions-rotate)                 |
| std.visualize._color_mix            | color.mix             | [https://typst.app/docs/reference/visualize/color/#definitions-mix](https://typst.app/docs/reference/visualize/color/#definitions-mix)                       |
| std.visualize._color_transparentize | transparentize        | [https://typst.app/docs/reference/visualize/color/#definitions-transparentize](https://typst.app/docs/reference/visualize/color/#definitions-transparentize) |
| std.visualize._color_opacify        | opacify               | [https://typst.app/docs/reference/visualize/color/#definitions-opacify](https://typst.app/docs/reference/visualize/color/#definitions-opacify)               |
| std.visualize.color                 | color                 | [https://typst.app/docs/reference/visualize/color/](https://typst.app/docs/reference/visualize/color/)                                                       |
| std.visualize.ellipse               | ellipse               | [https://typst.app/docs/reference/visualize/ellipse/](https://typst.app/docs/reference/visualize/ellipse/)                                                   |
| std.visualize._gradient_linear      | gradient.linear       | [https://typst.app/docs/reference/visualize/gradient/#definitions-linear](https://typst.app/docs/reference/visualize/gradient/#definitions-linear)           |
| std.visualize._gradient_radial      | gradient.radial       | [https://typst.app/docs/reference/visualize/gradient/#definitions-radial](https://typst.app/docs/reference/visualize/gradient/#definitions-radial)           |
| std.visualize._gradient_conic       | gradient.conic        | [https://typst.app/docs/reference/visualize/gradient/#definitions-conic](https://typst.app/docs/reference/visualize/gradient/#definitions-conic)             |
| std.visualize._gradient_sharp       | sharp                 | [https://typst.app/docs/reference/visualize/gradient/#definitions-sharp](https://typst.app/docs/reference/visualize/gradient/#definitions-sharp)             |
| std.visualize._gradient_repeat      | repeat                | [https://typst.app/docs/reference/visualize/gradient/#definitions-repeat](https://typst.app/docs/reference/visualize/gradient/#definitions-repeat)           |
| std.visualize._gradient_kind        | kind                  | [https://typst.app/docs/reference/visualize/gradient/#definitions-kind](https://typst.app/docs/reference/visualize/gradient/#definitions-kind)               |
| std.visualize._gradient_stops       | stops                 | [https://typst.app/docs/reference/visualize/gradient/#definitions-stops](https://typst.app/docs/reference/visualize/gradient/#definitions-stops)             |
| std.visualize._gradient_space       | space                 | [https://typst.app/docs/reference/visualize/gradient/#definitions-space](https://typst.app/docs/reference/visualize/gradient/#definitions-space)             |
| std.visualize._gradient_relative    | relative              | [https://typst.app/docs/reference/visualize/gradient/#definitions-relative](https://typst.app/docs/reference/visualize/gradient/#definitions-relative)       |
| std.visualize._gradient_angle       | angle                 | [https://typst.app/docs/reference/visualize/gradient/#definitions-angle](https://typst.app/docs/reference/visualize/gradient/#definitions-angle)             |
| std.visualize._gradient_sample      | sample                | [https://typst.app/docs/reference/visualize/gradient/#definitions-sample](https://typst.app/docs/reference/visualize/gradient/#definitions-sample)           |
| std.visualize._gradient_samples     | samples               | [https://typst.app/docs/reference/visualize/gradient/#definitions-samples](https://typst.app/docs/reference/visualize/gradient/#definitions-samples)         |
| std.visualize.gradient              | gradient              | [https://typst.app/docs/reference/visualize/gradient/](https://typst.app/docs/reference/visualize/gradient/)                                                 |
| std.visualize._image_decode         | image.decode          | [https://typst.app/docs/reference/visualize/image/#definitions-decode](https://typst.app/docs/reference/visualize/image/#definitions-decode)                 |
| std.visualize.image                 | image                 | [https://typst.app/docs/reference/visualize/image/](https://typst.app/docs/reference/visualize/image/)                                                       |
| std.visualize.line                  | line                  | [https://typst.app/docs/reference/visualize/line/](https://typst.app/docs/reference/visualize/line/)                                                         |
| std.visualize.path                  | path                  | [https://typst.app/docs/reference/visualize/path/](https://typst.app/docs/reference/visualize/path/)                                                         |
| std.visualize.pattern               | pattern               | [https://typst.app/docs/reference/visualize/pattern/](https://typst.app/docs/reference/visualize/pattern/)                                                   |
| std.visualize._polygon_regular      | polygon.regular       | [https://typst.app/docs/reference/visualize/polygon/#definitions-regular](https://typst.app/docs/reference/visualize/polygon/#definitions-regular)           |
| std.visualize.polygon               | polygon               | [https://typst.app/docs/reference/visualize/polygon/](https://typst.app/docs/reference/visualize/polygon/)                                                   |
| std.visualize.rect                  | rect                  | [https://typst.app/docs/reference/visualize/rect/](https://typst.app/docs/reference/visualize/rect/)                                                         |
| std.visualize.square                | square                | [https://typst.app/docs/reference/visualize/square/](https://typst.app/docs/reference/visualize/square/)                                                     |
| std.text.highlight                  | highlight             | [https://typst.app/docs/reference/text/highlight/](https://typst.app/docs/reference/text/highlight/)                                                         |
| std.text.linebreak                  | linebreak             | [https://typst.app/docs/reference/text/linebreak/](https://typst.app/docs/reference/text/linebreak/)                                                         |
| std.text.lorem                      | lorem                 | [https://typst.app/docs/reference/text/lorem/](https://typst.app/docs/reference/text/lorem/)                                                                 |
| std.text.lower                      | lower                 | [https://typst.app/docs/reference/text/lower/](https://typst.app/docs/reference/text/lower/)                                                                 |
| std.text.overline                   | overline              | [https://typst.app/docs/reference/text/overline/](https://typst.app/docs/reference/text/overline/)                                                           |
| std.text._raw_line                  | raw.line              | [https://typst.app/docs/reference/text/raw/#definitions-line](https://typst.app/docs/reference/text/raw/#definitions-line)                                   |
| std.text.raw                        | raw                   | [https://typst.app/docs/reference/text/raw/](https://typst.app/docs/reference/text/raw/)                                                                     |
| std.text.smallcaps                  | smallcaps             | [https://typst.app/docs/reference/text/smallcaps/](https://typst.app/docs/reference/text/smallcaps/)                                                         |
| std.text.smartquote                 | smartquote            | [https://typst.app/docs/reference/text/smartquote/](https://typst.app/docs/reference/text/smartquote/)                                                       |
| std.text.strike                     | strike                | [https://typst.app/docs/reference/text/strike/](https://typst.app/docs/reference/text/strike/)                                                               |
| std.text.subscript                  | sub                   | [https://typst.app/docs/reference/text/sub/](https://typst.app/docs/reference/text/sub/)                                                                     |
| std.text.superscript                | super                 | [https://typst.app/docs/reference/text/super/](https://typst.app/docs/reference/text/super/)                                                                 |
| std.text.text                       | text                  | [https://typst.app/docs/reference/text/text/](https://typst.app/docs/reference/text/text/)                                                                   |
| std.text.underline                  | underline             | [https://typst.app/docs/reference/text/underline/](https://typst.app/docs/reference/text/underline/)                                                         |
| std.text.upper                      | upper                 | [https://typst.app/docs/reference/text/upper/](https://typst.app/docs/reference/text/upper/)                                                                 |
| std.layout.align                    | align                 | [https://typst.app/docs/reference/layout/align/](https://typst.app/docs/reference/layout/align/)                                                             |
| std.layout.block                    | block                 | [https://typst.app/docs/reference/layout/block/](https://typst.app/docs/reference/layout/block/)                                                             |
| std.layout.box                      | box                   | [https://typst.app/docs/reference/layout/box/](https://typst.app/docs/reference/layout/box/)                                                                 |
| std.layout.colbreak                 | colbreak              | [https://typst.app/docs/reference/layout/colbreak/](https://typst.app/docs/reference/layout/colbreak/)                                                       |
| std.layout.columns                  | columns               | [https://typst.app/docs/reference/layout/columns/](https://typst.app/docs/reference/layout/columns/)                                                         |
| std.layout._grid_cell               | grid.cell             | [https://typst.app/docs/reference/layout/grid/#definitions-cell](https://typst.app/docs/reference/layout/grid/#definitions-cell)                             |
| std.layout._grid_hline              | grid.hline            | [https://typst.app/docs/reference/layout/grid/#definitions-hline](https://typst.app/docs/reference/layout/grid/#definitions-hline)                           |
| std.layout._grid_vline              | grid.vline            | [https://typst.app/docs/reference/layout/grid/#definitions-vline](https://typst.app/docs/reference/layout/grid/#definitions-vline)                           |
| std.layout._grid_header             | grid.header           | [https://typst.app/docs/reference/layout/grid/#definitions-header](https://typst.app/docs/reference/layout/grid/#definitions-header)                         |
| std.layout._grid_footer             | grid.footer           | [https://typst.app/docs/reference/layout/grid/#definitions-footer](https://typst.app/docs/reference/layout/grid/#definitions-footer)                         |
| std.layout.grid                     | grid                  | [https://typst.app/docs/reference/layout/grid/](https://typst.app/docs/reference/layout/grid/)                                                               |
| std.layout.hide                     | hide                  | [https://typst.app/docs/reference/layout/hide/](https://typst.app/docs/reference/layout/hide/)                                                               |
| std.layout.layout                   | layout                | [https://typst.app/docs/reference/layout/layout/](https://typst.app/docs/reference/layout/layout/)                                                           |
| std.layout.measure                  | measure               | [https://typst.app/docs/reference/layout/measure/](https://typst.app/docs/reference/layout/measure/)                                                         |
| std.layout.move                     | move                  | [https://typst.app/docs/reference/layout/move/](https://typst.app/docs/reference/layout/move/)                                                               |
| std.layout.padding                  | pad                   | [https://typst.app/docs/reference/layout/pad/](https://typst.app/docs/reference/layout/pad/)                                                                 |
| std.layout.pad                      | pad                   | [https://typst.app/docs/reference/layout/pad/](https://typst.app/docs/reference/layout/pad/)                                                                 |
| std.layout.page                     | page                  | [https://typst.app/docs/reference/layout/page/](https://typst.app/docs/reference/layout/page/)                                                               |
| std.layout.pagebreak                | pagebreak             | [https://typst.app/docs/reference/layout/pagebreak/](https://typst.app/docs/reference/layout/pagebreak/)                                                     |
| std.layout._place_flush             | place.flush           | [https://typst.app/docs/reference/layout/place/#definitions-flush](https://typst.app/docs/reference/layout/place/#definitions-flush)                         |
| std.layout.place                    | place                 | [https://typst.app/docs/reference/layout/place/](https://typst.app/docs/reference/layout/place/)                                                             |
| std.layout.repeat                   | repeat                | [https://typst.app/docs/reference/layout/repeat/](https://typst.app/docs/reference/layout/repeat/)                                                           |
| std.layout.rotate                   | rotate                | [https://typst.app/docs/reference/layout/rotate/](https://typst.app/docs/reference/layout/rotate/)                                                           |
| std.layout.scale                    | scale                 | [https://typst.app/docs/reference/layout/scale/](https://typst.app/docs/reference/layout/scale/)                                                             |
| std.layout.skew                     | skew                  | [https://typst.app/docs/reference/layout/skew/](https://typst.app/docs/reference/layout/skew/)                                                               |
| std.layout.hspace                   | h                     | [https://typst.app/docs/reference/layout/h/](https://typst.app/docs/reference/layout/h/)                                                                     |
| std.layout.vspace                   | v                     | [https://typst.app/docs/reference/layout/v/](https://typst.app/docs/reference/layout/v/)                                                                     |
| std.layout.stack                    | stack                 | [https://typst.app/docs/reference/layout/stack/](https://typst.app/docs/reference/layout/stack/)                                                             |
| std.model.bibliography              | bibliography          | [https://typst.app/docs/reference/model/bibliography/](https://typst.app/docs/reference/model/bibliography/)                                                 |
| std.model._bullet_list_item         | list.item             | [https://typst.app/docs/reference/model/list/#definitions-item](https://typst.app/docs/reference/model/list/#definitions-item)                               |
| std.model.bullet_list               | list                  | [https://typst.app/docs/reference/model/list/](https://typst.app/docs/reference/model/list/)                                                                 |
| std.model.cite                      | cite                  | [https://typst.app/docs/reference/model/cite/](https://typst.app/docs/reference/model/cite/)                                                                 |
| std.model.document                  | document              | [https://typst.app/docs/reference/model/document/](https://typst.app/docs/reference/model/document/)                                                         |
| std.model.emph                      | emph                  | [https://typst.app/docs/reference/model/emph/](https://typst.app/docs/reference/model/emph/)                                                                 |
| std.model._figure_caption           | figure.caption        | [https://typst.app/docs/reference/model/figure/#definitions-caption](https://typst.app/docs/reference/model/figure/#definitions-caption)                     |
| std.model.figure                    | figure                | [https://typst.app/docs/reference/model/figure/](https://typst.app/docs/reference/model/figure/)                                                             |
| std.model._footnote_entry           | footnote.entry        | [https://typst.app/docs/reference/model/footnote/#definitions-entry](https://typst.app/docs/reference/model/footnote/#definitions-entry)                     |
| std.model.footnote                  | footnote              | [https://typst.app/docs/reference/model/footnote/](https://typst.app/docs/reference/model/footnote/)                                                         |
| std.model.heading                   | heading               | [https://typst.app/docs/reference/model/heading/](https://typst.app/docs/reference/model/heading/)                                                           |
| std.model.link                      | link                  | [https://typst.app/docs/reference/model/link/](https://typst.app/docs/reference/model/link/)                                                                 |
| std.model._numbered_list_item       | enum.item             | [https://typst.app/docs/reference/model/enum/#definitions-item](https://typst.app/docs/reference/model/enum/#definitions-item)                               |
| std.model.numbered_list             | enum                  | [https://typst.app/docs/reference/model/enum/](https://typst.app/docs/reference/model/enum/)                                                                 |
| std.model.numbering                 | numbering             | [https://typst.app/docs/reference/model/numbering/](https://typst.app/docs/reference/model/numbering/)                                                       |
| std.model._outline_entry            | outline.entry         | [https://typst.app/docs/reference/model/outline/#definitions-entry](https://typst.app/docs/reference/model/outline/#definitions-entry)                       |
| std.model.outline                   | outline               | [https://typst.app/docs/reference/model/outline/](https://typst.app/docs/reference/model/outline/)                                                           |
| std.model._par_line                 | par.line              | [https://typst.app/docs/reference/model/par/#definitions-line](https://typst.app/docs/reference/model/par/#definitions-line)                                 |
| std.model.par                       | par                   | [https://typst.app/docs/reference/model/par/](https://typst.app/docs/reference/model/par/)                                                                   |
| std.model.parbreak                  | parbreak              | [https://typst.app/docs/reference/model/parbreak/](https://typst.app/docs/reference/model/parbreak/)                                                         |
| std.model.quote                     | quote                 | [https://typst.app/docs/reference/model/quote/](https://typst.app/docs/reference/model/quote/)                                                               |
| std.model.ref                       | ref                   | [https://typst.app/docs/reference/model/ref/](https://typst.app/docs/reference/model/ref/)                                                                   |
| std.model.strong                    | strong                | [https://typst.app/docs/reference/model/strong/](https://typst.app/docs/reference/model/strong/)                                                             |
| std.model._table_cell               | table.cell            | [https://typst.app/docs/reference/model/table/#definitions-cell](https://typst.app/docs/reference/model/table/#definitions-cell)                             |
| std.model._table_hline              | table.hline           | [https://typst.app/docs/reference/model/table/#definitions-hline](https://typst.app/docs/reference/model/table/#definitions-hline)                           |
| std.model._table_vline              | table.vline           | [https://typst.app/docs/reference/model/table/#definitions-vline](https://typst.app/docs/reference/model/table/#definitions-vline)                           |
| std.model._table_header             | table.header          | [https://typst.app/docs/reference/model/table/#definitions-header](https://typst.app/docs/reference/model/table/#definitions-header)                         |
| std.model._table_footer             | table.footer          | [https://typst.app/docs/reference/model/table/#definitions-footer](https://typst.app/docs/reference/model/table/#definitions-footer)                         |
| std.model.table                     | table                 | [https://typst.app/docs/reference/model/table/](https://typst.app/docs/reference/model/table/)                                                               |
| std.model._terms_item               | terms.item            | [https://typst.app/docs/reference/model/terms/#definitions-item](https://typst.app/docs/reference/model/terms/#definitions-item)                             |
| std.model.terms                     | terms                 | [https://typst.app/docs/reference/model/terms/](https://typst.app/docs/reference/model/terms/)                                                               |
| subpar.grid                         | subpar.grid           | [https://typst.app/universe/package/subpar](https://typst.app/universe/package/subpar)                                                                       |

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
>>> path(('0%', '0%'), ('100%', '0%'), ('100%', '100%'), ('0%', '100%'), fill='red')
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
```

`std.text.smartquote`:

```python
>>> smartquote(double=False, enabled=False, alternative=True, quotes='"()"')
'#smartquote(double: false, enabled: false, alternative: true, quotes: "()")'
>>> smartquote(quotes=('"()"', '"{}"'))
'#smartquote(quotes: ("()", "{}"))'
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
>>> subscript('[Hello, World!]', typographic=False, baseline='0.3em', size='0.7em')
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

`std.layout.padding`:

```python
>>> padding(
...     lorem(20),
...     left='4% + 0pt',
...     top='4% + 0pt',
...     right='4% + 0pt',
...     bottom='4% + 0pt',
... )
'#pad(lorem(20), left: 4% + 0pt, top: 4% + 0pt, right: 4% + 0pt, bottom: 4% + 0pt)'

.. deprecated:: 1.0.2
The function will be removed since version 1.1.x. Use `pad`
instead.
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
>>> stack(rect(width='40pt'), rect(width='120pt'), rect(width='90pt'), dir='btt')
'#stack(dir: btt, rect(width: 40pt), rect(width: 120pt), rect(width: 90pt))'
>>> stack((rect(width='40pt'), rect(width='120pt'), rect(width='90pt')), dir='btt')
'#stack(dir: btt, ..(rect(width: 40pt), rect(width: 120pt), rect(width: 90pt)))'
```

`std.model.bibliography`:

```python
>>> bibliography('"bibliography.bib"', style='"cell"')
'#bibliography("bibliography.bib", style: "cell")'
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
>>> outline(title='"Hello, World!"', target=heading.where(outlined=False))
'#outline(title: "Hello, World!", target: heading.where(outlined: false))'
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
