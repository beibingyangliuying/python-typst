# typstpy

`typstpy` is a library for generating executable [typst](https://typst.app/docs/) code.
This package is written primarily in functional programming paradigm with some OOP contents.
Each module has greater than 90% unit test coverage.

This package provides the interfaces in a way that is as close as possible to typst's native functions.
Through `typstpy` and other data processing packages, you can generate data reports quickly.

Repository on GitHub: [python-typst](https://github.com/beibingyangliuying/python-typst).
Homepage on PyPI: [python-typst](https://pypi.org/project/typstpy/).
Any contributions are welcome.

## Installation

```bash
pip install typstpy
```

## Current Support

| Is Standard | Function Name | Original Name | Documentation |
| --- | --- | --- | --- |
| True | align | align | [align](https://typst.app/docs/reference/layout/align/) |
| True | arguments | arguments | [arguments](https://typst.app/docs/reference/foundations/arguments/) |
| True | bibliography | bibliography | [bibliography](https://typst.app/docs/reference/model/bibliography/) |
| True | block | block | [block](https://typst.app/docs/reference/layout/block/) |
| True | box | box | [box](https://typst.app/docs/reference/layout/box/) |
| True | bullet_list | list | [list](https://typst.app/docs/reference/model/list/) |
| True | circle | circle | [circle](https://typst.app/docs/reference/visualize/circle/) |
| True | cite | cite | [cite](https://typst.app/docs/reference/model/cite/) |
| True | cmyk | cmyk | [cmyk](https://typst.app/docs/reference/visualize/color/#definitions-cmyk) |
| True | colbreak | colbreak | [colbreak](https://typst.app/docs/reference/layout/colbreak/) |
| True | color | color | [color](https://typst.app/docs/reference/visualize/color/) |
| True | columns | columns | [columns](https://typst.app/docs/reference/layout/columns/) |
| True | document | document | [document](https://typst.app/docs/reference/model/document/) |
| True | ellipse | ellipse | [ellipse](https://typst.app/docs/reference/visualize/ellipse/) |
| True | emph | emph | [emph](https://typst.app/docs/reference/model/emph/) |
| True | figure | figure | [figure](https://typst.app/docs/reference/model/figure/) |
| True | footnote | footnote | [footnote](https://typst.app/docs/reference/model/footnote/) |
| True | gradient | gradient | [gradient](https://typst.app/docs/reference/visualize/gradient/) |
| True | grid | grid | [grid](https://typst.app/docs/reference/layout/grid/) |
| True | heading | heading | [heading](https://typst.app/docs/reference/model/heading/) |
| True | hide | hide | [hide](https://typst.app/docs/reference/layout/hide/) |
| True | highlight | highlight | [highlight](https://typst.app/docs/reference/text/highlight/) |
| True | hspace | h | [h](https://typst.app/docs/reference/layout/h/) |
| True | image | image | [image](https://typst.app/docs/reference/visualize/image/) |
| True | layout | layout | [layout](https://typst.app/docs/reference/layout/layout/) |
| True | line | line | [line](https://typst.app/docs/reference/visualize/line/) |
| True | linebreak | linebreak | [linebreak](https://typst.app/docs/reference/text/linebreak/) |
| True | link | link | [link](https://typst.app/docs/reference/model/link/) |
| True | lorem | lorem | [lorem](https://typst.app/docs/reference/text/lorem/) |
| True | lower | lower | [lower](https://typst.app/docs/reference/text/lower/) |
| True | luma | luma | [luma](https://typst.app/docs/reference/visualize/color/#definitions-luma) |
| True | measure | measure | [measure](https://typst.app/docs/reference/layout/measure/) |
| True | move | move | [move](https://typst.app/docs/reference/layout/move/) |
| True | numbered_list | enum | [enum](https://typst.app/docs/reference/model/enum/) |
| True | numbering | numbering | [numbering](https://typst.app/docs/reference/model/numbering/) |
| True | oklab | oklab | [oklab](https://typst.app/docs/reference/visualize/color/#definitions-oklab) |
| True | oklch | oklch | [oklch](https://typst.app/docs/reference/visualize/color/#definitions-oklch) |
| True | outline | outline | [outline](https://typst.app/docs/reference/model/outline/) |
| True | overline | overline | [overline](https://typst.app/docs/reference/text/overline/) |
| True | padding | pad | [pad](https://typst.app/docs/reference/layout/pad/) |
| True | page | page | [page](https://typst.app/docs/reference/layout/page/) |
| True | pagebreak | pagebreak | [pagebreak](https://typst.app/docs/reference/layout/pagebreak/) |
| True | par | par | [par](https://typst.app/docs/reference/model/par/) |
| True | parbreak | parbreak | [parbreak](https://typst.app/docs/reference/model/parbreak/) |
| True | path | path | [path](https://typst.app/docs/reference/visualize/path/) |
| True | pattern | pattern | [pattern](https://typst.app/docs/reference/visualize/pattern/) |
| True | place | place | [place](https://typst.app/docs/reference/layout/place/) |
| True | polygon | polygon | [polygon](https://typst.app/docs/reference/visualize/polygon/) |
| True | quote | quote | [quote](https://typst.app/docs/reference/model/quote/) |
| True | raw | raw | [raw](https://typst.app/docs/reference/text/raw/) |
| True | rect | rect | [rect](https://typst.app/docs/reference/visualize/rect/) |
| True | ref | ref | [ref](https://typst.app/docs/reference/model/ref/) |
| True | repeat | repeat | [repeat](https://typst.app/docs/reference/layout/repeat/) |
| True | rgb | rgb | [rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb) |
| True | rotate | rotate | [rotate](https://typst.app/docs/reference/layout/rotate/) |
| True | scale | scale | [scale](https://typst.app/docs/reference/layout/scale/) |
| True | skew | skew | [skew](https://typst.app/docs/reference/layout/skew/) |
| True | smallcaps | smallcaps | [smallcaps](https://typst.app/docs/reference/text/smallcaps/) |
| True | smartquote | smartquote | [smartquote](https://typst.app/docs/reference/text/smartquote/) |
| True | square | square | [square](https://typst.app/docs/reference/visualize/square/) |
| True | stack | stack | [stack](https://typst.app/docs/reference/layout/stack/) |
| True | strike | strike | [strike](https://typst.app/docs/reference/text/strike/) |
| True | stroke | stroke | [stroke](https://typst.app/docs/reference/visualize/stroke/) |
| True | strong | strong | [strong](https://typst.app/docs/reference/model/strong/) |
| True | subscript | sub | [sub](https://typst.app/docs/reference/text/sub/) |
| True | superscript | super | [super](https://typst.app/docs/reference/text/super/) |
| True | table | table | [table](https://typst.app/docs/reference/model/table/) |
| True | terms | terms | [terms](https://typst.app/docs/reference/model/terms/) |
| True | text | text | [text](https://typst.app/docs/reference/text/text/) |
| True | underline | underline | [underline](https://typst.app/docs/reference/text/underline/) |
| True | upper | upper | [upper](https://typst.app/docs/reference/text/upper/) |
| True | vspace | v | [v](https://typst.app/docs/reference/layout/v/) |

## Design philosophy

## Change logs

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

`grid`:

```python
>>> grid(lorem(20), lorem(20), lorem(20), align=('center',) * 3)
'#grid(align: (center, center, center), lorem(20), lorem(20), lorem(20))'
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
