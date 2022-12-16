from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc


class Puzzle_Seperation:
    def __init__(self):
        self.gen_UI()



    def gen_UI(self):
        print('Generating UI')
        self.UI = dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.Span('Click to import your puzzle file'), className='w-25'),
                        dbc.Col(dbc.Button('Import File', id='import-file', className='me-1', n_clicks=0)),
                    ], className='p-2'),
                    dbc.Row([ # COLOR MODE
                        dbc.Col(dbc.Switch(label='Step 1', id='s_switch_1')),
                        dbc.Col(dbc.ButtonGroup([
                            dbc.Button('BGR2RGB'),
                            dbc.Button('BGR2GRAY'),
                            dbc.Button('BGR2HSV'),
                        ], id='s_btn_group1'),)
                    ], className='p-2'), # END COLOR MODE
                    dbc.Row([ # THRESHOLDING
                        dbc.Col(dbc.Switch(label='Step 2', id='s_switch_2')),
                        dbc.Col(dcc.RangeSlider(min=0, max=255, step=1, value=[230, 255], marks=None,
                                                tooltip={'placement': 'bottom',
                                                         'always_visible': True}, id='s_r_slider1'))
                    ], className='p-2'), # END THRESHOLDING
                    dbc.Row([ # BLURRING
                        dbc.Col(dbc.Switch(label='Step 3', id='s_switch_3')),
                        dbc.Col(dcc.Slider(min=1, max=15, step=2, value=3, marks=None, tooltip={'placement': 'bottom', 'always_visible': True
                        }, id='s_r_slider2'))
                    ], className='p-2'), # END BLURRING
                    dbc.Row([ # FINDING CONTOURS
                        dbc.Row([ # CONTOUR RETRIEVAL
                            dbc.Col(dbc.Switch(label='Step 4', id='s_switch_4')),
                            dbc.Col(dbc.ButtonGroup([
                                dbc.Button('RETR_LIST'),
                                dbc.Button('RETR_EXTERNAL'),
                                dbc.Button('RETR_CCOMP'),
                                dbc.Button('RETR_TREE')
                            ], id='s_btn_group2'))
                        ]), # END CONTOUR RETRIEVAL
                        dbc.Row([ # CONTOUR CHAIN
                            dbc.Col([html.Span('Chain Approx')]),
                            dbc.Col(dbc.ButtonGroup([
                                dbc.Button('None'),
                                dbc.Button('Simple')
                            ], id='s_btn_group3'))
                        ]) # END CONTOUR CHAIN
                    ], className='p-2') # END FINDING CONTOURS
                ], className='border border-2 rounded-3 w-25 px-2 mx-2'),
                dbc.Col([
                    html.Span('This is a place holder', id='example_txt')
                ], className='border border-2 rounded-3 w-75 px-2 mx-2'),
            ], className='position-relative'),
        ], className='px-5 mx-2', fluid=True)

    def get_UI(self):
        return self.UI


def sep_app():
    print('Hello')


if __name__ == '__main__':
    app.run_server(debug=True)