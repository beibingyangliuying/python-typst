# python-typst

`python-typst` is a library for generating executable typst code (See [typst repository](https://github.com/typst/typst) and [typst documentation](https://typst.app/docs/) for more information).
It is written primarily in functional programming paradigm with some OOP content.
Each module has greater than 90% unit test coverage.

This package provides the interfaces in a way that is as close as possible to typst's native functions.
Through `python-typst` and other data processing packages, you can generate data reports quickly.

Repository on GitHub: [python-typst](https://github.com/beibingyangliuying/python-typst).
Homepage on PyPI: [python-typst](https://pypi.org/project/typstpy/).
Contributions are welcome.

## Installation

```bash
pip install typstpy
```

## Current Support

| Is Standard | Function Name | Original Name | Documentation |
| --- | --- | --- | --- |
| True | _color_hsl | color.hsl | [color.hsl](https://typst.app/docs/reference/visualize/color/#definitions-hsl) |
| True | _color_linear_rgb | color.linear-rgb | [color.linear-rgb](https://typst.app/docs/reference/visualize/color/#definitions-linear-rgb) |
| True | _figure_caption | figure.caption | [figure.caption](https://typst.app/docs/reference/model/figure/#definitions-caption) |
| True | bibliography | bibliography | [bibliography](https://typst.app/docs/reference/model/bibliography/) |
| True | cite | cite | [cite](https://typst.app/docs/reference/model/cite/) |
| True | cmyk | cmyk | [cmyk](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) |
| False | color | None | [None](None) |
| True | emph | emph | [emph](https://typst.app/docs/reference/model/emph/) |
| True | figure | figure | [figure](https://typst.app/docs/reference/model/figure/) |
| True | footnote | footnote | [footnote](https://typst.app/docs/reference/model/footnote/) |
| True | heading | heading | [heading](https://typst.app/docs/reference/model/heading/) |
| True | image | image | [image](https://typst.app/docs/reference/visualize/image/) |
| True | link | link | [link](https://typst.app/docs/reference/model/link/) |
| True | lorem | lorem | [lorem](https://typst.app/docs/reference/text/lorem/) |
| True | luma | luma | [luma](https://typst.app/docs/reference/visualize/color/#definitions-luma) |
| True | pagebreak | pagebreak | [pagebreak](https://typst.app/docs/reference/layout/pagebreak/) |
| True | par | par | [par](https://typst.app/docs/reference/model/par/) |
| True | ref | ref | [ref](https://typst.app/docs/reference/model/ref/) |
| True | rgb | rgb | [rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb) |
| True | strong | strong | [strong](https://typst.app/docs/reference/model/strong/) |
| True | text | text | [text](https://typst.app/docs/reference/text/text/) |

## Examples

To be continued.
