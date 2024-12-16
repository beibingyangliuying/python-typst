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
| True | lower | lower | [lower](https://typst.app/docs/reference/text/lower/) |
| True | luma | luma | [luma](https://typst.app/docs/reference/visualize/color/#definitions-luma) |
| True | pagebreak | pagebreak | [pagebreak](https://typst.app/docs/reference/layout/pagebreak/) |
| True | par | par | [par](https://typst.app/docs/reference/model/par/) |
| True | ref | ref | [ref](https://typst.app/docs/reference/model/ref/) |
| True | rgb | rgb | [rgb](https://typst.app/docs/reference/visualize/color/#definitions-rgb) |
| True | smallcaps | smallcaps | [smallcaps](https://typst.app/docs/reference/text/smallcaps/) |
| True | strong | strong | [strong](https://typst.app/docs/reference/model/strong/) |
| True | sub | sub | [sub](https://typst.app/docs/reference/text/sub/) |
| True | sup | super | [super](https://typst.app/docs/reference/text/super/) |
| True | text | text | [text](https://typst.app/docs/reference/text/text/) |

## Examples

```python
from typstpy import *
```

_color_hsl

```python
>>> color.hsl(Angle.deg(30), Ratio(100), Ratio(50), Ratio(50))
'#color.hsl(30deg, 100%, 50%, 50%)'
>>> color.hsl(Angle.deg(30), 100, 50)
'#color.hsl(30deg, 100, 50)'
```

_color_linear_rgb

```python
>>> color.linear_rgb(255, 255, 255)
'#color.linear-rgb(255, 255, 255)'
>>> color.linear_rgb(255, 255, 255, 0.5)
'#color.linear-rgb(255, 255, 255, 0.5)'
>>> color.linear_rgb(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
'#color.linear-rgb(50%, 50%, 50%, 50%)'
```

_figure_caption

```python
>>> figure.caption("This is a caption.")
'This is a caption.'
>>> figure.caption(strong("This is a caption."))
'#strong[This is a caption.]'
>>> figure.caption("This is a caption.", position=Alignment.TOP)
'#figure.caption(position: top, [This is a caption.])'
>>> figure.caption(strong("This is a caption."), position=Alignment.TOP)
'#figure.caption(position: top, strong[This is a caption.])'
>>> figure.caption("This is a caption.", separator="---")
'#figure.caption(separator: [---], [This is a caption.])'
>>> figure.caption("This is a caption.", position=Alignment.TOP, separator="---")
'#figure.caption(position: top, separator: [---], [This is a caption.])'
```

bibliography

```python
>>> bibliography("references.bib")
'#bibliography("references.bib")'
>>> bibliography("references.bib", title="My Bib")
'#bibliography("references.bib", title: [My Bib])'
>>> bibliography("references.bib", title=None)
'#bibliography("references.bib", title: none)'
>>> bibliography("references.bib", full=True)
'#bibliography("references.bib", full: true)'
>>> bibliography("references.bib", style="annual-reviews")
'#bibliography("references.bib", style: "annual-reviews")'
>>> bibliography("references.bib", title="My Bib", full=True, style="annual-reviews")
'#bibliography("references.bib", title: [My Bib], full: true, style: "annual-reviews")'
```

cite

```python
>>> label = Label("Essay")
>>> cite(label)
'#cite(<Essay>)'
>>> cite(label, supplement="1")
'#cite(<Essay>, supplement: [1])'
>>> cite(label, form="prose")
'#cite(<Essay>, form: "prose")'
>>> cite(label, style="ieee")
'#cite(<Essay>, style: "ieee")'
>>> cite(label, supplement="1", form="prose", style="ieee")
'#cite(<Essay>, supplement: [1], form: "prose", style: "ieee")'
```

cmyk

```python
>>> cmyk(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
'#cmyk(50%, 50%, 50%, 50%)'
```

color

```python
>>> color("black")
'#luma(0)'
>>> color("gray")
'#luma(170)'
>>> color("silver")
'#luma(221)'
>>> color("white")
'#luma(255)'
>>> color("navy")
'#rgb("#001f3f")'
>>> color("blue")
'#rgb("#0074d9")'
>>> color("aqua")
'#rgb("#7fdbff")'
>>> color("teal")
'#rgb("#39cccc")'
>>> color("eastern")
'#rgb("#239dad")'
>>> color("purple")
'#rgb("#b10dc9")'
>>> color("fuchsia")
'#rgb("#f012be")'
>>> color("maroon")
'#rgb("#85144b")'
>>> color("red")
'#rgb("#ff4136")'
>>> color("orange")
'#rgb("#ff851b")'
>>> color("yellow")
'#rgb("#ffdc00")'
>>> color("olive")
'#rgb("#3d9970")'
>>> color("green")
'#rgb("#2ecc40")'
>>> color("lime")
'#rgb("#01ff70")'
```

emph

```python
>>> emph("Hello, World!")
'#emph([Hello, World!])'
>>> emph(text("Hello, World!", font="Arial", fallback=True))
'#emph(text(font: "Arial")[Hello, World!])'
```

figure

```python
>>> figure(image("image.png"))
'#figure(image("image.png"))'
>>> figure(image("image.png"), Label("fig:Figure"))
'#figure(image("image.png")) <fig:Figure>'
>>> figure(image("image.png"), placement=Alignment.TOP)
'#figure(image("image.png"), placement: top)'
>>> figure(image("image.png"), caption="This is a caption.")
'#figure(image("image.png"), caption: [This is a caption.])'
>>> figure(image("image.png"), caption=figure.caption("This is a caption.", position=Alignment.TOP, separator="---"))
'#figure(image("image.png"), caption: figure.caption(position: top, separator: [---], [This is a caption.]))'
>>> figure(image("image.png"), kind="figure")
'#figure(image("image.png"), kind: "figure")'
>>> figure(image("image.png"), supplement="Bar")
'#figure(image("image.png"), supplement: [Bar])'
>>> figure(image("image.png"), numbering="1.")
'#figure(image("image.png"), numbering: "1.")'
>>> figure(image("image.png"), gap=Length.em(0.5))
'#figure(image("image.png"), gap: 0.5em)'
>>> figure(image("image.png"), outlined=False)
'#figure(image("image.png"), outlined: false)'
```

footnote

```python
>>> footnote("Hello, World!")
'#footnote([Hello, World!])'
>>> footnote(text("Hello, World!", font="Arial"))
'#footnote(text(font: "Arial")[Hello, World!])'
```

heading

```python
>>> heading("Hello, World!")
'= Hello, World!'
>>> heading("Hello, World!", level=2)
'== Hello, World!'
>>> heading("Hello, World!", depth=2)
'== Hello, World!'
>>> heading("Hello, World!", offset=1)
'== Hello, World!'
>>> heading("Hello, World!", level=4, depth=2, offset=1)
'==== Hello, World!'
>>> heading("Hello, World!", numbering="a.")
'#heading(numbering: "a.", level: 1)[Hello, World!]'
>>> heading("Hello, World!", supplement="Chapter")
'#heading(supplement: [Chapter], level: 1)[Hello, World!]'
>>> heading("Hello, World!", outlined=False)
'#heading(outlined: false, level: 1)[Hello, World!]'
>>> heading("Hello, World!", bookmarked=False)
'#heading(bookmarked: false, level: 1)[Hello, World!]'
```

image

```python
>>> image("image.png")
'#image("image.png")'
>>> image("image.png", format="png")
'#image("image.png", format: "png")'
>>> image("image.png", width=Ratio(50))
'#image("image.png", width: 50%)'
>>> image("image.png", height=Ratio(50))
'#image("image.png", height: 50%)'
>>> image("image.png", alt="An image")
'#image("image.png", alt: "An image")'
```

link

```python
>>> link("https://typst.app/docs/")
'#link("https://typst.app/docs/")'
>>> link(Label("chap:chapter"))
'#link(<chap:chapter>)'
```

lorem

```python
>>> lorem(10)
'#lorem(10)'
```

lower

```python
>>> lower("Hello, World!")
'#lower([Hello, World!])'
>>> lower(text("Hello, World!", font="Arial"))
'#lower(text(font: "Arial")[Hello, World!])'
>>> lower(emph("Hello, World!"))
'#lower(emph([Hello, World!]))'
```

luma

```python
>>> luma(50)
'#luma(50)'
>>> luma(50, 0.5)
'#luma(50, 0.5)'
>>> luma(Ratio(50), Ratio(50))
'#luma(50%, 50%)'
```

pagebreak

```python
>>> pagebreak()
'#pagebreak()'
>>> pagebreak(weak=True)
'#pagebreak(weak: true)'
>>> pagebreak(to="even")
'#pagebreak(to: "even")'
>>> pagebreak(to="odd")
'#pagebreak(to: "odd")'
>>> pagebreak(weak=True, to="even")
'#pagebreak(weak: true, to: "even")'
>>> pagebreak(weak=True, to="odd")
'#pagebreak(weak: true, to: "odd")'
```

par

```python
>>> par("Hello, World!")
'Hello, World!'
>>> par("Hello, World!", leading=Length.em(1.5))
'#par(leading: 1.5em)[Hello, World!]'
>>> par("Hello, World!", justify=True)
'#par(justify: true)[Hello, World!]'
>>> par("Hello, World!", linebreaks="optimized")
'#par(linebreaks: "optimized")[Hello, World!]'
>>> par("Hello, World!", first_line_indent=Length.em(1.5))
'#par(first-line-indent: 1.5em)[Hello, World!]'
>>> par("Hello, World!", hanging_indent=Length.em(1.5))
'#par(hanging-indent: 1.5em)[Hello, World!]'
>>> par("Hello, World!", leading=Length.em(1.5), justify=True, linebreaks="optimized", first_line_indent=Length.em(1.5), hanging_indent=Length.em(1.5))     
'#par(leading: 1.5em, justify: true, linebreaks: "optimized", first-line-indent: 1.5em, hanging-indent: 1.5em)[Hello, World!]'
```

ref

```python
>>> label = Label("chap:chapter")
>>> ref(label)
'#ref(<chap:chapter>)'
>>> ref(Label("chap:chapter"), supplement="Spam!")
'#ref(<chap:chapter>, supplement: [Spam!])'
>>> ref(Label("chap:chapter"), supplement=None)
'#ref(<chap:chapter>, supplement: none)'
```

rgb

```python
>>> rgb(255, 255, 255)
'#rgb(255, 255, 255)'
>>> rgb(255, 255, 255, 0.5)
'#rgb(255, 255, 255, 0.5)'
>>> rgb(Ratio(50), Ratio(50), Ratio(50), Ratio(50))
'#rgb(50%, 50%, 50%, 50%)'
>>> rgb("#ffffff")
'#rgb("#ffffff")'
```

smallcaps

```python
>>> smallcaps("Hello, World!")
'#smallcaps([Hello, World!])'
```

strong

```python
>>> strong("Hello, World!")
'#strong[Hello, World!]'
>>> strong("Hello, World!", delta=400)
'#strong(delta: 400)[Hello, World!]'
>>> strong(text("Hello, World!", font="Arial"), delta=400)
'#strong(delta: 400)[#text(font: "Arial")[Hello, World!]]'
```

sub

```python
>>> sub("Hello, World!")
'#sub[Hello, World!]'
>>> sub("Hello, World!", typographic=False)
'#sub(typographic: false)[Hello, World!]'
>>> sub("Hello, World!", baseline=Length.em(0.4))
'#sub(baseline: 0.4em)[Hello, World!]'
>>> sub("Hello, World!", size=Length.em(0.8))
'#sub(size: 0.8em)[Hello, World!]'
>>> sub("Hello, World!", typographic=False, baseline=Length.em(0.4), size=Length.em(0.8))
'#sub(typographic: false, baseline: 0.4em, size: 0.8em)[Hello, World!]'
```

sup

```python
>>> sup("Hello, World!")
'#super[Hello, World!]'
>>> sup("Hello, World!", typographic=False)
'#super(typographic: false)[Hello, World!]'
>>> sup("Hello, World!", baseline=Length.em(0.4))
'#super(baseline: 0.4em)[Hello, World!]'
>>> sup("Hello, World!", size=Length.em(0.8))
'#super(size: 0.8em)[Hello, World!]'
>>> sup("Hello, World!", typographic=False, baseline=Length.em(0.4), size=Length.em(0.8))
'#super(typographic: false, baseline: 0.4em, size: 0.8em)[Hello, World!]'
```

text

```python
>>> text("Hello, World!")
'Hello, World!'
>>> text("Hello, World!", font="Arial")
'#text(font: "Arial")[Hello, World!]'
>>> text("Hello, World!", font=("Arial", "Times New Roman"))
'#text(font: ("Arial", "Times New Roman"))[Hello, World!]'
>>> text("Hello, World!", fallback=False)
'#text(fallback: false)[Hello, World!]'
>>> text("Hello, World!", style="italic")
'#text(style: "italic")[Hello, World!]'
>>> text("Hello, World!", weight="bold")
'#text(weight: "bold")[Hello, World!]'
>>> text("Hello, World!", weight=300)
'#text(weight: 300)[Hello, World!]'
>>> text("Hello, World!", stretch=Ratio(50))
'#text(stretch: 50%)[Hello, World!]'
>>> text("Hello, World!", size=Length(12, "pt"))
'#text(size: 12pt)[Hello, World!]'
>>> text("Hello, World!", fill=color("red"))
'#text(fill: rgb("#ff4136"))[Hello, World!]'
```
