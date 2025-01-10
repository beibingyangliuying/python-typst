from typing import Any, Callable, Literal, Protocol, TypedDict

# region foundations


Auto = Literal['auto']
Alignment = str
Angle = str
Content = str
Color = str
DateTime = str
Direction = str
Fraction = str
Function = str
Gradient = str
Label = str
Length = str
Location = str
Pattern = str
Ratio = str
Relative = str
Selector = str
Stroke = str


# endregion

TypstFunc = Callable[..., Content]
"""Functions that generate executable typst code."""
Predicate = Callable[[], bool]

# region protocols


class Normal(Protocol):
    def __call__(
        self, body: Any, /, *positional: Any, **keyword_only: Any
    ) -> Content: ...


class Positional(Protocol):
    def __call__(self, *positional: Any) -> Content: ...


class Instance(Protocol):
    def __call__(
        self, instance: Content, /, *positional: Any, **keyword_only: Any
    ) -> Content: ...


class Series(Protocol):
    def __call__(self, *children: Any, **keyword_only: Any) -> Content: ...


# endregion
# region constants


VALID_PAPER_SIZES = frozenset(
    [
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
    [
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
    'TypstFunc',
    'Predicate',
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
