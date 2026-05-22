from .registry import _Implement, _raise_unknown_fields
from .render import _render_value, _strip_brace


def attach_func(attached, name=None):
    """Attach a typst function to another typst function.

    Args:
        attached: The function to attach.
        name: The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Raises:
        ValueError: Invalid name.

    Returns:
        The decorator function.
    """

    def wrapper(func):
        _name = name if name else attached.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}')
        setattr(func, _name, attached)
        return func

    return wrapper


def implement(original_name, *, hyperlink=None, version=None):
    """Register a typst function and attach it with `where` and `with_` functions.

    Args:
        original_name: The original function name in typst.
        hyperlink: The hyperlink of the documentation in typst. Defaults to None.
        version: The current supported version. Defaults to None.

    Returns:
        The decorator function.
    """

    def wrapper(func):
        _Implement.permanent[func] = _Implement(original_name, hyperlink, version)

        def where(**kwargs):
            """Returns a selector that filters for elements belonging to this function whose fields have the values of the given arguments."""
            if func not in _Implement.temporary:
                _raise_unknown_fields(func, kwargs)

            params = _strip_brace(_render_value(kwargs)) if kwargs else ''
            return f'#{original_name}.where({params})'

        def with_(*args, **kwargs):
            """Returns a new function that has the given arguments pre-applied."""
            if func not in _Implement.temporary:
                _raise_unknown_fields(func, kwargs)

            params = []
            if args:
                params.append(_strip_brace(_render_value(args)))
            if kwargs:
                params.append(_strip_brace(_render_value(kwargs)))

            return f'#{original_name}.with({", ".join(params)})'

        attach_func(where, 'where')(func)
        attach_func(with_, 'with_')(func)
        return func

    return wrapper


def temporary(func):
    """Mark a function that is generated from function factory in module `customizations`.

    Args:
        func: The function to be marked.

    Returns:
        The marked function.
    """
    _Implement.temporary.add(func)
    return func
