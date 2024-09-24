# python-typst

`python-typst` is a library for generating executable typst code (See [typst repository](https://github.com/typst/typst) and [typst documentation](https://typst.app/docs/) for more information).
It is written primarily in functional programming paradigm with some OOP content.

This package provides the interfaces in a way that is as close as possible to typst's native functions.
Through `python-typst` and other data processing packages, you can generate data reports quickly.

Contributions are welcome.

## Installation

```bash
pip install typstpy
```

## Examples

```python
>>> from typstpy import emph, figure, heading, image, par, strong, text, Block, Content, Label, Length, Ratio, Relative
>>> text("Hello, World!", font="Arial", fallback=True)
'#text(font: "Arial", fallback: true)[Hello, World!]'
>>> text("Hello, World!", font=("Arial", "Times New Roman"), fallback=True)
'#text(font: ("Arial", "Times New Roman"), fallback: true)[Hello, World!]'
>>> text("Hello, World!", size=Length(12, "pt"))
'#text(size: 12pt)[Hello, World!]'
>>> emph("Hello, World!")
'#emph[Hello, World!]'
>>> strong("Hello, World!")
'#strong[Hello, World!]'
>>> strong("Hello, World!", delta=300)
'#strong(delta: 300)[Hello, World!]'
>>> par("Hello, World!", leading=Length(1.5, "em"))
'#par(leading: 1.5em)[Hello, World!]'
>>> par("Hello, World!", justify=True)
'#par(justify: true)[Hello, World!]'
>>> par("Hello, World!")
'Hello, World!'
>>> heading("Hello, World!", level=2, supplement=Content("Chapter"), label=Label("chap:chapter"))
'#heading(supplement: [Chapter], level: 2)[Hello, World!] <chap:chapter>'
>>> heading("Hello, World!", level=2)
'== Hello, World!'
>>> image("image.png")
'#image("image.png")'
>>> image("image.png", format="png")
'#image("image.png", format: "png")'
>>> figure(image("image.png"))
'#figure(image("image.png"))'
>>> figure(image("image.png"), caption=Content("This is a figure."))
'#figure(image("image.png"), caption: [This is a figure.])'
>>> figure(image("image.png"), caption=Content("This is a figure."), label=Label("fig:figure"))
'#figure(image("image.png"), caption: [This is a figure.]) <fig:figure>'
>>> figure(image("image.png"), caption=figure.caption("This is a figure.", separator=Content("---")))
'#figure(image("image.png"), caption: figure.caption(separator: [---])[This is a figure.])'
```

## Current Support

| Name | Parameters |
| --- | ---|
| text | font, fallback, size |
| emph | |
| strong | delta |
| par | leading, justify, linebreaks, first_line_indent, hanging_indent |
| heading | level, supplement, numbering, label |
| image | path, format, width, height, alt, fit |
| figure | caption, label |
| figure.caption | separator |

## ChangeLog

### [0.0.1] - 2024-09-24

#### Added

| Name | Parameters |
| --- | ---|
| text | font, fallback, size |
| emph | |
| strong | delta |
| par | leading, justify, linebreaks, first_line_indent, hanging_indent |
| heading | level, supplement, numbering, label |
| image | path, format, width, height, alt, fit |
| figure | caption, label |
| figure.caption | separator |
