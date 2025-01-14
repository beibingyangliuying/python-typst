from typing import Any, Literal, Protocol, TypedDict

# region foundations


# TODO: Use `type` expression in future version.
Auto = Literal['auto']
"""A value that indicates a smart default. See [the documentation](https://typst.app/docs/reference/foundations/auto/) for more information."""
Alignment = Literal[
    'start',
    'end',
    'left',
    'center',
    'right',
    'top',
    'horizon',
    'bottom',
    'start + end',
    'start + left',
    'start + center',
    'start + right',
    'start + top',
    'start + horizon',
    'start + bottom',
    'end + left',
    'end + center',
    'end + right',
    'end + top',
    'end + horizon',
    'end + bottom',
    'left + center',
    'left + right',
    'left + top',
    'left + horizon',
    'left + bottom',
    'center + right',
    'center + top',
    'center + horizon',
    'center + bottom',
    'right + top',
    'right + horizon',
    'right + bottom',
    'top + horizon',
    'top + bottom',
    'horizon + bottom',
]
"""Where to align something along an axis. See [the documentation](https://typst.app/docs/reference/layout/alignment/) for more information."""
Angle = str
"""An angle describing a rotation. See [the documentation](https://typst.app/docs/reference/layout/angle/) for more information."""
Content = str
"""Executable typst code. See [the documentation](https://typst.app/docs/reference/foundations/content/) for more information."""
Color = str
"""A color in a specific color space. See [the documentation](https://typst.app/docs/reference/visualize/color/) for more information."""
DateTime = str
"""Represents a date, a time, or a combination of both. See [the documentation](https://typst.app/docs/reference/foundations/datetime/) for more information."""
Direction = Literal['ltr', 'rtl', 'ttb', 'btt']
"""The four directions into which content can be laid out. See [the documentation](https://typst.app/docs/reference/layout/direction/) for more information."""
Fraction = str
"""Defines how the remaining space in a layout is distributed. See [the documentation](https://typst.app/docs/reference/layout/fraction/) for more information."""
Function = str
"""A mapping from argument values to a return value. See [the documentation](https://typst.app/docs/reference/foundations/function/) for more information."""
Gradient = str
"""A color gradient. See [the documentation](https://typst.app/docs/reference/visualize/gradient/) for more information."""
Label = str
"""A label for an element. See [the documentation](https://typst.app/docs/reference/foundations/label/) for more information."""
Length = str
"""A size or distance, possibly expressed with contextual units. See [the documentation](https://typst.app/docs/reference/layout/length/) for more information."""
Location = str
"""Identifies an element in the document. See [the documentation](https://typst.app/docs/reference/introspection/location/) for more information."""
Pattern = str
"""A repeating pattern fill. See [the documentation](https://typst.app/docs/reference/visualize/pattern/) for more information."""
Ratio = str
"""A ratio of a whole. See [the documentation](https://typst.app/docs/reference/layout/ratio/) for more information."""
Relative = str
"""A length in relation to some known length. See [the documentation](https://typst.app/docs/reference/layout/relative/) for more information."""
Selector = str
"""A filter for selecting elements within the document. See [the documentation](https://typst.app/docs/reference/foundations/selector/) for more information."""
Stroke = str
"""Defines how to draw a line. See [the documentation](https://typst.app/docs/reference/visualize/stroke/) for more information."""


# endregion
# region protocols


class Normal(Protocol):
    def __call__(self, body: Any, /, *args: Any, **kwargs: Any) -> Content: ...


class Positional(Protocol):
    def __call__(self, *args: Any) -> Content: ...


class Instance(Protocol):
    def __call__(self, instance: Content, /, *args: Any, **kwargs: Any) -> Content: ...


class Series(Protocol):
    def __call__(self, *children: Any, **kwargs: Any) -> Content: ...


# endregion
# region constants


VALID_PAPER_SIZES = frozenset(
    {
        '"a0"',
        '"a1"',
        '"a2"',
        '"a3"',
        '"a4"',
        '"a5"',
        '"a6"',
        '"a7"',
        '"a8"',
        '"a9"',
        '"a10"',
        '"a11"',
        '"iso-b1"',
        '"iso-b2"',
        '"iso-b3"',
        '"iso-b4"',
        '"iso-b5"',
        '"iso-b6"',
        '"iso-b7"',
        '"iso-b8"',
        '"iso-c3"',
        '"iso-c4"',
        '"iso-c5"',
        '"iso-c6"',
        '"iso-c7"',
        '"iso-c8"',
        '"din-d3"',
        '"din-d4"',
        '"din-d5"',
        '"din-d6"',
        '"din-d7"',
        '"din-d8"',
        '"sis-g5"',
        '"sis-e5"',
        '"ansi-a"',
        '"ansi-b"',
        '"ansi-c"',
        '"ansi-d"',
        '"ansi-e"',
        '"arch-a"',
        '"arch-b"',
        '"arch-c"',
        '"arch-d"',
        '"arch-e1"',
        '"arch-e"',
        '"jis-b0"',
        '"jis-b1"',
        '"jis-b2"',
        '"jis-b3"',
        '"jis-b4"',
        '"jis-b5"',
        '"jis-b6"',
        '"jis-b7"',
        '"jis-b8"',
        '"jis-b9"',
        '"jis-b10"',
        '"jis-b11"',
        '"sac-d0"',
        '"sac-d1"',
        '"sac-d2"',
        '"sac-d3"',
        '"sac-d4"',
        '"sac-d5"',
        '"sac-d6"',
        '"iso-id-1"',
        '"iso-id-2"',
        '"iso-id-3"',
        '"asia-f4"',
        '"jp-shiroku-ban-4"',
        '"jp-shiroku-ban-5"',
        '"jp-shiroku-ban-6"',
        '"jp-kiku-4"',
        '"jp-kiku-5"',
        '"jp-business-card"',
        '"cn-business-card"',
        '"eu-business-card"',
        '"fr-tellière"',
        '"fr-couronne-écriture"',
        '"fr-couronne-édition"',
        '"fr-raisin"',
        '"fr-carré"',
        '"fr-jésus"',
        '"uk-brief"',
        '"uk-draft"',
        '"uk-foolscap"',
        '"uk-quarto"',
        '"uk-crown"',
        '"uk-book-a"',
        '"uk-book-b"',
        '"us-letter"',
        '"us-legal"',
        '"us-tabloid"',
        '"us-executive"',
        '"us-foolscap-folio"',
        '"us-statement"',
        '"us-ledger"',
        '"us-oficio"',
        '"us-gov-letter"',
        '"us-gov-legal"',
        '"us-business-card"',
        '"us-digest"',
        '"us-trade"',
        '"newspaper-compact"',
        '"newspaper-berliner"',
        '"newspaper-broadsheet"',
        '"presentation-16-9"',
        '"presentation-4-3"',
    }
)
ValidPaperSizes = Literal[
    '"a0"',
    '"a1"',
    '"a2"',
    '"a3"',
    '"a4"',
    '"a5"',
    '"a6"',
    '"a7"',
    '"a8"',
    '"a9"',
    '"a10"',
    '"a11"',
    '"iso-b1"',
    '"iso-b2"',
    '"iso-b3"',
    '"iso-b4"',
    '"iso-b5"',
    '"iso-b6"',
    '"iso-b7"',
    '"iso-b8"',
    '"iso-c3"',
    '"iso-c4"',
    '"iso-c5"',
    '"iso-c6"',
    '"iso-c7"',
    '"iso-c8"',
    '"din-d3"',
    '"din-d4"',
    '"din-d5"',
    '"din-d6"',
    '"din-d7"',
    '"din-d8"',
    '"sis-g5"',
    '"sis-e5"',
    '"ansi-a"',
    '"ansi-b"',
    '"ansi-c"',
    '"ansi-d"',
    '"ansi-e"',
    '"arch-a"',
    '"arch-b"',
    '"arch-c"',
    '"arch-d"',
    '"arch-e1"',
    '"arch-e"',
    '"jis-b0"',
    '"jis-b1"',
    '"jis-b2"',
    '"jis-b3"',
    '"jis-b4"',
    '"jis-b5"',
    '"jis-b6"',
    '"jis-b7"',
    '"jis-b8"',
    '"jis-b9"',
    '"jis-b10"',
    '"jis-b11"',
    '"sac-d0"',
    '"sac-d1"',
    '"sac-d2"',
    '"sac-d3"',
    '"sac-d4"',
    '"sac-d5"',
    '"sac-d6"',
    '"iso-id-1"',
    '"iso-id-2"',
    '"iso-id-3"',
    '"asia-f4"',
    '"jp-shiroku-ban-4"',
    '"jp-shiroku-ban-5"',
    '"jp-shiroku-ban-6"',
    '"jp-kiku-4"',
    '"jp-kiku-5"',
    '"jp-business-card"',
    '"cn-business-card"',
    '"eu-business-card"',
    '"fr-tellière"',
    '"fr-couronne-écriture"',
    '"fr-couronne-édition"',
    '"fr-raisin"',
    '"fr-carré"',
    '"fr-jésus"',
    '"uk-brief"',
    '"uk-draft"',
    '"uk-foolscap"',
    '"uk-quarto"',
    '"uk-crown"',
    '"uk-book-a"',
    '"uk-book-b"',
    '"us-letter"',
    '"us-legal"',
    '"us-tabloid"',
    '"us-executive"',
    '"us-foolscap-folio"',
    '"us-statement"',
    '"us-ledger"',
    '"us-oficio"',
    '"us-gov-letter"',
    '"us-gov-legal"',
    '"us-business-card"',
    '"us-digest"',
    '"us-trade"',
    '"newspaper-compact"',
    '"newspaper-berliner"',
    '"newspaper-broadsheet"',
    '"presentation-16-9"',
    '"presentation-4-3"',
]
VALID_CITATION_STYLES = frozenset(
    {
        '"annual-reviews"',
        '"pensoft"',
        '"annual-reviews-author-date"',
        '"the-lancet"',
        '"elsevier-with-titles"',
        '"gb-7714-2015-author-date"',
        '"royal-society-of-chemistry"',
        '"american-anthropological-association"',
        '"sage-vancouver"',
        '"british-medical-journal"',
        '"frontiers"',
        '"elsevier-harvard"',
        '"gb-7714-2005-numeric"',
        '"angewandte-chemie"',
        '"gb-7714-2015-note"',
        '"springer-basic-author-date"',
        '"trends"',
        '"american-geophysical-union"',
        '"american-political-science-association"',
        '"american-psychological-association"',
        '"cell"',
        '"spie"',
        '"harvard-cite-them-right"',
        '"american-institute-of-aeronautics-and-astronautics"',
        '"council-of-science-editors-author-date"',
        '"copernicus"',
        '"sist02"',
        '"springer-socpsych-author-date"',
        '"modern-language-association-8"',
        '"nature"',
        '"iso-690-numeric"',
        '"springer-mathphys"',
        '"springer-lecture-notes-in-computer-science"',
        '"future-science"',
        '"current-opinion"',
        '"deutsche-gesellschaft-für-psychologie"',
        '"american-meteorological-society"',
        '"modern-humanities-research-association"',
        '"american-society-of-civil-engineers"',
        '"chicago-notes"',
        '"institute-of-electrical-and-electronics-engineers"',
        '"deutsche-sprache"',
        '"gb-7714-2015-numeric"',
        '"bristol-university-press"',
        '"association-for-computing-machinery"',
        '"associacao-brasileira-de-normas-tecnicas"',
        '"american-medical-association"',
        '"elsevier-vancouver"',
        '"chicago-author-date"',
        '"vancouver"',
        '"chicago-fullnotes"',
        '"turabian-author-date"',
        '"springer-fachzeitschriften-medizin-psychologie"',
        '"thieme"',
        '"taylor-and-francis-national-library-of-medicine"',
        '"american-chemical-society"',
        '"american-institute-of-physics"',
        '"taylor-and-francis-chicago-author-date"',
        '"gost-r-705-2008-numeric"',
        '"institute-of-physics-numeric"',
        '"iso-690-author-date"',
        '"the-institution-of-engineering-and-technology"',
        '"american-society-for-microbiology"',
        '"multidisciplinary-digital-publishing-institute"',
        '"springer-basic"',
        '"springer-humanities-author-date"',
        '"turabian-fullnote-8"',
        '"karger"',
        '"springer-vancouver"',
        '"vancouver-superscript"',
        '"american-physics-society"',
        '"mary-ann-liebert-vancouver"',
        '"american-society-of-mechanical-engineers"',
        '"council-of-science-editors"',
        '"american-physiological-society"',
        '"future-medicine"',
        '"biomed-central"',
        '"public-library-of-science"',
        '"american-sociological-association"',
        '"modern-language-association"',
        '"alphanumeric"',
        '"ieee"',
    }
)
ValidCitationStyles = Literal[
    '"annual-reviews"',
    '"pensoft"',
    '"annual-reviews-author-date"',
    '"the-lancet"',
    '"elsevier-with-titles"',
    '"gb-7714-2015-author-date"',
    '"royal-society-of-chemistry"',
    '"american-anthropological-association"',
    '"sage-vancouver"',
    '"british-medical-journal"',
    '"frontiers"',
    '"elsevier-harvard"',
    '"gb-7714-2005-numeric"',
    '"angewandte-chemie"',
    '"gb-7714-2015-note"',
    '"springer-basic-author-date"',
    '"trends"',
    '"american-geophysical-union"',
    '"american-political-science-association"',
    '"american-psychological-association"',
    '"cell"',
    '"spie"',
    '"harvard-cite-them-right"',
    '"american-institute-of-aeronautics-and-astronautics"',
    '"council-of-science-editors-author-date"',
    '"copernicus"',
    '"sist02"',
    '"springer-socpsych-author-date"',
    '"modern-language-association-8"',
    '"nature"',
    '"iso-690-numeric"',
    '"springer-mathphys"',
    '"springer-lecture-notes-in-computer-science"',
    '"future-science"',
    '"current-opinion"',
    '"deutsche-gesellschaft-für-psychologie"',
    '"american-meteorological-society"',
    '"modern-humanities-research-association"',
    '"american-society-of-civil-engineers"',
    '"chicago-notes"',
    '"institute-of-electrical-and-electronics-engineers"',
    '"deutsche-sprache"',
    '"gb-7714-2015-numeric"',
    '"bristol-university-press"',
    '"association-for-computing-machinery"',
    '"associacao-brasileira-de-normas-tecnicas"',
    '"american-medical-association"',
    '"elsevier-vancouver"',
    '"chicago-author-date"',
    '"vancouver"',
    '"chicago-fullnotes"',
    '"turabian-author-date"',
    '"springer-fachzeitschriften-medizin-psychologie"',
    '"thieme"',
    '"taylor-and-francis-national-library-of-medicine"',
    '"american-chemical-society"',
    '"american-institute-of-physics"',
    '"taylor-and-francis-chicago-author-date"',
    '"gost-r-705-2008-numeric"',
    '"institute-of-physics-numeric"',
    '"iso-690-author-date"',
    '"the-institution-of-engineering-and-technology"',
    '"american-society-for-microbiology"',
    '"multidisciplinary-digital-publishing-institute"',
    '"springer-basic"',
    '"springer-humanities-author-date"',
    '"turabian-fullnote-8"',
    '"karger"',
    '"springer-vancouver"',
    '"vancouver-superscript"',
    '"american-physics-society"',
    '"mary-ann-liebert-vancouver"',
    '"american-society-of-mechanical-engineers"',
    '"council-of-science-editors"',
    '"american-physiological-society"',
    '"future-medicine"',
    '"biomed-central"',
    '"public-library-of-science"',
    '"american-sociological-association"',
    '"modern-language-association"',
    '"alphanumeric"',
    '"ieee"',
]


class RectangleRadius(TypedDict, total=False):
    top_left: Relative
    top_right: Relative
    bottom_right: Relative
    bottom_left: Relative
    left: Relative
    top: Relative
    right: Relative
    bottom: Relative
    rest: Relative


class RectangleStroke(TypedDict, total=False):
    top: Stroke
    right: Stroke
    bottom: Stroke
    left: Stroke
    x: Stroke
    y: Stroke
    rest: Stroke


class BoxInset(TypedDict, total=False):
    x: Relative
    y: Relative


class BoxOutset(TypedDict, total=False):
    x: Relative
    y: Relative


class PageMargin(TypedDict, total=False):
    top: Relative
    right: Relative
    bottom: Relative
    left: Relative
    inside: Relative
    outside: Relative
    x: Relative
    y: Relative
    rest: Relative


class LinkDest(TypedDict, total=False):
    page: int
    x: Length
    y: Length


class SmartquoteQuotes(TypedDict, total=False):  # TODO: Uncertain value type.
    single: Auto | str
    double: Auto | str


class TextCosts(TypedDict, total=False):
    hyphenation: Ratio
    runt: Ratio
    widow: Ratio
    orphan: Ratio


# endregion


__all__ = [
    'Auto',
    'Alignment',
    'Angle',
    'Content',
    'Color',
    'DateTime',
    'Direction',
    'Fraction',
    'Function',
    'Gradient',
    'Label',
    'Length',
    'Location',
    'Pattern',
    'Ratio',
    'Relative',
    'Selector',
    'Stroke',
    'Normal',
    'Positional',
    'Instance',
    'Series',
    'VALID_PAPER_SIZES',
    'ValidPaperSizes',
    'VALID_CITATION_STYLES',
    'ValidCitationStyles',
    'RectangleRadius',
    'RectangleStroke',
    'BoxInset',
    'BoxOutset',
    'PageMargin',
    'LinkDest',
    'SmartquoteQuotes',
    'TextCosts',
]
