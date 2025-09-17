import inspect
import warnings
from collections.abc import Callable, Iterable, Mapping
from functools import singledispatch
from io import StringIO
from typing import ClassVar, Self
from weakref import WeakKeyDictionary, WeakSet

from attrs import frozen
from cytoolz.curried import curry, keyfilter

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
            f'The function {obj} has not been registered. Use `implement` decorator to register it and set the correct original name.'
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
        _name = name if name else func.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}')
        setattr(func, _name, attached)
        return func

    return wrapper


@frozen
class _Implement:
    permanent: ClassVar[WeakKeyDictionary[Callable, Self]] = WeakKeyDictionary()
    temporary: ClassVar[WeakSet[Callable]] = WeakSet()

    original_name: str
    hyperlink: str | None = None
    version: str | None = None

    @staticmethod
    def implement_table():
        with StringIO() as stream:
            _print = curry(print, file=stream, sep='\n')
            _print(
                "| Package's function name | Typst's function name | Documentation on typst | Version |",
                '| --- | --- | --- | --- |',
            )
            _print(
                *(
                    f'| {k.__module__[len("typstpy.") :]}.{k.__name__} | {v.original_name} | [{v.hyperlink}]({v.hyperlink}) | {v.version} |'
                    for k, v in _Implement.permanent.items()
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
            for func in _Implement.permanent:
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
            assert kwargs.keys() <= func.__kwdefaults__.keys()

            return f'#{original_name}.where({_strip_brace(_render_value(kwargs))})'

        def with_(*args, **kwargs):
            """Returns a new function that has the given arguments pre-applied."""
            assert (not kwargs) or (kwargs.keys() <= func.__kwdefaults__.keys())

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
    assert kwargs.keys() <= func.__kwdefaults__.keys()

    return f'#set {_render_value(func)}({_strip_brace(_render_value(kwargs))})'


def show_(element, appearance, /):
    """Represent `show` rule in typst.

    Args:
        element: The typst function or content. If None, it means `show everything` rule.
        appearance: The typst function or content.

    Raises:
        ValueError: If the target is invalid.

    Returns:
        Executable typst code.
    """
    return f'#show {"" if element is None else _render_value(element)}: {_render_value(appearance)}'


def import_(path, /, *names):
    """Represent `import` operation in typst.

    Args:
        path: The path of the file to be imported.

    Returns:
        Executable typst code.
    """
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
    defaults = func.__kwdefaults__
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif func not in _Implement.temporary:
        assert not kwargs

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
    defaults = func.__kwdefaults__
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif func not in _Implement.temporary:
        assert not kwargs

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
    defaults = func.__kwdefaults__
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif func not in _Implement.temporary:
        assert not kwargs

    params = []
    if len(children) != 1:
        params.append(_strip_brace(_render_value(children)))
    else:
        params.append(f'..{_render_value(children[0])}')
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
    defaults = func.__kwdefaults__
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif func not in _Implement.temporary:
        assert not kwargs

    params = []
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))
    if len(children) != 1:
        params.append(_strip_brace(_render_value(children)))
    else:
        params.append(f'..{_render_value(children[0])}')

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
