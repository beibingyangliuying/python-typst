from typing import Any

from typstpy._core import Instance, Normal, Positional, Series, implement, temporary
from typstpy._core import instance as _instance
from typstpy._core import normal as _normal
from typstpy._core import positional as _positional
from typstpy._core import post_series as _post_series
from typstpy._core import pre_series as _pre_series
from typstpy.typings import Content


def normal(original_name: str, /) -> Normal:
    """Function factory, create function that represent the protocol of `normal`.

    Args:
        original_name: The original function name in typst.

    Returns:
        A function that represent the protocol of `normal`.

    Examples:
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
    """

    @temporary()
    @implement(original_name)
    def wrapped(body: Any = '', /, *args: Any, **kwargs: Any) -> Content:
        return _normal(wrapped, body, *args, **kwargs)

    return wrapped


def instance(original_name: str, /) -> Instance:
    """Function factory, create function that represent the protocol of `instance`.

    Args:
        original_name: The original function name in typst.

    Returns:
        A function that represent the protocol of `instance`.

    Examples:
        >>> rgb = positional('rgb')
        >>> color_lighten = instance('lighten')
        >>> color_lighten(rgb(255, 255, 255), '50%')
        '#rgb(255, 255, 255).lighten(50%)'
    """

    @temporary()
    @implement(original_name)
    def wrapped(instance: Content, /, *args: Any, **kwargs: Any) -> Content:
        return _instance(wrapped, instance, *args, **kwargs)

    return wrapped


def positional(original_name: str, /) -> Positional:
    """Function factory, create function that represent the protocol of `positional`.

    Args:
        original_name: The original function name in typst.

    Returns:
        A function that represent the protocol of `positional`.

    Examples:
        >>> rgb = positional('rgb')
        >>> rgb(255, 255, 255, '50%')
        '#rgb(255, 255, 255, 50%)'
    """

    @temporary()
    @implement(original_name)
    def wrapped(*args: Any) -> Content:
        return _positional(wrapped, *args)

    return wrapped


def post_series(original_name: str, /) -> Series:
    """Function factory, create function that represent the protocol of `Series`.

    Args:
        original_name: The original function name in typst.

    Returns:
        A function that represent the protocol of `Series`.

    Examples:
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
    """

    @temporary()
    @implement(original_name)
    def wrapped(*children: Any, **kwargs: Any) -> Content:
        return _post_series(wrapped, *children, **kwargs)

    return wrapped


def pre_series(original_name: str, /) -> Series:
    """Function factory, create function that represent the protocol of `Series`.

    Args:
        original_name: The original function name in typst.

    Returns:
        A function that represent the protocol of `Series`.

    Examples:
        >>> subpar_grid = pre_series('subpar.grid')
        >>> subpar_grid(
        ...     '[]',
        ...     '[]',
        ...     columns=('1fr', '1fr'),
        ...     caption='[A figure composed of two sub figures.]',
        ...     label='<full>',
        ... )
        '#subpar.grid([], [], columns: (1fr, 1fr), caption: [A figure composed of two sub figures.], label: <full>)'
    """

    @temporary()
    @implement(original_name)
    def wrapped(*children: Any, **kwargs: Any) -> Content:
        return _pre_series(wrapped, *children, **kwargs)

    return wrapped


__all__ = ['normal', 'instance', 'positional', 'post_series', 'pre_series']
