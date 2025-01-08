from typing import Any, Callable, NoReturn, Optional, Union

from attrs import frozen
from cytoolz.curried import (  # type: ignore
    curry,
    isiterable,
    keyfilter,
    map,
    memoize,
    pipe,
)

from .typings import Content, Instance, Normal, Positional, Predicate, Series, TypstFunc

# region utils


def all_predicates_satisfied(*predicates: Predicate) -> NoReturn | None:
    """Check if all predicates are satisfied and raise `ValueError` exception if not.

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
                f'Invalid parameters: {', '.join(f'{i} = {j.cell_contents}' for i, j in zip(freevars, closure))}'  # type: ignore
            )
    return None


def _all_keywords_valid(func: TypstFunc, *keys: str) -> NoReturn | None:
    """Check if there are invalid keyword-only parameters.

    Args:
        func (TypstFunc): The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        NoReturn | None: None if there are no invalid keyword-only parameters, otherwise raises ValueError.
    """
    if not set(keys) <= _extract_func(func).__kwdefaults__.keys():
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
    return func.func if isinstance(func, curry) else func


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
        func._implement.original_name if hasattr(func, '_implement') else func.__name__
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
    _all_keywords_valid(func, *kwargs.keys())
    defaults = _extract_func(func).__kwdefaults__
    return keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)


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


def _strip_brace(value: str, /) -> str:
    """Strip the left and right braces of a string.

    Args:
        value (str): The string to be stripped.

    Returns:
        str: The stripped string.
    """
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
        func (TypstFunc): The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        Content: Executable typst code.
    """
    _all_keywords_valid(func, *keyword_only.keys())
    return f'#set {_original_name(func)}({_strip_brace(_render_value(keyword_only))})'


def show_(
    content: Content,
    shown: Optional[Union[Content, TypstFunc]] = None,
    /,
) -> Content:
    """Represent `show` rule in typst.

    Args:
        content (Content): Executable typst code.
        shown (Optional[Union[Content, TypstFunc]]): The typst function or content. If None, it means `show everything` rule. Defaults to None.

    Raises:
        ValueError: If the target is invalid.

    Returns:
        Content: Executable typst code.
    """
    if shown is None:
        _target = ''
    elif isinstance(shown, Content):
        _target = _render_value(shown)
    elif callable(shown):
        _target = _original_name(shown)
    else:
        raise ValueError(f'Invalid target: {shown}')
    return f'#show {_target}: {_render_value(content)}'


def import_(path: str, /, *names: str) -> Content:
    """Represent `import` operation in typst.

    Args:
        path (str): The path of the file to be imported.

    Returns:
        Content: Executable typst code.
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
        func (Normal): The function to be represented.
        body (Any, optional): The core parameter. Defaults to ''.

    Returns:
        Content: Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)
    return (
        f'#{_original_name(func)}('
        + ', '.join(
            pipe(
                [],
                lambda x: x if body == '' else x + [_render_value(body)],
                lambda x: x
                if not positional
                else x + [_strip_brace(_render_value(positional))],
                lambda x: x
                if not keyword_only
                else x + [_strip_brace(_render_value(keyword_only))],
            )
        )
        + ')'
    )


def positional(func: Positional, *positional: Any) -> Content:
    """Represent the protocol of `positional`.

    Args:
        func (Positional): The function to be represented.

    Returns:
        Content: Executable typst code.
    """
    return f'#{_original_name(func)}{_render_value(positional)}'


def instance(
    func: Instance, instance: Content, /, *positional: Any, **keyword_only: Any
) -> Content:
    """Represent the protocol of `pre_instance`.

    Args:
        func (Instance): The function to be represented.
        instance (Content): The `instance` to call the function on.

    Returns:
        Content: Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)
    pipe(
        [],
        lambda x: x
        if not positional
        else x + [_strip_brace(_render_value(positional))],
        lambda x: x
        if not keyword_only
        else x + [_strip_brace(_render_value(keyword_only))],
    )
    return (
        f'{instance}.{_original_name(func)}('
        + ', '.join(
            pipe(
                [],
                lambda x: x
                if not positional
                else x + [_strip_brace(_render_value(positional))],
                lambda x: x
                if not keyword_only
                else x + [_strip_brace(_render_value(keyword_only))],
            )
        )
        + ')'
    )


def pre_series(func: Series, *children: Any, **keyword_only: Any) -> Content:
    """Represent the protocol of `pre_series`.

    Args:
        func (Series): The function to be represented.

    Returns:
        Content: Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)
    return (
        f'#{_original_name(func)}('
        + ', '.join(
            pipe(
                [],
                lambda x: x + [_strip_brace(_render_value(children))]
                if len(children) != 1
                else x + [f'..{_render_value(children[0])}'],
                lambda x: x
                if not keyword_only
                else x + [_strip_brace(_render_value(keyword_only))],
            )
        )
        + ')'
    )


def post_series(func: Series, *children: Any, **keyword_only: Any) -> Content:
    """Represent the protocol of `post_series`.

    Args:
        func (Series): The function to be represented.

    Returns:
        Content: Executable typst code.
    """
    keyword_only = _filter_params(func, **keyword_only)
    return (
        f'#{_original_name(func)}('
        + ', '.join(
            pipe(
                [],
                lambda x: x
                if not keyword_only
                else x + [_strip_brace(_render_value(keyword_only))],
                lambda x: x + [_strip_brace(_render_value(children))]
                if len(children) != 1
                else x + [f'..{_render_value(children[0])}'],
            )
        )
        + ')'
    )


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
