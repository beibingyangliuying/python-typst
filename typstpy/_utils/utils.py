from itertools import product
from typing import Any, Callable, Generator

import pandas as pd
from cytoolz.curried import keyfilter, memoize  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from ..param_types import Content


@memoize
def valid_styles() -> set[str]:
    """Valid typst citation styles.

    Returns:
        set[str]: The valid citation styles.
    """
    return {
        "annual-reviews",
        "pensoft",
        "annual-reviews-author-date",
        "the-lancet",
        "elsevier-with-titles",
        "gb-7714-2015-author-date",
        "royal-society-of-chemistry",
        "american-anthropological-association",
        "sage-vancouver",
        "british-medical-journal",
        "frontiers",
        "elsevier-harvard",
        "gb-7714-2005-numeric",
        "angewandte-chemie",
        "gb-7714-2015-note",
        "springer-basic-author-date",
        "trends",
        "american-geophysical-union",
        "american-political-science-association",
        "american-psychological-association",
        "cell",
        "spie",
        "harvard-cite-them-right",
        "american-institute-of-aeronautics-and-astronautics",
        "council-of-science-editors-author-date",
        "copernicus",
        "sist02",
        "springer-socpsych-author-date",
        "modern-language-association-8",
        "nature",
        "iso-690-numeric",
        "springer-mathphys",
        "springer-lecture-notes-in-computer-science",
        "future-science",
        "current-opinion",
        "deutsche-gesellschaft-für-psychologie",
        "american-meteorological-society",
        "modern-humanities-research-association",
        "american-society-of-civil-engineers",
        "chicago-notes",
        "institute-of-electrical-and-electronics-engineers",
        "deutsche-sprache",
        "gb-7714-2015-numeric",
        "bristol-university-press",
        "association-for-computing-machinery",
        "associacao-brasileira-de-normas-tecnicas",
        "american-medical-association",
        "elsevier-vancouver",
        "chicago-author-date",
        "vancouver",
        "chicago-fullnotes",
        "turabian-author-date",
        "springer-fachzeitschriften-medizin-psychologie",
        "thieme",
        "taylor-and-francis-national-library-of-medicine",
        "american-chemical-society",
        "american-institute-of-physics",
        "taylor-and-francis-chicago-author-date",
        "gost-r-705-2008-numeric",
        "institute-of-physics-numeric",
        "iso-690-author-date",
        "the-institution-of-engineering-and-technology",
        "american-society-for-microbiology",
        "multidisciplinary-digital-publishing-institute",
        "springer-basic",
        "springer-humanities-author-date",
        "turabian-fullnote-8",
        "karger",
        "springer-vancouver",
        "vancouver-superscript",
        "american-physics-society",
        "mary-ann-liebert-vancouver",
        "american-society-of-mechanical-engineers",
        "council-of-science-editors",
        "american-physiological-society",
        "future-medicine",
        "biomed-central",
        "public-library-of-science",
        "american-sociological-association",
        "modern-language-association",
        "alphanumeric",
        "ieee",
    }


@memoize
def original_name(func: Callable) -> str:
    """Get the `original name` of a function in typst.

    Args:
        func (Callable): The function to be retrieved.

    Returns:
        str: The `original name` of the function.
    """
    if hasattr(func, "_implement"):
        return func._implement.original_name
    return func.__name__


def decompose_dataframe(df: pd.DataFrame) -> Generator[Content, None, None]:
    """Decompose a pandas DataFrame into a generator of Content. The sequence is in row-major order.

    Args:
        df (pd.DataFrame): The DataFrame to be decomposed.

    Yields:
        Generator[Content, None, None]: A generator of Content.

    Example:
        >>> import pandas as pd
        >>> list(decompose_dataframe(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})))
        [Content(content='1'), Content(content='4'), Content(content='2'), Content(content='5'), Content(content='3'), Content(content='6')]
    """
    rows, columns = df.shape
    for row, column in product(range(rows), range(columns)):
        yield Content(str(df.iloc[row, column]))


def filter_default_params(func: Callable, params: dict[str, Any]) -> dict[str, Any]:
    """Filter out the default parameters of a function.

    Args:
        func (Callable): The function to be filtered.
        params (dict[str, Any]): The parameters to be filtered.

    Raises:
        ValueError: When the parameters which are not default given.

    Returns:
        dict[str, Any]: The filtered parameters.
    """
    defaults = func.__kwdefaults__
    if not params.keys() <= defaults.keys():
        raise ValueError("Parameters which are not default given.")
    return Pipe(params).map(keyfilter(lambda x: params[x] != defaults[x])).flush()
