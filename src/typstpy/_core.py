import inspect
import warnings
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from functools import partial, singledispatch
from io import StringIO
from typing import ClassVar, Self
from weakref import WeakKeyDictionary, WeakSet

# region render


def _render_key(key):
    return key.replace('_', '-')


@singledispatch
def _render_value(obj):
    return str(obj)


@_render_value.register
def _(obj: bool | None):
    return str(obj).lower()


@_render_value.register
def _(obj: str):
    if obj.startswith('#'):
        return obj[1:]
    return obj


@_render_value.register
def _(obj: Mapping):
    if not obj:
        return '(:)'
    return f'({", ".join(f"{_render_key(k)}: {_render_value(v)}" for k, v in obj.items())})'


@_render_value.register
def _(obj: Iterable):
    return f'({", ".join(_render_value(v) for v in obj)})'


@_render_value.register
def _(obj: Callable):
    implement = _Implement.permanent.get(obj, None)
    if implement is None:
        warnings.warn(
            f'The function {obj} has not been registered. Use `implement` decorator to register it and set the correct original name.',
            stacklevel=2,
        )
        return obj.__name__
    return implement.original_name


def _strip_brace(value):
    return value[1:-1]


# endregion
# region decorators


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


@dataclass(frozen=True)
class _Implement:
    permanent: ClassVar[WeakKeyDictionary[Callable, Self]] = WeakKeyDictionary()
    temporary: ClassVar[WeakSet[Callable]] = WeakSet()

    original_name: str
    hyperlink: str | None = None
    version: str | None = None

    @staticmethod
    def implement_table():
        with StringIO() as stream:
            _print = partial(print, file=stream, sep='\n')
            _print(
                "| Package's function name | Typst's function name | Documentation on typst | Version |",
                '| --- | --- | --- | --- |',
            )
            _print(
                *(
                    f'| {k.__module__[len("typstpy.") :]}.{k.__name__} | {v.original_name} | [{v.hyperlink}]({v.hyperlink}) | {v.version} |'
                    for k, v in sorted(
                        _Implement.permanent.items(),
                        key=lambda item: (item[0].__module__, item[0].__name__),
                    )
                ),
            )
            return stream.getvalue()

    @staticmethod
    def code_examples():
        def extract_examples(func):
            docstring = inspect.getdoc(func)
            if not docstring:
                return None

            sign_start = 'Examples:'
            if sign_start not in docstring:
                return None
            index_start = docstring.index(sign_start) + len(sign_start) + 1

            sign_end = 'See also:'
            index_end = docstring.index(sign_end) if sign_end in docstring else None

            examples = (
                docstring[index_start:index_end]
                if index_end
                else docstring[index_start:]
            )
            return '\n'.join(i.lstrip() for i in examples.splitlines())

        with StringIO() as stream:
            for func in sorted(
                _Implement.permanent,
                key=lambda item: (item.__module__, item.__name__),
            ):
                examples = extract_examples(func)
                if examples is None:
                    continue

                print(
                    f'`{func.__module__[len("typstpy.") :]}.{func.__name__}`:',
                    '\n```python',
                    examples,
                    '```\n',
                    sep='\n',
                    file=stream,
                )
            return stream.getvalue()


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


def _function_label(func):
    implement = _Implement.permanent.get(func, None)
    if implement is not None:
        return implement.original_name
    return getattr(func, '__name__', repr(func))


def _keyword_defaults(func):
    return func.__kwdefaults__ or {}


def _raise_unknown_fields(func, kwargs):
    defaults = _keyword_defaults(func)
    invalid = sorted(set(kwargs) - set(defaults))
    if invalid:
        fields = ', '.join(invalid)
        raise TypeError(f'{_function_label(func)} does not accept field(s): {fields}')


def _validate_value(func, name, value, allowed):
    if value not in allowed:
        choices = ', '.join(repr(choice) for choice in sorted(allowed, key=repr))
        raise ValueError(
            f'{_function_label(func)} got invalid {name}={value!r}; expected one of: {choices}'
        )


def _filter_default_kwargs(func, kwargs):
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


def _should_spread_single_child(func, child):
    if isinstance(child, str) and child.startswith(_SPREADABLE_CODE_PREFIXES):
        return True
    if isinstance(child, list | tuple):
        return _function_label(func) in _SPREAD_SINGLE_SEQUENCE_FUNCTIONS
    return False


def _render_series_children(func, children):
    if not children:
        return []
    if len(children) == 1:
        child = children[0]
        if _should_spread_single_child(func, child):
            return [f'..{_render_value(child)}']
        return [_render_value(child)]
    return [_strip_brace(_render_value(children))]


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


# endregion
# region protocols


def set_(func, /, **kwargs):
    """Represent `set` rule in typst.

    Args:
        func: The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        Executable typst code.
    """
    if func not in _Implement.temporary:
        _raise_unknown_fields(func, kwargs)

    params = _strip_brace(_render_value(kwargs)) if kwargs else ''
    return f'#set {_render_value(func)}({params})'


def show_(element, appearance, /):
    """Represent `show` rule in typst.

    Args:
        element: The typst function or content. If None, it means `show everything` rule.
        appearance: The typst function or content.

    Raises:
        ValueError: If the target is invalid.

    Returns:
        Executable typst code.

    Examples:
        >>> show_(None, 'it => it')
        '#show: it => it'
    """
    if element is None:
        return f'#show: {_render_value(appearance)}'
    return f'#show {_render_value(element)}: {_render_value(appearance)}'


def import_(path, /, *names):
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
    func,
    body='',
    /,
    *args,
    **kwargs,
):
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


def positional(func, *args):
    """Represent the protocol of `positional`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    return f'#{_render_value(func)}{_render_value(args)}'


def instance(func, instance, /, *args, **kwargs):
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


def pre_series(func, *children, **kwargs):
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


def post_series(func, *children, **kwargs):
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


# endregion

__all__ = [
    'attach_func',
    'implement',
    'temporary',
    'set_',
    'show_',
    'import_',
    'normal',
    'positional',
    'instance',
    'pre_series',
    'post_series',
]
