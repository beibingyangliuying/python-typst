# Version: 0.2.0

from typstpy._core import implement, pre_series
from typstpy.std import figure, image  # noqa


@implement('subpar.grid', 'https://typst.app/universe/package/subpar')
def grid(
    *children,
    columns='auto',
    rows='auto',
    gutter='1em',
    column_gutter='auto',
    row_gutter='auto',
    align='bottom',
    inset={},
    kind='image',
    numbering='"1"',
    numbering_sub='"(a)"',
    numbering_sub_ref='"1a"',
    supplement='auto',
    propagate_supplement=True,
    caption=None,
    placement=None,
    scope='"column"',
    gap='0.65em',
    outlined=True,
    outlined_sub=False,
    label=None,
    show_sub='auto',
    show_sub_caption='auto',
):
    """Interface of `subpar.grid` in typst. See [the documentation](https://typst.app/universe/package/subpar) for more information.

    Args:
        columns: _description_. Defaults to 'auto'.
        rows: _description_. Defaults to 'auto'.
        gutter: _description_. Defaults to '1em'.
        column_gutter: _description_. Defaults to 'auto'.
        row_gutter: _description_. Defaults to 'auto'.
        align: _description_. Defaults to 'bottom'.
        inset: _description_. Defaults to {}.
        kind: _description_. Defaults to 'image'.
        numbering: _description_. Defaults to '"1"'.
        numbering_sub: _description_. Defaults to '"(a)"'.
        numbering_sub_ref: _description_. Defaults to '"1a"'.
        supplement: _description_. Defaults to 'auto'.
        propagate_supplement: _description_. Defaults to True.
        caption: _description_. Defaults to None.
        placement: _description_. Defaults to None.
        scope: _description_. Defaults to '"column"'.
        gap: _description_. Defaults to '0.65em'.
        outlined: _description_. Defaults to True.
        outlined_sub: _description_. Defaults to False.
        label: _description_. Defaults to None.
        show_sub: _description_. Defaults to 'auto'.
        show_sub_caption: _description_. Defaults to 'auto'.

    Returns:
        Executable typst code.

    Examples:
        >>> grid(
        ...     figure(image('"image.png"')),
        ...     '<a>',
        ...     figure(image('"image.png"')),
        ...     '<b>',
        ...     columns=('1fr', '1fr'),
        ...     caption='[A figure composed of two sub figures.]',
        ...     label='<full>',
        ... )
        '#subpar.grid(figure(image("image.png")), <a>, figure(image("image.png")), <b>, columns: (1fr, 1fr), caption: [A figure composed of two sub figures.], label: <full>)'
    """
    return pre_series(
        grid,
        *children,
        columns=columns,
        rows=rows,
        gutter=gutter,
        column_gutter=column_gutter,
        row_gutter=row_gutter,
        align=align,
        inset=inset,
        kind=kind,
        numbering=numbering,
        numbering_sub=numbering_sub,
        numbering_sub_ref=numbering_sub_ref,
        supplement=supplement,
        propagate_supplement=propagate_supplement,
        caption=caption,
        placement=placement,
        scope=scope,
        gap=gap,
        outlined=outlined,
        outlined_sub=outlined_sub,
        label=label,
        show_sub=show_sub,
        show_sub_caption=show_sub_caption,
    )
