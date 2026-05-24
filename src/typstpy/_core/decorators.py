from collections.abc import Callable
from typing import Any

from .registry import Implement, raise_unknown_fields
from .render import render_content


def attach_func(
    attached: Callable[..., Any], name: str | None = None
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Attach a typst function to another typst function.

    Args:
        attached: The function to attach.
        name: The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Raises:
        ValueError: Invalid name.

    Returns:
        The decorator function.
    """

    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        _name = name if name else attached.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}')
        setattr(func, _name, attached)
        return func

    return wrapper


def _make_where_func(
    func: Callable[..., Any], original_name: str
) -> Callable[..., str]:
    def where(**kwargs: Any) -> str:
        if func not in Implement.temporary:
            raise_unknown_fields(func, kwargs)
        params = render_content(kwargs) if kwargs else ''
        return f'#{original_name}.where({params})'

    return where


def _make_with_func(func: Callable[..., Any], original_name: str) -> Callable[..., str]:
    def with_(*args: Any, **kwargs: Any) -> str:
        if func not in Implement.temporary:
            raise_unknown_fields(func, kwargs)
        params = []
        if args:
            params.append(render_content(args))
        if kwargs:
            params.append(render_content(kwargs))
        return f'#{original_name}.with({", ".join(params)})'

    return with_


def implement(
    original_name: str,
    *,
    hyperlink: str | None = None,
    version: str | None = None,
    spread_single: bool = False,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Register a typst function and attach it with `where` and `with_` functions.

    Args:
        original_name: The original function name in typst.
        hyperlink: The hyperlink of the documentation in typst. Defaults to None.
        version: The current supported version. Defaults to None.
        spread_single: Whether a single list/tuple child should be spread. Defaults to False.

    Returns:
        The decorator function.
    """

    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        Implement.permanent[func] = Implement(
            original_name, hyperlink, version, spread_single
        )

        where = _make_where_func(func, original_name)
        where.__doc__ = (
            'Returns a selector that filters for elements belonging to this '
            'function whose fields have the values of the given arguments.'
        )
        with_ = _make_with_func(func, original_name)
        with_.__doc__ = (
            'Returns a new function that has the given arguments pre-applied.'
        )

        attach_func(where, 'where')(func)
        attach_func(with_, 'with_')(func)
        return func

    return wrapper


def temporary(func: Callable[..., Any]) -> Callable[..., Any]:
    """Mark a function that is generated from function factory in module `customizations`.

    Args:
        func: The function to be marked.

    Returns:
        The marked function.
    """
    Implement.temporary.add(func)
    return func
