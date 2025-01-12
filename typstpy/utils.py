from collections.abc import Iterable, Mapping
from typing import Any, Callable, NoReturn, Optional

from attrs import frozen
from cytoolz.curried import curry, keyfilter, memoize  # type: ignore

from typstpy.typings import (
    Content,
    Instance,
    Normal,
    Positional,
    Predicate,
    Series,
    TypstFunc,
)

# region utils


def all_predicates_satisfied(*predicates: Predicate) -> NoReturn | None:
    """Check if all predicates are satisfied and raise `ValueError` exception if not.

    Raises:
        ValueError: If any predicate is not satisfied.

    Returns:
        None if all predicates are satisfied, otherwise raises ValueError.
    """
    for predicate in predicates:
        if not predicate():
            freevars = predicate.__code__.co_freevars
            closure = (
                predicate.__closure__
            )  # Closure exists if and only if freevars is not empty
            raise ValueError(
                f'Invalid parameters: {', '.join(f'{i} = {j.cell_contents}' for i, j in zip(freevars, closure))}'  # type: ignore
            )
    return None


def _all_keywords_valid(func: TypstFunc, *keys: str) -> NoReturn | None:
    """Check if there are invalid keyword-only parameters.

    Args:
        func: The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        None if there are no invalid keyword-only parameters, otherwise raises ValueError.
    """
    residual = set(keys) - _extract_func(func).__kwdefaults__.keys()
    if residual:
        raise ValueError(f'Parameters which are not keyword-only given: {residual}')
    return None


def _extract_func(func: Callable, /) -> TypstFunc:
    """Extract the original function from the function decorated by `@curry`.

    Args:
        func: The function to be extracted.

    Returns:
        The original function.
    """
    # TODO: Check if the extracted function is compatible with `TypstFunc`.
    return func.func if isinstance(func, curry) else func


@memoize
def _original_name(func: TypstFunc, /) -> str:
    """Get the name representation in typst of a function.

    Args:
        func: The function to be retrieved.

    Returns:
        The name representation in typst.
    """
    func = _extract_func(func)
    return (
        func._implement.original_name if hasattr(func, '_implement') else func.__name__
    )


def _filter_params(func: TypstFunc, /, **kwargs: Any) -> dict[str, Any]:
    """Filter out parameters that are different from default values.

    Args:
        func: The function to be filtered.

    Raises:
        ValueError: Parameters which are not keyword-only given.

    Returns:
        The filtered parameters.
    """
    if not kwargs:
        return {}
    _all_keywords_valid(func, *kwargs.keys())
    defaults = _extract_func(func).__kwdefaults__
    return keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)


# endregion
# region render


def _render_key(key: str, /) -> str:
    """Render a key into a valid typst parameter representation.

    Args:
        key: The key to be rendered.

    Returns:
        The rendered key.
    """
    return key.replace('_', '-')


def _render_value(value: Any, /) -> str:
    """Render a value into a valid typst parameter representation.

    Args:
        value: The value to be rendered.

    Returns:
        The rendered value.

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
        case str():
            if value.startswith('#'):  # Function call.
                return value[1:]
            return value
        case Mapping():
            if not value:
                return '(:)'
            return f'({', '.join(f'{_render_key(k)}: {_render_value(v)}' for k, v in value.items())})'
        case Iterable():
            return f"({', '.join(_render_value(v) for v in value)})"
        case _:
            return str(value)


def _strip_brace(value: str, /) -> str:
    """Strip the left and right braces of a string.

    Args:
        value: The string to be stripped.

    Returns:
        The stripped string.
    """
    return value[1:-1]


# endregion
# region decorators


def attach_func(
    func: TypstFunc, name: Optional[str] = None, /
) -> Callable[[TypstFunc], TypstFunc]:
    """Attach a typst function to another typst function.

    Args:
        func: The function to attach.
        name: The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Raises:
        ValueError: Invalid name.

    Returns:
        The decorator function.
    """

    def wrapper(_func: TypstFunc) -> TypstFunc:
        _name = name if name else _func.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}')
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
    original_name: str, hyperlink: str = '', /
) -> Callable[[TypstFunc], TypstFunc]:
    """Set `_implement` attribute of a typst function and attach it with `where` and `with_` functions. The attribute type is `_Implement`.

    Args:
        original_name: The original function name in typst.
        hyperlink: The hyperlink of the documentation in typst. Defaults to ''.

    Returns:
        The decorator function.
    """

    def wrapper(_func: TypstFunc) -> TypstFunc:
        def where(**keyword_only: Any) -> Content:
            _all_keywords_valid(_func, *keyword_only.keys())
            return (
                f'#{original_name}.where({_strip_brace(_render_value(keyword_only))})'
            )

        def with_(**keyword_only: Any) -> Content:
            _all_keywords_valid(_func, *keyword_only.keys())
            return f'#{original_name}.with({_strip_brace(_render_value(keyword_only))})'

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


def set_(func: TypstFunc, /, **keyword_only: Any) -> Content:
    """Represent `set` rule in typst.

    Args:
        func: The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        Executable typst code.
    """
    _all_keywords_valid(func, *keyword_only.keys())
    return f'#set {_original_name(func)}({_strip_brace(_render_value(keyword_only))})'


def show_(
    element: Content | TypstFunc | None,
    appearance: Content | TypstFunc,
    /,
) -> Content:
    """Represent `show` rule in typst.

    Args:
        element: The typst function or content. If None, it means `show everything` rule.
        appearance: The typst function or content.

    Raises:
        ValueError: If the target is invalid.

    Returns:
        Executable typst code.
    """

    if element is None:
        _element = ''
    elif callable(element):
        _element = _original_name(element)
    else:
        _element = _render_value(element)

    if callable(appearance):
        _appearance = _original_name(appearance)
    else:
        _appearance = _render_value(appearance)

    return f'#show {_element}: {_appearance}'


def import_(path: str, /, *names: str) -> Content:
    """Represent `import` operation in typst.

    Args:
        path: The path of the file to be imported.

    Returns:
        Executable typst code.
    """
    return f'#import {path}: {_strip_brace(_render_value(names))}'


def normal(
    func: Normal,
    body: Any = '',
    /,
    *positional: Any,
    **keyword_only: Any,
) -> Content:
    """Represent the protocol of `normal`.

    Args:
        func: The function to be represented.
        body: The core parameter, it will be omitted if set to ''. Defaults to ''.

    Returns:
        Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)

    params = []
    if body != '':
        params.append(_render_value(body))
    if positional:
        params.append(_strip_brace(_render_value(positional)))
    if keyword_only:
        params.append(_strip_brace(_render_value(keyword_only)))

    return f'#{_original_name(func)}(' + ', '.join(params) + ')'


def positional(func: Positional, *positional: Any) -> Content:
    """Represent the protocol of `positional`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    return f'#{_original_name(func)}{_render_value(positional)}'


def instance(
    func: Instance, instance: Content, /, *positional: Any, **keyword_only: Any
) -> Content:
    """Represent the protocol of `pre_instance`.

    Args:
        func: The function to be represented.
        instance: The `instance` to call the function on.

    Returns:
        Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)

    params = []
    if positional:
        params.append(_strip_brace(_render_value(positional)))
    if keyword_only:
        params.append(_strip_brace(_render_value(keyword_only)))

    return f'{instance}.{_original_name(func)}(' + ', '.join(params) + ')'


def pre_series(func: Series, *children: Any, **keyword_only: Any) -> Content:
    """Represent the protocol of `pre_series`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)

    params = []
    if len(children) != 1:
        params.append(_strip_brace(_render_value(children)))
    else:
        params.append(f'..{_render_value(children[0])}')
    if keyword_only:
        params.append(_strip_brace(_render_value(keyword_only)))

    return f'#{_original_name(func)}(' + ', '.join(params) + ')'


def post_series(func: Series, *children: Any, **keyword_only: Any) -> Content:
    """Represent the protocol of `post_series`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)

    params = []
    if keyword_only:
        params.append(_strip_brace(_render_value(keyword_only)))
    if len(children) != 1:
        params.append(_strip_brace(_render_value(children)))
    else:
        params.append(f'..{_render_value(children[0])}')

    return f'#{_original_name(func)}(' + ', '.join(params) + ')'


# endregion

__all__ = [
    'all_predicates_satisfied',
    'attach_func',
    'implement',
    'set_',
    'show_',
    'import_',
    'normal',
    'positional',
    'instance',
    'pre_series',
    'post_series',
]
