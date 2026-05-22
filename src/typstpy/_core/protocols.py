from collections.abc import Callable

from .registry import (
    _function_label,
    _Implement,
    _keyword_defaults,
    _raise_unknown_fields,
)
from .render import _render_value, _strip_brace

_SPREADABLE_CODE_PREFIXES = ('#color.map.',)
_SPREAD_SINGLE_SEQUENCE_FUNCTIONS = frozenset(
    {
        'color.mix',
        'enum',
        'gradient.conic',
        'gradient.linear',
        'gradient.radial',
        'grid',
        'list',
        'stack',
        'subpar.grid',
        'table',
    }
)


def _filter_default_kwargs(
    func: Callable[..., object], kwargs: dict[str, object]
) -> dict[str, object]:
    defaults = _keyword_defaults(func)
    if func not in _Implement.temporary:
        _raise_unknown_fields(func, kwargs)
    if not defaults:
        return kwargs
    return {
        key: value
        for key, value in kwargs.items()
        if key not in defaults or value != defaults[key]
    }


def _should_spread_single_child(func: Callable[..., object], child: object) -> bool:
    if isinstance(child, str) and child.startswith(_SPREADABLE_CODE_PREFIXES):
        return True
    if isinstance(child, list | tuple):
        return _function_label(func) in _SPREAD_SINGLE_SEQUENCE_FUNCTIONS
    return False


def _render_series_children(
    func: Callable[..., object], children: tuple[object, ...]
) -> list[str]:
    if not children:
        return []
    if len(children) == 1:
        child = children[0]
        if _should_spread_single_child(func, child):
            return [f'..{_render_value(child)}']
        return [_render_value(child)]
    return [_strip_brace(_render_value(children))]


def set_(func: Callable[..., object], /, **kwargs: object) -> str:
    """Represent `set` rule in typst.

    Args:
        func: The typst function.

    Raises:
        TypeError: If there are invalid keyword-only parameters.

    Returns:
        Executable typst code.
    """
    if func not in _Implement.temporary:
        _raise_unknown_fields(func, kwargs)

    params = _strip_brace(_render_value(kwargs)) if kwargs else ''
    return f'#set {_render_value(func)}({params})'


def show_(element: object, appearance: object, /) -> str:
    """Represent `show` rule in typst.

    Args:
        element: The typst function or content. If None, it means `show everything` rule.
        appearance: The typst function or content.

    Returns:
        Executable typst code.

    Examples:
        >>> show_(None, 'it => it')
        '#show: it => it'
    """
    if element is None:
        return f'#show: {_render_value(appearance)}'
    return f'#show {_render_value(element)}: {_render_value(appearance)}'


def import_(path: object, /, *names: object) -> str:
    """Represent `import` operation in typst.

    Args:
        path: The path of the file to be imported.

    Returns:
        Executable typst code.

    Examples:
        >>> import_('"module.typ"')
        '#import "module.typ"'
        >>> import_('"module.typ"', 'foo', 'bar')
        '#import "module.typ": foo, bar'
    """
    if not names:
        return f'#import {path}'
    return f'#import {path}: {_strip_brace(_render_value(names))}'


def normal(
    func: Callable[..., object],
    body: object = '',
    /,
    *args: object,
    **kwargs: object,
) -> str:
    """Represent the protocol of `normal`.

    Args:
        func: The function to be represented.
        body: The core parameter, it will be omitted if set to ''. Defaults to ''.

    Returns:
        Executable typst code.
    """
    kwargs = _filter_default_kwargs(func, kwargs)

    params = []
    if body != '':
        params.append(_render_value(body))
    if args:
        params.append(_strip_brace(_render_value(args)))
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'#{_render_value(func)}(' + ', '.join(params) + ')'


def positional(func: Callable[..., object], *args: object) -> str:
    """Represent the protocol of `positional`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    return f'#{_render_value(func)}{_render_value(args)}'


def _call(func: Callable[..., object], *args: object, **kwargs: object) -> str:
    """Render a function call with explicit positional argument order."""
    kwargs = _filter_default_kwargs(func, kwargs)

    params = []
    if args:
        params.append(_strip_brace(_render_value(args)))
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'#{_render_value(func)}(' + ', '.join(params) + ')'


def instance(
    func: Callable[..., object], instance: object, /, *args: object, **kwargs: object
) -> str:
    """Represent the protocol of `pre_instance`.

    Args:
        func: The function to be represented.
        instance: The `instance` to call the function on.

    Returns:
        Executable typst code.
    """
    kwargs = _filter_default_kwargs(func, kwargs)

    params = []
    if args:
        params.append(_strip_brace(_render_value(args)))
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'{instance}.{_render_value(func)}(' + ', '.join(params) + ')'


def pre_series(func: Callable[..., object], *children: object, **kwargs: object) -> str:
    """Represent the protocol of `pre_series`, which means that `children` will be prepended.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    kwargs = _filter_default_kwargs(func, kwargs)

    params = _render_series_children(func, children)
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'#{_render_value(func)}(' + ', '.join(params) + ')'


def post_series(
    func: Callable[..., object], *children: object, **kwargs: object
) -> str:
    """Represent the protocol of `post_series`, which means that `children` will be postfixed.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    kwargs = _filter_default_kwargs(func, kwargs)

    params = []
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))
    params.extend(_render_series_children(func, children))

    return f'#{_render_value(func)}(' + ', '.join(params) + ')'
