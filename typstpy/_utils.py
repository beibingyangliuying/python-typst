import inspect
import warnings
from collections.abc import Callable, Iterable, Mapping
from functools import singledispatch
from io import StringIO
from typing import Any, ClassVar, Optional, Protocol, Self

from attrs import frozen
from cytoolz.curried import curry, keyfilter, memoize  # type: ignore

from typstpy.typings import Content

TypstFunc = Callable[..., Content]
Decorator = Callable[[TypstFunc], TypstFunc]


# region render


def _render_key(key: str, /) -> str:
    """Render a key into a valid typst parameter representation.

    Args:
        key: The key to be rendered.

    Returns:
        The rendered key.
    """
    return key.replace('_', '-')


@singledispatch
def _render_value(obj: object) -> str:
    return str(obj)


@_render_value.register
def _(obj: bool | None) -> str:
    return str(obj).lower()


@_render_value.register
def _(text: str) -> str:
    if text.startswith('#'):
        return text[1:]
    return text


@_render_value.register
def _(mapping: Mapping) -> str:
    if not mapping:
        return '(:)'
    return f'({', '.join(f'{_render_key(k)}: {_render_value(v)}' for k, v in mapping.items())})'


@_render_value.register
def _(iterable: Iterable) -> str:
    return f"({', '.join(_render_value(v) for v in iterable)})"


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


def attach_func(attached: TypstFunc, name: Optional[str] = None, /) -> Decorator:
    """Attach a typst function to another typst function.

    Args:
        attached: The function to attach.
        name: The attribute name to be set. When set to None, the function's name will be used. Defaults to None.

    Raises:
        ValueError: Invalid name.

    Returns:
        The decorator function.
    """

    def wrapper(func: TypstFunc) -> TypstFunc:
        _name = name if name else func.__name__
        if _name.startswith('_'):
            raise ValueError(f'Invalid name: {_name}')
        setattr(func, _name, attached)
        return func

    return wrapper


@frozen
class _Implement:
    _registry: ClassVar[dict[TypstFunc, Self]] = {}
    _temporary: ClassVar[set[TypstFunc]] = set()

    original_name: str
    hyperlink: str

    @staticmethod
    @memoize
    def get_original_name(func: TypstFunc, /) -> str:
        """Get the name representation in typst of a function.

        Args:
            func: The function to be retrieved.

        Returns:
            The name representation in typst.
        """
        implement = _Implement._registry.get(func, None)
        if implement is None:
            warnings.warn(
                f'The function {func} has not been registered. Use `implement` decorator to register it and set the correct original name.'
            )
            return func.__name__
        return implement.original_name

    @staticmethod
    def is_temporary(func: TypstFunc, /) -> bool:
        """_summary_

        Args:
            func: The function to be checked.

        Returns:
            _description_
        """
        return func in _Implement._temporary

    @staticmethod
    def implement_table() -> str:
        """_summary_

        Returns:
            _description_
        """
        with StringIO() as stream:
            _print = curry(print, file=stream, sep='\n')
            _print(
                "| Package's function name | Typst's function name | Documentation on typst |",
                '| --- | --- | --- |',
            )
            _print(
                *(
                    f'| {k.__module__[len('typstpy.'):]}.{k.__name__} | {v.original_name} | [{v.hyperlink}]({v.hyperlink}) |'
                    for k, v in _Implement._registry.items()
                ),
            )
            return stream.getvalue()

    @staticmethod
    def examples() -> str:
        """_summary_

        Returns:
            _description_
        """

        def extract_examples(func: TypstFunc) -> str | None:
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
            for func in _Implement._registry:
                examples = extract_examples(func)
                if examples is None:
                    continue

                print(
                    f'`{func.__module__[len('typstpy.'):]}.{func.__name__}`:',
                    '\n```python',
                    examples,
                    '```\n',
                    sep='\n',
                    file=stream,
                )
            return stream.getvalue()


def implement(original_name: str, hyperlink: str = '', /) -> Decorator:
    """Register a typst function and attach it with `where` and `with_` functions.

    Args:
        original_name: The original function name in typst.
        hyperlink: The hyperlink of the documentation in typst. Defaults to ''.

    Returns:
        The decorator function.
    """

    def wrapper(func: TypstFunc) -> TypstFunc:
        _Implement._registry[func] = _Implement(original_name, hyperlink)

        def where(**kwargs: Any) -> Content:
            assert kwargs.keys() <= func.__kwdefaults__.keys()

            return f'#{original_name}.where({_strip_brace(_render_value(kwargs))})'

        def with_(*args: Any, **kwargs: Any) -> Content:
            assert (not kwargs) or kwargs.keys() <= func.__kwdefaults__.keys()

            params = []
            if args:
                params.append(_strip_brace(_render_value(args)))
            if kwargs:
                params.append(_strip_brace(_render_value(kwargs)))

            return f'#{original_name}.with({', '.join(params)})'

        attach_func(where, 'where')(func)
        attach_func(with_, 'with_')(func)
        return func

    return wrapper


def temporary() -> Decorator:
    """Mark a function that is generated from function factory in module `customizations`.

    Returns:
        The decorator function.
    """

    def wrapper(func: TypstFunc) -> TypstFunc:
        _Implement._temporary.add(func)
        return func

    return wrapper


# endregion
# region protocols


def set_(func: TypstFunc, /, **kwargs: Any) -> Content:
    """Represent `set` rule in typst.

    Args:
        func: The typst function.

    Raises:
        ValueError: If there are invalid keyword-only parameters.

    Returns:
        Executable typst code.
    """
    assert kwargs.keys() <= func.__kwdefaults__.keys()

    return f'#set {_Implement.get_original_name(func)}({_strip_brace(_render_value(kwargs))})'


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
        _element = _Implement.get_original_name(element)
    else:
        _element = _render_value(element)

    if callable(appearance):
        _appearance = _Implement.get_original_name(appearance)
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


class Normal(Protocol):
    def __call__(self, body: Any, /, *args: Any, **kwargs: Any) -> Content: ...


def normal(
    func: Normal,
    body: Any = '',
    /,
    *args: Any,
    **kwargs: Any,
) -> Content:
    """Represent the protocol of `normal`.

    Args:
        func: The function to be represented.
        body: The core parameter, it will be omitted if set to ''. Defaults to ''.

    Returns:
        Executable typst code.
    """
    defaults = func.__kwdefaults__  # type: ignore
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif not _Implement.is_temporary(func):
        assert not kwargs

    params = []
    if body != '':
        params.append(_render_value(body))
    if args:
        params.append(_strip_brace(_render_value(args)))
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'#{_Implement.get_original_name(func)}(' + ', '.join(params) + ')'


class Positional(Protocol):
    def __call__(self, *args: Any) -> Content: ...


def positional(func: Positional, *args: Any) -> Content:
    """Represent the protocol of `positional`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    return f'#{_Implement.get_original_name(func)}{_render_value(args)}'


class Instance(Protocol):
    def __call__(self, instance: Content, /, *args: Any, **kwargs: Any) -> Content: ...


def instance(
    func: Instance, instance: Content, /, *args: Any, **kwargs: Any
) -> Content:
    """Represent the protocol of `pre_instance`.

    Args:
        func: The function to be represented.
        instance: The `instance` to call the function on.

    Returns:
        Executable typst code.
    """
    defaults = func.__kwdefaults__  # type: ignore
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif not _Implement.is_temporary(func):
        assert not kwargs

    params = []
    if args:
        params.append(_strip_brace(_render_value(args)))
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'{instance}.{_Implement.get_original_name(func)}(' + ', '.join(params) + ')'


class Series(Protocol):
    def __call__(self, *children: Any, **kwargs: Any) -> Content: ...


def pre_series(func: Series, *children: Any, **kwargs: Any) -> Content:
    """Represent the protocol of `pre_series`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    defaults = func.__kwdefaults__  # type: ignore
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif not _Implement.is_temporary(func):
        assert not kwargs

    params = []
    if len(children) != 1:
        params.append(_strip_brace(_render_value(children)))
    else:
        params.append(f'..{_render_value(children[0])}')
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))

    return f'#{_Implement.get_original_name(func)}(' + ', '.join(params) + ')'


def post_series(func: Series, *children: Any, **kwargs: Any) -> Content:
    """Represent the protocol of `post_series`.

    Args:
        func: The function to be represented.

    Returns:
        Executable typst code.
    """
    defaults = func.__kwdefaults__  # type: ignore
    if defaults:
        kwargs = keyfilter(lambda x: kwargs[x] != defaults[x], kwargs)
    elif not _Implement.is_temporary(func):
        assert not kwargs

    params = []
    if kwargs:
        params.append(_strip_brace(_render_value(kwargs)))
    if len(children) != 1:
        params.append(_strip_brace(_render_value(children)))
    else:
        params.append(f'..{_render_value(children[0])}')

    return f'#{_Implement.get_original_name(func)}(' + ', '.join(params) + ')'


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
