from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import sys

external_stylesheets = [dbc.themes.FLATLY, dbc.icons.BOOTSTRAP]

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

def navbar():
    html.Div([
        dbc.Container([
            dbc.Col(html.Img(src='assets/images/logo.png', height='30px'))])
    ])

app.layout = html.Div([
    navbar()
])

if __name__ == '__main__':
    app.run_server(debug=True)