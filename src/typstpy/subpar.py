# Version: 0.2.0

from typstpy._core import implement, pre_series
from typstpy.std import figure, image  # noqa


@implement(
    'subpar.grid',
    hyperlink='https://typst.app/universe/package/subpar',
    spread_single=True,
)
def grid(
    *children,
    columns='auto',
    rows='auto',
    gutter='1em',
    column_gutter='auto',
    row_gutter='auto',
    align='bottom',
    inset=dict(),
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
) -> str:
    """Interface of `subpar.grid` in typst. See [the documentation](https://typst.app/universe/package/subpar) for more information.

    Args:
        columns: The column sizes for the subfigure grid. Defaults to 'auto'.
        rows: The row sizes for the subfigure grid. Defaults to 'auto'.
        gutter: The default gap between rows and columns. Defaults to '1em'.
        column_gutter: The gap between columns. Defaults to 'auto'.
        row_gutter: The gap between rows. Defaults to 'auto'.
        align: The alignment of subfigures within their cells. Defaults to 'bottom'.
        inset: Cell inset configuration. Defaults to dict().
        kind: The figure kind used for the composed figure. Defaults to 'image'.
        numbering: Numbering pattern for the composed figure. Defaults to '"1"'.
        numbering_sub: Numbering pattern for subfigures. Defaults to '"(a)"'.
        numbering_sub_ref: Reference numbering pattern for subfigures. Defaults to '"1a"'.
        supplement: Supplement for the composed figure. Defaults to 'auto'.
        propagate_supplement: Whether to propagate the supplement to subfigures. Defaults to True.
        caption: Caption for the composed figure. Defaults to None.
        placement: Placement of the composed figure. Defaults to None.
        scope: Placement scope for the composed figure. Defaults to '"column"'.
        gap: Gap between the composed figure body and caption. Defaults to '0.65em'.
        outlined: Whether the composed figure appears in an outline. Defaults to True.
        outlined_sub: Whether subfigures appear in an outline. Defaults to False.
        label: Label for the composed figure. Defaults to None.
        show_sub: How subfigure labels are shown. Defaults to 'auto'.
        show_sub_caption: How subfigure captions are shown. Defaults to 'auto'.

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


__all__ = ['grid']
