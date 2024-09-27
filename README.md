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

## Examples

To be continued.

### `text`

```python
>>> text("Hello, World!", font="Arial", fallback=True)
'#text(font: "Arial", fallback: true)[Hello, World!]'
>>> text("Hello, World!", font=("Arial", "Times New Roman"), fallback=True)
'#text(font: ("Arial", "Times New Roman"), fallback: true)[Hello, World!]'
>>> text("Hello, World!", size=Length(12, "pt"))
'#text(size: 12pt)[Hello, World!]'
>>> text("Hello, World!", fill=color("red"))
'#text(fill: rgb("#ff4136"))[Hello, World!]'
```

### `emph`

```python
>>> emph("Hello, World!")
'#emph[Hello, World!]'
```

### `strong`

```python
>>> strong("Hello, World!")
'#strong[Hello, World!]'
>>> strong("Hello, World!", delta=300)
'#strong(delta: 300)[Hello, World!]'
```

### `par`

```python
>>> par("Hello, World!", leading=Length(1.5, "em"))
'#par(leading: 1.5em)[Hello, World!]'
>>> par("Hello, World!", justify=True)
'#par(justify: true)[Hello, World!]'
>>> par("Hello, World!")
'Hello, World!'
```

### `heading`

```python
>>> heading("Hello, World!", level=2, supplement=Content("Chapter"), label=Label("chap:chapter"))
'#heading(supplement: [Chapter], level: 2)[Hello, World!] <chap:chapter>'
>>> heading("Hello, World!", level=2)
'== Hello, World!'
```

### `image`

```python
>>> image("image.png")
'#image("image.png")'
>>> image("image.png", format="png")
'#image("image.png", format: "png")'
```

### `figure`

```python
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

| bibliography | path, title, full, style | STANDARD |
| cite | key, form, style | STANDARD |
| cmyk | cyan, magenta, yellow, key | STANDARD |
| color | name | NOTSTANDARD |
| rgb | args | STANDARD |
| color.hsl | hue, saturation, lightness, alpha | STANDARD |
| color.linear_rgb | red, green, blue, alpha | STANDARD |
| emph | content | STANDARD |
| figure | content, caption, label | STANDARD |
| figure.caption | content, position, separator | STANDARD |
| heading | content, level, supplement, numbering, label | STANDARD |
| image | path, format, width, height, alt, fit | STANDARD |
| lorem | words | STANDARD |
| luma | lightness, alpha | STANDARD |
| pagebreak | weak, to | STANDARD |
| par | content, leading, justify, linebreaks, first_line_indent, hanging_indent | STANDARD |
| ref | target | STANDARD |
| rgb | args | STANDARD |
| strong | content, delta | STANDARD |
| text | content, font, fallback, style, weight, stretch, size, fill | STANDARD |

_STANDARD_ means you could find implementation in typst.
_NOTSTANDARD_ means this function is not the standard implementation of corresponding function in typst, or is not implemented in typst but for convenience.
