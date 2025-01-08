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

## Installation

```bash
pip install typstpy
```

## Current Supports

| Package's function name | Typst's function name | Documentation on typst |
| --- | --- | --- |
| align | align | [https://typst.app/docs/reference/layout/align/](https://typst.app/docs/reference/layout/align/) |
| bibliography | bibliography | [https://typst.app/docs/reference/model/bibliography/](https://typst.app/docs/reference/model/bibliography/) |
| block | block | [https://typst.app/docs/reference/layout/block/](https://typst.app/docs/reference/layout/block/) |
| box | box | [https://typst.app/docs/reference/layout/box/](https://typst.app/docs/reference/layout/box/) |
| bullet_list | list | [https://typst.app/docs/reference/model/list/](https://typst.app/docs/reference/model/list/) |
| circle | circle | [https://typst.app/docs/reference/visualize/circle/](https://typst.app/docs/reference/visualize/circle/) |
| cite | cite | [https://typst.app/docs/reference/model/cite/](https://typst.app/docs/reference/model/cite/) |
| cmyk | cmyk | [https://typst.app/docs/reference/visualize/color/#definitions-cmyk](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) |
| colbreak | colbreak | [https://typst.app/docs/reference/layout/colbreak/](https://typst.app/docs/reference/layout/colbreak/) |
| color | color | [https://typst.app/docs/reference/visualize/color/](https://typst.app/docs/reference/visualize/color/) |
| columns | columns | [https://typst.app/docs/reference/layout/columns/](https://typst.app/docs/reference/layout/columns/) |
| document | document | [https://typst.app/docs/reference/model/document/](https://typst.app/docs/reference/model/document/) |
| ellipse | ellipse | [https://typst.app/docs/reference/visualize/ellipse/](https://typst.app/docs/reference/visualize/ellipse/) |
| emph | emph | [https://typst.app/docs/reference/model/emph/](https://typst.app/docs/reference/model/emph/) |
| figure | figure | [https://typst.app/docs/reference/model/figure/](https://typst.app/docs/reference/model/figure/) |
| footnote | footnote | [https://typst.app/docs/reference/model/footnote/](https://typst.app/docs/reference/model/footnote/) |
| gradient | gradient | [https://typst.app/docs/reference/visualize/gradient/](https://typst.app/docs/reference/visualize/gradient/) |
| grid | grid | [https://typst.app/docs/reference/layout/grid/](https://typst.app/docs/reference/layout/grid/) |
| heading | heading | [https://typst.app/docs/reference/model/heading/](https://typst.app/docs/reference/model/heading/) |
| hide | hide | [https://typst.app/docs/reference/layout/hide/](https://typst.app/docs/reference/layout/hide/) |
| highlight | highlight | [https://typst.app/docs/reference/text/highlight/](https://typst.app/docs/reference/text/highlight/) |
| hspace | h | [https://typst.app/docs/reference/layout/h/](https://typst.app/docs/reference/layout/h/) |
| image | image | [https://typst.app/docs/reference/visualize/image/](https://typst.app/docs/reference/visualize/image/) |
| layout | layout | [https://typst.app/docs/reference/layout/layout/](https://typst.app/docs/reference/layout/layout/) |
| line | line | [https://typst.app/docs/reference/visualize/line/](https://typst.app/docs/reference/visualize/line/) |
| linebreak | linebreak | [https://typst.app/docs/reference/text/linebreak/](https://typst.app/docs/reference/text/linebreak/) |
| link | link | [https://typst.app/docs/reference/model/link/](https://typst.app/docs/reference/model/link/) |
| lorem | lorem | [https://typst.app/docs/reference/text/lorem/](https://typst.app/docs/reference/text/lorem/) |
| lower | lower | [https://typst.app/docs/reference/text/lower/](https://typst.app/docs/reference/text/lower/) |
| luma | luma | [https://typst.app/docs/reference/visualize/color/#definitions-luma](https://typst.app/docs/reference/visualize/color/#definitions-luma) |
| measure | measure | [https://typst.app/docs/reference/layout/measure/](https://typst.app/docs/reference/layout/measure/) |
| move | move | [https://typst.app/docs/reference/layout/move/](https://typst.app/docs/reference/layout/move/) |
| numbered_list | enum | [https://typst.app/docs/reference/model/enum/](https://typst.app/docs/reference/model/enum/) |
| numbering | numbering | [https://typst.app/docs/reference/model/numbering/](https://typst.app/docs/reference/model/numbering/) |
| oklab | oklab | [https://typst.app/docs/reference/visualize/color/#definitions-oklab](https://typst.app/docs/reference/visualize/color/#definitions-oklab) |
| oklch | oklch | [https://typst.app/docs/reference/visualize/color/#definitions-oklch](https://typst.app/docs/reference/visualize/color/#definitions-oklch) |
| outline | outline | [https://typst.app/docs/reference/model/outline/](https://typst.app/docs/reference/model/outline/) |
| overline | overline | [https://typst.app/docs/reference/text/overline/](https://typst.app/docs/reference/text/overline/) |
| padding | pad | [https://typst.app/docs/reference/layout/pad/](https://typst.app/docs/reference/layout/pad/) |
| page | page | [https://typst.app/docs/reference/layout/page/](https://typst.app/docs/reference/layout/page/) |
| pagebreak | pagebreak | [https://typst.app/docs/reference/layout/pagebreak/](https://typst.app/docs/reference/layout/pagebreak/) |
| par | par | [https://typst.app/docs/reference/model/par/](https://typst.app/docs/reference/model/par/) |
| parbreak | parbreak | [https://typst.app/docs/reference/model/parbreak/](https://typst.app/docs/reference/model/parbreak/) |
| path | path | [https://typst.app/docs/reference/visualize/path/](https://typst.app/docs/reference/visualize/path/) |
| pattern | pattern | [https://typst.app/docs/reference/visualize/pattern/](https://typst.app/docs/reference/visualize/pattern/) |
| place | place | [https://typst.app/docs/reference/layout/place/](https://typst.app/docs/reference/layout/place/) |
| polygon | polygon | [https://typst.app/docs/reference/visualize/polygon/](https://typst.app/docs/reference/visualize/polygon/) |
| quote | quote | [https://typst.app/docs/reference/model/quote/](https://typst.app/docs/reference/model/quote/) |
| raw | raw | [https://typst.app/docs/reference/text/raw/](https://typst.app/docs/reference/text/raw/) |
| rect | rect | [https://typst.app/docs/reference/visualize/rect/](https://typst.app/docs/reference/visualize/rect/) |
| ref | ref | [https://typst.app/docs/reference/model/ref/](https://typst.app/docs/reference/model/ref/) |
| repeat | repeat | [https://typst.app/docs/reference/layout/repeat/](https://typst.app/docs/reference/layout/repeat/) |
| rgb | rgb | [https://typst.app/docs/reference/visualize/color/#definitions-rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb) |
| rotate | rotate | [https://typst.app/docs/reference/layout/rotate/](https://typst.app/docs/reference/layout/rotate/) |
| scale | scale | [https://typst.app/docs/reference/layout/scale/](https://typst.app/docs/reference/layout/scale/) |
| skew | skew | [https://typst.app/docs/reference/layout/skew/](https://typst.app/docs/reference/layout/skew/) |
| smallcaps | smallcaps | [https://typst.app/docs/reference/text/smallcaps/](https://typst.app/docs/reference/text/smallcaps/) |
| smartquote | smartquote | [https://typst.app/docs/reference/text/smartquote/](https://typst.app/docs/reference/text/smartquote/) |
| square | square | [https://typst.app/docs/reference/visualize/square/](https://typst.app/docs/reference/visualize/square/) |
| stack | stack | [https://typst.app/docs/reference/layout/stack/](https://typst.app/docs/reference/layout/stack/) |
| strike | strike | [https://typst.app/docs/reference/text/strike/](https://typst.app/docs/reference/text/strike/) |
| strong | strong | [https://typst.app/docs/reference/model/strong/](https://typst.app/docs/reference/model/strong/) |
| subscript | sub | [https://typst.app/docs/reference/text/sub/](https://typst.app/docs/reference/text/sub/) |
| superscript | super | [https://typst.app/docs/reference/text/super/](https://typst.app/docs/reference/text/super/) |
| table | table | [https://typst.app/docs/reference/model/table/](https://typst.app/docs/reference/model/table/) |
| terms | terms | [https://typst.app/docs/reference/model/terms/](https://typst.app/docs/reference/model/terms/) |
| text | text | [https://typst.app/docs/reference/text/text/](https://typst.app/docs/reference/text/text/) |
| underline | underline | [https://typst.app/docs/reference/text/underline/](https://typst.app/docs/reference/text/underline/) |
| upper | upper | [https://typst.app/docs/reference/text/upper/](https://typst.app/docs/reference/text/upper/) |
| vspace | v | [https://typst.app/docs/reference/layout/v/](https://typst.app/docs/reference/layout/v/) |

## Change logs

- _1.0.2_: Improved type annotations.
- _1.0.1_: Implement `set`, `show`, and `import`.
- _1.0.0_: Completed documentation and test cases in `layout`, `model`, `text` and `visualize` modules. Improved functionality.
- _1.0.0-beta.2_: Improved the implementation and documentation of functions in the `layout` module.
- _1.0.0-beta.1_: Completely reconstructed the underlying implementation.

## Examples

```python
from typstpy.std import *
```

`align`:

```python
>>> align('"Hello, World!"', 'center')
'#align("Hello, World!", center)'
>>> align('[Hello, World!]', 'center')
'#align([Hello, World!], center)'
>>> align(lorem(20), 'center')
'#align(lorem(20), center)'
```

`bibliography`:

```python
>>> bibliography('"bibliography.bib"', style='"cell"')
'#bibliography("bibliography.bib", style: "cell")'
```

`block`:

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

`box`:

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

`bullet_list`:

```python
>>> bullet_list(lorem(20), lorem(20), lorem(20))
'#list(lorem(20), lorem(20), lorem(20))'
>>> bullet_list(lorem(20), lorem(20), lorem(20), tight=False)
'#list(tight: false, lorem(20), lorem(20), lorem(20))'
```

`circle`:

```python
>>> circle('[Hello, world!]')
'#circle([Hello, world!])'
>>> circle('[Hello, world!]', radius='10pt')
'#circle([Hello, world!], radius: 10pt)'
>>> circle('[Hello, world!]', width='100%', height='100%')
'#circle([Hello, world!], width: 100%, height: 100%)'
```

`cite`:

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

`cmyk`:

```python
>>> cmyk('0%', '0%', '0%', '0%')
'#cmyk(0%, 0%, 0%, 0%)'
>>> cmyk('50%', '50%', '50%', '50%')
'#cmyk(50%, 50%, 50%, 50%)'
```

`colbreak`:

```python
>>> colbreak()
'#colbreak()'
>>> colbreak(weak=True)
'#colbreak(weak: true)'
```

`color`:

```python
>>> color()
'#color'
```

`columns`:

```python
>>> columns(lorem(20))
'#columns(lorem(20))'
>>> columns(lorem(20), 3)
'#columns(lorem(20), 3)'
>>> columns(lorem(20), 3, gutter='8% + 0pt')
'#columns(lorem(20), 3, gutter: 8% + 0pt)'
```

`ellipse`:

```python
>>> ellipse('[Hello, World!]')
'#ellipse([Hello, World!])'
>>> ellipse('[Hello, World!]', width='100%')
'#ellipse([Hello, World!], width: 100%)'
```

`emph`:

```python
>>> emph('"Hello, World!"')
'#emph("Hello, World!")'
>>> emph('[Hello, World!]')
'#emph([Hello, World!])'
```

`figure`:

```python
>>> figure(image('"image.png"'))
'#figure(image("image.png"))'
>>> figure(image('"image.png"'), caption='[Hello, World!]')
'#figure(image("image.png"), caption: [Hello, World!])'
```

`footnote`:

```python
>>> footnote('[Hello, World!]')
'#footnote([Hello, World!])'
>>> footnote('[Hello, World!]', numbering='"a"')
'#footnote([Hello, World!], numbering: "a")'
```

`gradient`:

```python
>>> gradient()
'#gradient'
```

`grid`:

```python
>>> grid(lorem(20), lorem(20), lorem(20), align=('center',) * 3)
'#grid(align: (center, center, center), lorem(20), lorem(20), lorem(20))'
```

`heading`:

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

`hide`:

```python
>>> hide(lorem(20))
'#hide(lorem(20))'
```

`highlight`:

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

`hspace`:

```python
>>> hspace('1em')
'#h(1em)'
>>> hspace('1em', weak=True)
'#h(1em, weak: true)'
```

`image`:

```python
>>> image('"image.png"')
'#image("image.png")'
>>> image('"image.png"', fit='"contain"')
'#image("image.png", fit: "contain")'
```

`line`:

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

`linebreak`:

```python
>>> linebreak()
'#linebreak()'
>>> linebreak(justify=True)
'#linebreak(justify: true)'
```

`link`:

```python
>>> link('"https://typst.app"')
'#link("https://typst.app")'
>>> link('"https://typst.app"', '"Typst"')
'#link("https://typst.app", "Typst")'
```

`lorem`:

```python
>>> lorem(10)
'#lorem(10)'
```

`lower`:

```python
>>> lower('"Hello, World!"')
'#lower("Hello, World!")'
>>> lower('[Hello, World!]')
'#lower([Hello, World!])'
>>> lower(upper('"Hello, World!"'))
'#lower(upper("Hello, World!"))'
```

`luma`:

```python
>>> luma('50%')
'#luma(50%)'
>>> luma('50%', '50%')
'#luma(50%, 50%)'
```

`move`:

```python
>>> move(lorem(20), dx='50% + 10pt', dy='10% + 5pt')
'#move(lorem(20), dx: 50% + 10pt, dy: 10% + 5pt)'
```

`numbered_list`:

```python
>>> numbered_list(lorem(20), lorem(20), lorem(20))
'#enum(lorem(20), lorem(20), lorem(20))'
>>> numbered_list(lorem(20), lorem(20), lorem(20), tight=False)
'#enum(tight: false, lorem(20), lorem(20), lorem(20))'
```

`numbering`:

```python
>>> numbering('"1.1)"', 1, 2)
'#numbering("1.1)", 1, 2)'
```

`oklab`:

```python
>>> oklab('50%', '0%', '0%')
'#oklab(50%, 0%, 0%)'
>>> oklab('50%', '0%', '0%', '50%')
'#oklab(50%, 0%, 0%, 50%)'
```

`oklch`:

```python
>>> oklch('50%', '0%', '0deg')
'#oklch(50%, 0%, 0deg)'
>>> oklch('50%', '0%', '0deg', '50%')
'#oklch(50%, 0%, 0deg, 50%)'
```

`outline`:

```python
>>> outline()
'#outline()'
>>> outline(title='"Hello, World!"', target=heading.where(outlined=False))
'#outline(title: "Hello, World!", target: heading.where(outlined: false))'
```

`overline`:

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

`padding`:

```python
>>> padding(
...     lorem(20),
...     left='4% + 0pt',
...     top='4% + 0pt',
...     right='4% + 0pt',
...     bottom='4% + 0pt',
... )
'#pad(lorem(20), left: 4% + 0pt, top: 4% + 0pt, right: 4% + 0pt, bottom: 4% + 0pt)'
```

`page`:

```python
>>> page(lorem(20))
'#page(lorem(20))'
>>> page(lorem(20), paper='"a0"', width='8.5in', height='11in')
'#page(lorem(20), paper: "a0", width: 8.5in, height: 11in)'
```

`pagebreak`:

```python
>>> pagebreak()
'#pagebreak()'
>>> pagebreak(weak=True)
'#pagebreak(weak: true)'
>>> pagebreak(to='"even"')
'#pagebreak(to: "even")'
```

`par`:

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

`parbreak`:

```python
>>> parbreak()
'#parbreak()'
```

`path`:

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

`place`:

```python
>>> place(lorem(20))
'#place(lorem(20))'
>>> place(lorem(20), 'top')
'#place(lorem(20), top)'
```

`quote`:

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

`raw`:

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

`ref`:

```python
>>> ref('<label>')
'#ref(<label>)'
>>> ref('<label>', supplement='[Hello, World!]')
'#ref(<label>, supplement: [Hello, World!])'
```

`repeat`:

```python
>>> repeat(lorem(20), gap='0.5em')
'#repeat(lorem(20), gap: 0.5em)'
>>> repeat(lorem(20), gap='0.5em', justify=False)
'#repeat(lorem(20), gap: 0.5em, justify: false)'
```

`rgb`:

```python
>>> rgb(255, 255, 255)
'#rgb(255, 255, 255)'
>>> rgb('50%', '50%', '50%', '50%')
'#rgb(50%, 50%, 50%, 50%)'
>>> rgb('"#ffffff"')
'#rgb("#ffffff")'
```

`rotate`:

```python
>>> rotate(lorem(20), '20deg')
'#rotate(lorem(20), 20deg)'
>>> rotate(lorem(20), '20deg', origin='left + horizon')
'#rotate(lorem(20), 20deg, origin: left + horizon)'
```

`scale`:

```python
>>> scale(lorem(20), '50%')
'#scale(lorem(20), 50%)'
>>> scale(lorem(20), x='50%', y='50%')
'#scale(lorem(20), x: 50%, y: 50%)'
>>> scale(lorem(20), '50%', x='50%', y='50%')
'#scale(lorem(20), 50%, x: 50%, y: 50%)'
```

`skew`:

```python
>>> skew(lorem(20), ax='10deg', ay='20deg')
'#skew(lorem(20), ax: 10deg, ay: 20deg)'
```

`smallcaps`:

```python
>>> smallcaps('"Hello, World!"')
'#smallcaps("Hello, World!")'
>>> smallcaps('[Hello, World!]')
'#smallcaps([Hello, World!])'
```

`smartquote`:

```python
>>> smartquote(double=False, enabled=False, alternative=True, quotes='"()"')
'#smartquote(double: false, enabled: false, alternative: true, quotes: "()")'
>>> smartquote(quotes=('"()"', '"{}"'))
'#smartquote(quotes: ("()", "{}"))'
```

`stack`:

```python
>>> stack(rect(width='40pt'), rect(width='120pt'), rect(width='90pt'), dir='btt')
'#stack(dir: btt, rect(width: 40pt), rect(width: 120pt), rect(width: 90pt))'
>>> stack((rect(width='40pt'), rect(width='120pt'), rect(width='90pt')), dir='btt')
'#stack(dir: btt, ..(rect(width: 40pt), rect(width: 120pt), rect(width: 90pt)))'
```

`strike`:

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

`strong`:

```python
>>> strong('"Hello, World!"')
'#strong("Hello, World!")'
>>> strong('[Hello, World!]', delta=400)
'#strong([Hello, World!], delta: 400)'
```

`subscript`:

```python
>>> subscript('"Hello, World!"')
'#sub("Hello, World!")'
>>> subscript('[Hello, World!]')
'#sub([Hello, World!])'
>>> subscript('[Hello, World!]', typographic=False, baseline='0.3em', size='0.7em')
'#sub([Hello, World!], typographic: false, baseline: 0.3em, size: 0.7em)'
```

`superscript`:

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

`table`:

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

`terms`:

```python
>>> terms(('[1]', lorem(20)), ('[1]', lorem(20)))
'#terms(([1], lorem(20)), ([1], lorem(20)))'
>>> terms(('[1]', lorem(20)), ('[1]', lorem(20)), tight=False)
'#terms(tight: false, ([1], lorem(20)), ([1], lorem(20)))'
>>> terms(terms.item('[1]', lorem(20)), terms.item('[1]', lorem(20)))
'#terms(terms.item([1], lorem(20)), terms.item([1], lorem(20)))'
```

`text`:

```python
>>> text('"Hello, World!"')
'#text("Hello, World!")'
>>> text('[Hello, World!]')
'#text([Hello, World!])'
>>> text('[Hello, World!]', font='"Times New Roman"')
'#text([Hello, World!], font: "Times New Roman")'
```

`underline`:

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

`upper`:

```python
>>> upper('"Hello, World!"')
'#upper("Hello, World!")'
>>> upper('[Hello, World!]')
'#upper([Hello, World!])'
>>> upper(lower('"Hello, World!"'))
'#upper(lower("Hello, World!"))'
```

`vspace`:

```python
>>> vspace('1em')
'#v(1em)'
>>> vspace('1em', weak=True)
'#v(1em, weak: true)'
```
