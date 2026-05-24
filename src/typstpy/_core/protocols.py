from collections.abc import Callable

from .registry import (
    Implement,
    keyword_defaults,
    raise_unknown_fields,
)
from .render import render_content, render_value

_SPREADABLE_CODE_PREFIXES = ('#color.map.',)
"""Typst color-map values (e.g. ``'#color.map.turbo'``) carry a ``#`` prefix
in raw Python form; ``render_value()`` strips the ``#`` during rendering,
so the spread output becomes ``..color.map.turbo`` as expected by Typst.
"""


def _filter_default_kwargs(
    func: Callable[..., object], kwargs: dict[str, object]
) -> dict[str, object]:
    """Drop keyword arguments whose value matches the function's own default."""
    defaults = keyword_defaults(func)
    if func not in Implement.temporary:
        raise_unknown_fields(func, kwargs)
    if not defaults:
        return kwargs
    return {
        key: value
        for key, value in kwargs.items()
        if key not in defaults or value != defaults[key]
    }


def _should_spread_color_map(child: object) -> bool:
    """Return True if *child* is a color-map value that should be spread."""
    return isinstance(child, str) and child.startswith(_SPREADABLE_CODE_PREFIXES)


def _should_spread_list_sequence(func: Callable[..., object], child: object) -> bool:
    """Return True if a single list/tuple *child* should be spread per the function's config."""
    if isinstance(child, list | tuple):
        impl = Implement.permanent.get(func)
        if impl is not None:
            return impl.spread_single
    return False


def _should_spread_single_child(func: Callable[..., object], child: object) -> bool:
    """Return True if a single child value should be spread into multiple arguments."""
    return _should_spread_color_map(child) or _should_spread_list_sequence(func, child)


def _render_series_children(
    func: Callable[..., object], children: tuple[object, ...]
) -> list[str]:
    """Render variadic children for series protocols, applying spread when needed."""
    if not children:
        return []
    if len(children) == 1:
        child = children[0]
        if _should_spread_single_child(func, child):
            return [f'..{render_value(child)}']
        return [render_value(child)]
    return [render_content(children)]


def set_(func: Callable[..., object], /, **kwargs: object) -> str:
    """Represent `set` rule in typst.

    Args:
        func: The typst function.

    Raises:
        TypeError: If there are invalid keyword-only parameters.

    Returns:
        Executable typst code.
    """
    if func not in Implement.temporary:
        raise_unknown_fields(func, kwargs)

    params = render_content(kwargs) if kwargs else ''
    return f'#set {render_value(func)}({params})'


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
        return f'#show: {render_value(appearance)}'
    return f'#show {render_value(element)}: {render_value(appearance)}'


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
    return f'#import {path}: {render_content(names)}'


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
        params.append(render_value(body))
    if args:
        params.append(render_content(args))
    if kwargs:
        params.append(render_content(kwargs))

    return f'#{render_value(func)}(' + ', '.join(params) + ')'


def positional(func: Callable[..., object], *args: object) -> str:
    """Represent the protocol of `positional`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    return f'#{render_value(func)}{render_value(args)}'


def call_(func: Callable[..., object], *args: object, **kwargs: object) -> str:
    """Render a function call with explicit positional argument order."""
    kwargs = _filter_default_kwargs(func, kwargs)

    params = []
    if args:
        params.append(render_content(args))
    if kwargs:
        params.append(render_content(kwargs))

    return f'#{render_value(func)}(' + ', '.join(params) + ')'


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
        params.append(render_content(args))
    if kwargs:
        params.append(render_content(kwargs))

    return f'{instance}.{render_value(func)}(' + ', '.join(params) + ')'


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
        params.append(render_content(kwargs))

    return f'#{render_value(func)}(' + ', '.join(params) + ')'


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
        params.append(render_content(kwargs))
    params.extend(_render_series_children(func, children))

    return f'#{render_value(func)}(' + ', '.join(params) + ')'
