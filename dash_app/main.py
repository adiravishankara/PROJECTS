# IMPORTS
import os
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import sys
from separation.UI import Puzzle_Seperation as ps

#SETTING UP THE APP
external_stylesheets = [dbc.themes.FLATLY, dbc.icons.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Common Tools
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(html.Img(src='assets/images/logo2.png', height='75px')),
            dbc.Col(dbc.NavbarBrand('Puzzle Solver', className='ms-2')),
        ],
            align='center',
            className='g-0',
        ),
    ]),
    color='#001A3D',
    dark=True
)

# LOAD UIs
separation_ui = ps()

tabs = dbc.Tabs([
    dbc.Tab(separation_ui.get_UI(), label='Separation')
], className="p-2 m-2")

# The defined layout
app.layout = html.Div([
    navbar,
    tabs,
])


# CALLBACKS
# @app.callback(
#     Output(),
#     Input())
# def my_func():
#     pass

@app.callback(
    Output('example_text', 'children'),
    Input('s_btn_group1', 'value')
)
def change_example_value(value):
    return value


if __name__ == '__main__':
    print(os.getcwd())
    app.run_server(debug=True)