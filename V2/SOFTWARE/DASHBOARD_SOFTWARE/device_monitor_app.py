from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_daq as daq
import json
import requests

external_stylesheets = [dbc.themes.FLATLY, dbc.icons.BOOTSTRAP, ]
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Center(html.H2('AWS Dashboard')), class_name='my-2')
    ]),
    dbc.Container([
        dbc.Row([

            # Column 1
            dbc.Col([
                # AWS SWITCH
                dbc.Row([
                    dbc.Switch(label='AWS CONNECTION STATUS', id='aws_switch', value=1)
                ], class_name='border rounded p-1 m-1'),
                # PICO SWITCH
                dbc.Row([
                    dbc.Switch(label='PICO CONNECTION STATUS', id='pico_switch', value=0)
                ], class_name='border rounded p-1 m-1'),

                # MOTOR CONTROLLER
                dbc.Row([
                    html.Center('Motor Control'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Switch(id='motor_switch', label='Motor On/Off', value=0, class_name='mx-auto'),
                            daq.Knob(label='Hour Hand', min=0, max=360, size=100, value=0, id='hour_knob'),
                            dbc.Row([html.Center(html.H3(113, id='hour_label'))]),
                        ], class_name='p-1 mx-auto', align='center'),
                        dbc.Col([
                            dbc.Switch(id='motor_switch_2', label='Motor On/Off', value=0, class_name='mx-auto'),
                            daq.Knob(label='Minute Hand', min=0, max=360, size=100, value=0, id='minute_knob'),
                            dbc.Row([html.Center(html.H3(113, id='minute_label'))]),
                        ], class_name='p-1 mx-auto', align='center'),
                    ], 'p-1 m-1')
                ], class_name='border rounded px-1 m-1')
            ], class_name='p-1 m-1 w-25'),

            # Column 2
            dbc.Col([
                dbc.Row([
                    dbc.Container([
                        html.Div(id='log-div', style={'height': '400px', 'overflow-y': 'scroll'}),
                    ], class_name='border rounded height p-1 m-1')
                ], align='start')
            ], class_name='p-2 m-2'),

            # Column 3
            dbc.Col([
                dbc.Container([
                    dbc.Switch(label='Ultrasonic Sensor Measurement'),
                    dbc.Row([daq.Thermometer(label='Current Ultrasonic Sensor Value', max=1024, min=0, scale={})]),
                ], class_name='p-1 m-1 border rounded-2 h-auto')
            ], class_name='p-2 m-2')
        ], class_name='shadow-md')
    ], class_name='border shadow-sm rounded-2', fluid=True)
], fluid=True)





@app.callback(
    Output('hour_label', 'children'),
    Input('hour_knob', 'value'))
def update_hour_label(value):
    return str(int(value))

@app.callback(
    Output('minute_label', 'children'),
    Input('minute_knob', 'value'))
def update_minute_label(value):
    return str(int(value))

@app.callback(
    Output('hour_knob', 'disabled'),
    Input('motor_switch', 'value'))
def hour_motor_control(value):
    if value:
        return False
    else:
        return True

@app.callback(
    Output('minute_knob', 'disabled'),
    Input('motor_switch_2', 'value'))
def minute_motor_control(value):
    if value:
        return False
    else:
        return True




if __name__ == '__main__':
    app.run_server(debug=True)