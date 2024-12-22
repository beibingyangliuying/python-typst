from typing import Any, Callable

from cytoolz.curried import (  # type:ignore  # type:ignore
    curry,
    identity,
    isiterable,
    keyfilter,
    map,
    memoize,
)
from pymonad.maybe import Maybe  # type:ignore
from pymonad.reader import Pipe  # type:ignore
from pymonad.state import State  # type:ignore

from ..typings import Block, Instance, Normal, Positional, Series, TypstFunc

# region utils


def _extract_func(func: Callable, /) -> TypstFunc:
    """Extract the original function from a curried function.

    Args:
        func (Callable): The function to be extracted.

    Returns:
        TypstFunc: The original function.
    """
    return (
        Maybe(func, isinstance(func, curry)).map(lambda x: x.func).maybe(func, identity)
    )


@memoize
def _original_name(func: TypstFunc, /) -> str:
    """Get the name representation in typst of a function.

    Args:
        func (TypstFunc): The function to be retrieved.

    Returns:
        str: The name representation in typst.
    """
    func = _extract_func(func)
    return (
        Maybe(func, hasattr(func, '_implement'))
        .map(lambda x: x._implement.original_name)
        .maybe(func.__name__, identity)
    )


def _filter_params(func: TypstFunc, /, **params: Any) -> dict[str, Any]:
    """Filter out parameters that are different from default values.

    Args:
        func (TypstFunc): The function to be filtered.

    Raises:
        ValueError: Parameters which are not keyword-only given.

    Returns:
        dict[str, Any]: The filtered parameters.
    """
    if not params:
        return {}
    defaults = _extract_func(func).__kwdefaults__
    if not params.keys() <= defaults.keys():
        raise ValueError('Parameters which are not keyword-only given.')
    return Pipe(params).map(keyfilter(lambda x: params[x] != defaults[x])).flush()


# endregion
# region render


def _render_key(key: str, /) -> str:
    """Render a key into a valid typst parameter representation.

    Args:
        key (str): The key to be rendered.

    Returns:
        str: The rendered key.
    """
    return key.replace('_', '-')


def _render_value(value: Any, /) -> str:
    """Render a value into a valid typst parameter representation.

    Args:
        value (Any): The value to be rendered.

    Returns:
        str: The rendered value.

    Examples:
        >>> _render_value(True)
        'true'
        >>> _render_value(False)
        'false'
        >>> _render_value(None)
        'none'
        >>> _render_value(1)
        '1'
        >>> _render_value('foo')
        'foo'
        >>> _render_value('#color.map')
        'color.map'
        >>> _render_value(dict())
        '(:)'
        >>> _render_value({'a': 1, 'b': 2})
        '(a: 1, b: 2)'
        >>> _render_value(dict(left='5pt', top_right='20pt', bottom_right='10pt'))
        '(left: 5pt, top-right: 20pt, bottom-right: 10pt)'
        >>> _render_value([])
        '()'
        >>> _render_value([1, 2, 3])
        '(1, 2, 3)'
        >>> _render_value([[1] * 5, [2] * 5, [3] * 5])
        '((1, 1, 1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3))'
    """
    match value:
        case None | bool():
            return str(value).lower()
        case dict():
            if not value:
                return '(:)'
            return f'({', '.join(f'{_render_key(k)}: {_render_value(v)}' for k, v in value.items())})'
        case str() if value.startswith('#'):  # Function call.
            return value[1:]
        case str():
            return value
        case value if isiterable(value):
            return f"({', '.join(map(_render_value, value))})"
        case _:
            return str(value)


def _strip(value: str, /) -> str:
    return value[1:-1]


# endregion
# region concepts


def normal(
    func: Normal,
    body: Any = '',
    /,
    *positional_args: Any,
    **keyword_only_args: Any,
) -> Block:
    """Represent the concept of `normal`.

    Args:
        func (Normal): The function to be represented.
        body (Any, optional): The core parameter. Defaults to ''.

    Returns:
        Block: Executable typst code.
    """
    keyword_only_args = _filter_params(func, **keyword_only_args)
    result = (
        State(lambda x: (x, x))
        .then(
            lambda x: Maybe(body, body != '')
            .map(_render_value)
            .maybe(x, lambda y: x + [y])
        )
        .then(
            lambda x: Maybe(positional_args, positional_args)
            .map(_render_value)
            .map(_strip)
            .maybe(x, lambda y: x + [y])
        )
        .then(
            lambda x: Maybe(keyword_only_args, keyword_only_args)
            .map(_render_value)
            .map(_strip)
            .maybe(x, lambda y: x + [y])
        )
        .run([])
    )[0]
    return f'#{_original_name(func)}(' + ', '.join(result) + ')'


def positional(func: Positional, *positional_args: Any) -> Block:
    """Represent the concept of `positional`.

    Args:
        func (Positional): The function to be represented.

    Returns:
        Block: Executable typst code.
    """
    return f'#{_original_name(func)}{_render_value(positional_args)}'


def instance(
    func: Instance, instance: Block, /, *positional_args: Any, **keyword_only_args: Any
) -> Block:
    """Represent the concept of `instance`.

    Args:
        func (Instance): The function to be represented.
        instance (Block): The `instance` to call the function on.

    Returns:
        Block: Executable typst code.
    """
    keyword_only_args = _filter_params(func, **keyword_only_args)
    result = (
        State(lambda x: (x, x))
        .then(
            lambda x: Maybe(positional_args, positional_args)
            .map(_render_value)
            .map(_strip)
            .maybe(x, lambda y: x + [y])
        )
        .then(
            lambda x: Maybe(keyword_only_args, keyword_only_args)
            .map(_render_value)
            .map(_strip)
            .maybe(x, lambda y: x + [y])
        )
        .run([])
    )[0]
    return f'{instance}.{_original_name(func)}(' + ', '.join(result) + ')'


def pre_series(func: Series, *elements: Any, **keyword_only_args: Any) -> Block:
    """Represent the concept of `pre_series`.

    Args:
        func (Series): The function to be represented.

    Returns:
        Block: Executable typst code.
    """
    keyword_only_args = _filter_params(func, **keyword_only_args)
    result = (
        State(lambda x: (x, x))
        .then(
            lambda x: x
            + [
                Maybe(elements, len(elements) == 1)
                .map(_render_value)
                .map(lambda x: f'..{x}')
                .maybe(_strip(_render_value(elements)), identity)
            ]
        )
        .then(
            lambda x: Maybe(keyword_only_args, keyword_only_args)
            .map(_render_value)
            .map(_strip)
            .maybe(x, lambda y: x + [y])
        )
        .run([])
    )[0]
    return f'#{_original_name(func)}(' + ', '.join(result) + ')'


def post_series(func: Series, *elements: Any, **keyword_only_args: Any) -> Block:
    """Represent the concept of `post_series`.

    Args:
        func (Series): The function to be represented.

    Returns:
        Block: Executable typst code.
    """
    keyword_only_args = _filter_params(func, **keyword_only_args)
    result = (
        State(lambda x: (x, x))
        .then(
            lambda x: Maybe(keyword_only_args, keyword_only_args)
            .map(_render_value)
            .map(_strip)
            .maybe(x, lambda y: x + [y])
        )
        .then(
            lambda x: x
            + [
                Maybe(elements, len(elements) == 1)
                .map(_render_value)
                .map(lambda x: f'..{x}')
                .maybe(_strip(_render_value(elements)), identity)
            ]
        )
        .run([])
    )[0]
    return f'#{_original_name(func)}(' + ', '.join(result) + ')'


# endregion
