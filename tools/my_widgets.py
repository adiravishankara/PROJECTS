from ipywidgets import widgets


def dropdown(option, default, description):
    return widgets.Dropdown(
        options=option,
        value=default,
        description=description,
    )


def slider_setup(description, disabled=False):
    return widgets.IntRangeSlider(
        value=[25, 220],
        min=0, max=255,
        step=1,
        continuous_update=True,
        orientation='vertical',
        readout=True,
        disabled=disabled,
        readout_format='d',
        description=description)

