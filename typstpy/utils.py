from typing import Any, Callable, NoReturn, Optional

from attrs import frozen
from cytoolz.curried import (  # type:ignore
    curry,
    isiterable,
    keyfilter,
    map,
    memoize,
)
from pymonad.maybe import Maybe  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from .typings import Block, Instance, Normal, Positional, Predicate, Series, TypstFunc

# region utils


def pad(s: str, /) -> str:
    """Pad a string with double quotes.

    Args:
        s (str): The string to be padded.

    Returns:
        str: The padded string.
    """
    return f'"{s}"'


def is_valid(*predicates: Predicate) -> NoReturn | None:
    """Check if all predicates are satisfied and throw `ValueError` if not.

    Raises:
        ValueError: If any predicate is not satisfied.

    Returns:
        NoReturn | None: None if all predicates are satisfied, otherwise raises ValueError.
    """
    for predicate in predicates:
        if not predicate():
            freevars = predicate.__code__.co_freevars
            closure = (
                predicate.__closure__
            )  # Closure exists if and only if freevars is not empty
            raise ValueError(
                f'Invalid parameters: {', '.join(f'{i} = {j.cell_contents}' for i, j in zip(freevars, closure))}'  # type:ignore
            )
    return None


def is_keywords_valid(func: TypstFunc, /, **kwargs: Any) -> NoReturn | None:
    """Check if there are invalid keyword-only parameters.

    Args:
        func (TypstFunc): The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        NoReturn | None: None if there are no invalid keyword-only parameters, otherwise raises ValueError.
    """
    keys = kwargs.keys()
    if not keys <= _extract_func(func).__kwdefaults__.keys():
        raise ValueError(f'Parameters which are not keyword-only given: {keys}')
    return None


def _extract_func(func: Callable, /) -> TypstFunc:
    """Extract the original function from the function decorated by `@curry`.

    Args:
        func (Callable): The function to be extracted.

    Returns:
        TypstFunc: The original function.
    """
    # TODO: Check if the extracted function is compatible with `TypstFunc`.
    return Maybe(func, isinstance(func, curry)).maybe(func, lambda x: x.func)


@memoize
def _original_name(func: TypstFunc, /) -> str:
    """Get the name representation in typst of a function.

    Args:
        func (TypstFunc): The function to be retrieved.

    Returns:
        str: The name representation in typst.
    """
    func = _extract_func(func)
    return Maybe(func, hasattr(func, '_implement')).maybe(
        func.__name__, lambda x: x._implement.original_name
    )


def _filter_params(func: TypstFunc, /, **kwargs: Any) -> dict[str, Any]:
    """Filter out parameters that are different from default values.

    Args:
        func (TypstFunc): The function to be filtered.

    Raises:
        ValueError: Parameters which are not keyword-only given.

    Returns:
        dict[str, Any]: The filtered parameters.
    """
    if not kwargs:
        return {}
    is_keywords_valid(func, **kwargs)
    defaults = _extract_func(func).__kwdefaults__
    return Pipe(kwargs).map(keyfilter(lambda x: kwargs[x] != defaults[x])).flush()


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
# region decorators


def attach_func(
    func: TypstFunc, name: Optional[str] = None, /
) -> Callable[[TypstFunc], TypstFunc]:
    """Attach a typst function to another typst function.

    Args:
        func (TypstFunc): The function to attach.
        name (Optional[str], optional): The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Raises:
        ValueError: Invalid name.

    Returns:
        Callable[[TypstFunc], TypstFunc]: The decorator function.
    """

    def wrapper(_func: TypstFunc) -> TypstFunc:
        _name = name if name else _func.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}.')
        setattr(_func, _name, func)
        return _func

    return wrapper


@frozen
class _Implement:
    name: str
    original_name: str
    hyperlink: str

    def __str__(self) -> str:
        return (
            '| '
            + ' | '.join(
                [self.name, self.original_name, f'[{self.hyperlink}]({self.hyperlink})']
            )
            + ' |'
        )


def implement(
    original_name: str, hyperlink: str, /
) -> Callable[[TypstFunc], TypstFunc]:
    """Set `_implement` attribute of a typst function and attach it with `where` and `with_` functions. The attribute type is `_Implement`.

    Args:
        original_name (str): The original function name in typst.
        hyperlink (str): The hyperlink of the documentation in typst.

    Returns:
        Callable[[TypstFunc], TypstFunc]: The decorator function.
    """

    def wrapper(_func: TypstFunc) -> TypstFunc:
        def where(**kwargs: Any) -> Block:
            is_keywords_valid(_func, **kwargs)
            return f'#{original_name}.where({_strip(_render_value(kwargs))})'

        def with_(**kwargs: Any) -> Block:
            is_keywords_valid(_func, **kwargs)
            return f'#{original_name}.with({_strip(_render_value(kwargs))})'

        setattr(
            _func,
            '_implement',
            _Implement(_func.__name__, original_name, hyperlink),
        )
        attach_func(where, 'where')(_func)
        attach_func(with_, 'with_')(_func)
        return _func

    return wrapper


# endregion
# region protocols


def normal(
    func: Normal,
    body: Any = '',
    /,
    *args: Any,
    **kwargs: Any,
) -> Block:
    """Represent the protocol of `normal`.

    Args:
        func (Normal): The function to be represented.
        body (Any, optional): The core parameter. Defaults to ''.

    Returns:
        Block: Executable typst code.
    """
    kwargs = _filter_params(func, **kwargs)
    return (
        f'#{_original_name(func)}('
        + ', '.join(
            Pipe([])
            .map(
                lambda x: Maybe(body, body != '')
                .map(_render_value)
                .maybe(x, lambda y: x + [y])
            )
            .map(
                lambda x: Maybe(args, args)
                .map(_render_value)
                .map(_strip)
                .maybe(x, lambda y: x + [y])
            )
            .map(
                lambda x: Maybe(kwargs, kwargs)
                .map(_render_value)
                .map(_strip)
                .maybe(x, lambda y: x + [y])
            )
            .flush()
        )
        + ')'
    )


def positional(func: Positional, *args: Any) -> Block:
    """Represent the protocol of `positional`.

    Args:
        func (Positional): The function to be represented.

    Returns:
        Block: Executable typst code.
    """
    return f'#{_original_name(func)}{_render_value(args)}'


def instance(func: Instance, instance: Block, /, *args: Any, **kwargs: Any) -> Block:
    """Represent the protocol of `pre_instance`.

    Args:
        func (Instance): The function to be represented.
        instance (Block): The `instance` to call the function on.

    Returns:
        Block: Executable typst code.
    """
    kwargs = _filter_params(func, **kwargs)
    return (
        f'{instance}.{_original_name(func)}('
        + ', '.join(
            Pipe([])
            .map(
                lambda x: Maybe(args, args)
                .map(_render_value)
                .map(_strip)
                .maybe(x, lambda y: x + [y])
            )
            .map(
                lambda x: Maybe(kwargs, kwargs)
                .map(_render_value)
                .map(_strip)
                .maybe(x, lambda y: x + [y])
            )
            .flush()
        )
        + ')'
    )


def pre_series(func: Series, *elements: Any, **kwargs: Any) -> Block:
    """Represent the protocol of `pre_series`.

    Args:
        func (Series): The function to be represented.

    Returns:
        Block: Executable typst code.
    """
    kwargs = _filter_params(func, **kwargs)
    return (
        f'#{_original_name(func)}('
        + ', '.join(
            Pipe([])
            .map(
                lambda x: x
                + [
                    Maybe(elements, len(elements) == 1)
                    .map(lambda x: _render_value(x[0]))
                    .maybe(
                        Pipe(elements).map(_render_value).map(_strip),
                        lambda x: Pipe(x).map(lambda x: f'..{x}'),
                    )
                    .flush()
                ]
            )
            .map(
                lambda x: Maybe(kwargs, kwargs)
                .map(_render_value)
                .map(_strip)
                .maybe(x, lambda y: x + [y])
            )
            .flush()
        )
        + ')'
    )


def post_series(func: Series, *elements: Any, **kwargs: Any) -> Block:
    """Represent the protocol of `post_series`.

    Args:
        func (Series): The function to be represented.

    Returns:
        Block: Executable typst code.
    """
    kwargs = _filter_params(func, **kwargs)
    return (
        f'#{_original_name(func)}('
        + ', '.join(
            Pipe([])
            .map(
                lambda x: Maybe(kwargs, kwargs)
                .map(_render_value)
                .map(_strip)
                .maybe(x, lambda y: x + [y])
            )
            .map(
                lambda x: x
                + [
                    Maybe(elements, len(elements) == 1)
                    .map(lambda x: _render_value(x[0]))
                    .maybe(
                        Pipe(elements).map(_render_value).map(_strip),
                        lambda x: Pipe(x).map(lambda x: f'..{x}'),
                    )
                    .flush()
                ]
            )
            .flush()
        )
        + ')'
    )


# endregion

__all__ = [
    'pad',
    'is_valid',
    'is_keywords_valid',
    'attach_func',
    'implement',
    'normal',
    'positional',
    'instance',
    'pre_series',
    'post_series',
]
