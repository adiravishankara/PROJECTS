import ipywidgets as wid

class tools:
    def __init__(self):
        pass

    def get_dropdown(self, options, default, description):
        return wid.Dropdown(
            options=options,
            value=default,
            description=description)

    def get_int_slider(self, low=0, high=200, mini=0, maxi=255, orientation='vertical'):
        return wid.IntRangeSlider(
            value=[low, high],
            min=mini,
            max=maxi,
            step=1,
            continuous_update=True,
            orientation=orientation,
            readout=True,
            readout_format='d',
        )

