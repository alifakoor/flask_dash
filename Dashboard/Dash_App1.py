import datetime
import random
import plotly.subplots

from dash import Dash
from dash.dependencies import Input, State, Output
from .Dash_fun import apply_layout_with_auth, load_object, save_object
from dash import dcc
from dash import html

url_base = '/dash/app1/'


def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    # apply_layout_with_auth(app, layout)

    # data = {
    #     'time': [],
    #     'temperature': []
    # }
    #
    # # Collect some data
    # for i in range(1000):
    #     time = datetime.datetime.now() - datetime.timedelta(seconds=(100 - i) * 2)
    #     temp = random.uniform(22, 25)
    #
    #     data['temperature'].append(temp)
    #     data['time'].append(time)


    layout = html.Div([
        dcc.Interval(
            id='interval-component',
            interval=1000,
            n_intervals=0
        ),
        dcc.Interval(
            id='interval-temp',
            interval=100,
            n_intervals=0
        ),
        html.Div('Temperature / Time'), html.Br(),
        dcc.Graph(id='temp'),
        dcc.Store(id='store'),
        dcc.Store(id='offset', data=0)
    ])

    app.layout = layout

    @app.callback(Output('store', 'data'),
                  Input('interval-component', 'n_intervals'))
    def store_data(n):
        data = {
            'time': [],
            'temperature': []
        }

        # Collect some data
        for i in range(100):
            time = datetime.datetime.now() - datetime.timedelta(seconds=(100 - i) * 2)
            temp = random.uniform(22, 25)

            data['temperature'].append(temp)
            data['time'].append(time)

        return data


    app.clientside_callback(
        """
        function(n, data, offset) {
            offset += 10
            return [{
                "data": [
                    {
                        "x": data["time"],
                        "y": data["temperature"]
                    }
                ],
                "layout": {
                    "xaxis": { "range": [data["time"][offset - 10], data["time"][offset]] },
                    "yaxis": { "range": [0, 50] }
                }
            },
            offset
            ]
        }
        """,
        [Output('temp', 'figure'), Output('offset', 'data')],
        Input('interval-temp', 'n_intervals'),
        Input('store', 'data'),
        Input('offset', 'data')
    )
    
    return app.server
