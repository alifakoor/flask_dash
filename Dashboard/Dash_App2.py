import datetime
import pytz
import plotly.subplots
from app.base.models import Temperature, PH, EC, ORP, Ammonia, Nitrite, Nitrate, Oxygen
from flask_login import current_user
from dash import Dash
from dash.dependencies import Input, Output
from .Dash_fun import apply_layout_with_auth
from dash import dcc
from dash import html

url_base = '/dash/app2/'

timezone_iran = pytz.timezone('Asia/Tehran')

layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=120000,  # in milliseconds
        n_intervals=0
    ),
    html.Div('Temperature / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-temp', animate=True),

    html.Div('pH / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-ph', animate=True),

    html.Div('ORP / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-orp', animate=True),

    html.Div('EC / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-ec', animate=True),

    html.Div('Ammonia / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-ammonia', animate=True),

    html.Div('Nitrite / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-nitrite', animate=True),

    html.Div('Nitrate / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-nitrate', animate=True),

    html.Div('Oxygen / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-oxygen', animate=True)
])


def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    apply_layout_with_auth(app, layout)

    @app.callback(Output('live-update-graph-temp', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Temperature': []
        }

        temperatures = Temperature.query.filter_by(user_id=current_user.id).all()

        for temp in temperatures:
            data['Temperature'].append(temp.value)
            data['time'].append(temp.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['Temperature'],
            'name': 'Temperature',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Temperature", range=[0, 50])
        return fig

    @app.callback(Output('live-update-graph-ph', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'pH': []
        }

        phs = PH.query.filter_by(user_id=current_user.id).all()

        for ph in phs:
            data['pH'].append(ph.value)
            data['time'].append(ph.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['pH'],
            'name': 'pH',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="pH", range=[0, 14])

        return fig

    @app.callback(Output('live-update-graph-orp', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'ORP': []
        }

        orps = ORP.query.filter_by(user_id=current_user.id).all()

        for orp in orps:
            data['ORP'].append(orp.value)
            data['time'].append(orp.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['ORP'],
            'name': 'ORP',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="ORP", range=[0, 400])

        return fig

    @app.callback(Output('live-update-graph-ec', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'EC': []
        }

        ecs = EC.query.filter_by(user_id=current_user.id).all()

        for ec in ecs:
            data['EC'].append(ec.value)
            data['time'].append(ec.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['EC'],
            'name': 'EC',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="EC", range=[0, 4000])

        return fig

    @app.callback(Output('live-update-graph-ammonia', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Ammonia': []
        }

        ammonias = Ammonia.query.filter_by(user_id=current_user.id).all()

        for ammonia in ammonias:
            data['Ammonia'].append(ammonia.value)
            data['time'].append(ammonia.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['Ammonia'],
            'name': 'Ammonia',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Ammonia", range=[0, 2000])

        return fig

    @app.callback(Output('live-update-graph-nitrite', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Nitrite': []
        }

        nitrites = Nitrite.query.filter_by(user_id=current_user.id).all()

        for nitrite in nitrites:
            data['Nitrite'].append(nitrite.value)
            data['time'].append(nitrite.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['Nitrite'],
            'name': 'Nitrite',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Nitrite", range=[0, 50])

        return fig

    @app.callback(Output('live-update-graph-nitrate', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Nitrate': []
        }

        nitrates = Nitrate.query.filter_by(user_id=current_user.id).all()

        for nitrate in nitrates:
            data['Nitrate'].append(nitrate.value)
            data['time'].append(nitrate.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['Nitrate'],
            'name': 'Nitrate',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Nitrate", range=[0, 50])

        return fig

    @app.callback(Output('live-update-graph-oxygen', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Oxygen': []
        }

        oxygens = Oxygen.query.filter_by(user_id=current_user.id).all()

        for oxygen in oxygens:
            data['Oxygen'].append(oxygen.value)
            data['time'].append(oxygen.timestamp)

        # Create the graph with subplots
        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        fig['layout']['margin'] = {
            'l': 30, 'r': 10, 'b': 30, 't': 10
        }
        fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

        fig.append_trace({
            'x': data['time'],
            'y': data['Oxygen'],
            'name': 'Oxygen',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Oxygen", range=[0, 100])

        return fig

    return app.server
