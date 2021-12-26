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
    html.Div([
    dcc.Interval(
        id='interval-component',
        interval=120000,  # in milliseconds
        n_intervals=0
    ),
    html.Div([
        html.Div([
            html.Div([
                html.Div('Temperature / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-temp', animate=True, className='card-body'),
            ], className='card')
        ], className='col-12 col-md-8'),
        html.Div([
            html.Div([
                html.Div('Oxygen / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-oxygen', animate=True, className='card-body')
            ], className='card')
        ], className='col-12 col-md-4')
    ], className='row mb-3'),

    html.Div([
        html.Div([
            html.Div([
                html.Div('pH / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-ph', animate=True, className='card-body')
            ], className='card')

        ], className='col-12 col-md-4'),
        html.Div([
            html.Div([
                html.Div('EC / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-ec', animate=True, className='card-body')
            ], className='card')

        ], className='col-12 col-md-4'),
        html.Div([
            html.Div([
                html.Div('ORP / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-orp', animate=True, className='card-body')
            ], className='card')

        ], className='col-12 col-md-4'),
    ], className='row mb-3'),

    html.Div([
        html.Div([
            html.Div([
                html.Div('Ammonia / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-ammonia', animate=True, className='card-body')
            ], className='card')

        ], className='col-12 col-md-4'),
        html.Div([
            html.Div([
                html.Div('Nitrite / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-nitrite', animate=True, className='card-body')
            ], className='card')

        ], className='col-12 col-md-4'),
        html.Div([
            html.Div([
                html.Div('Nitrate / Time', className='card-header'),
                dcc.Graph(id='live-update-graph-nitrate', animate=True, className='card-body')
            ], className='card')

        ], className='col-12 col-md-4'),
    ], className='row')


], className='col-12 col-md-12')
], className='row', style={'width': '100%'})


def create_fig(data_x, data_y, name, bg_color, color):
    fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
    fig['layout']['plot_bgcolor'] = bg_color

    fig.append_trace({
        'x': data_x,
        'y': data_y,
        'name': name,
        'marker_color': color,
        'mode': 'lines+markers',
        'type': 'scatter',
    }, 1, 1)
    return fig

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    apply_layout_with_auth(app, layout)

    @app.callback(Output('live-update-graph-temp', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'temp': []
        }

        temperatures = Temperature.query.filter_by(user_id=current_user.id).all()

        for temp in temperatures:
            data['temp'].append(temp.value)
            data['time'].append(temp.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['Temperature'],
        #     'name': 'Temperature',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)
        fig = create_fig(data["time"], data["temp"], "Temperature", "#BE0713", "white")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        temp_range_min = min(data["temp"]) - 10
        temp_range_max = max(data["temp"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Temperature", range=[temp_range_min, temp_range_max])
        return fig

    @app.callback(Output('live-update-graph-ph', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'ph': []
        }

        phs = PH.query.filter_by(user_id=current_user.id).all()

        for ph in phs:
            data['ph'].append(ph.value)
            data['time'].append(ph.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['pH'],
        #     'name': 'pH',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["ph"], "pH", "#6E359D", "black")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        ph_range_min = min(data["ph"]) - 10
        ph_range_max = max(data["ph"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="pH", range=[ph_range_min, ph_range_max])

        return fig

    @app.callback(Output('live-update-graph-orp', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'orp': []
        }

        orps = ORP.query.filter_by(user_id=current_user.id).all()

        for orp in orps:
            data['orp'].append(orp.value)
            data['time'].append(orp.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['ORP'],
        #     'name': 'ORP',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["orp"], "ORP", "#CDD4E7", "black")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        orp_range_min = min(data["orp"]) - 10
        orp_range_max = max(data["orp"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="ORP", range=[orp_range_min, orp_range_max])

        return fig

    @app.callback(Output('live-update-graph-ec', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'ec': []
        }

        ecs = EC.query.filter_by(user_id=current_user.id).all()

        for ec in ecs:
            data['ec'].append(ec.value)
            data['time'].append(ec.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['EC'],
        #     'name': 'EC',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["ec"], "EC", "#19AE55", "black")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        ec_range_min = min(data["ec"]) - 10
        ec_range_max = max(data["ec"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="EC", range=[ec_range_min, ec_range_max])

        return fig

    @app.callback(Output('live-update-graph-ammonia', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'ammonia': []
        }

        ammonias = Ammonia.query.filter_by(user_id=current_user.id).all()

        for ammonia in ammonias:
            data['ammonia'].append(ammonia.value)
            data['time'].append(ammonia.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['Ammonia'],
        #     'name': 'Ammonia',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["ammonia"], "Ammonia", "#FCBE2E", "black")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        ammonia_range_min = min(data["ammonia"]) - 10
        ammonia_range_max = max(data["ammonia"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Ammonia", range=[ammonia_range_min, ammonia_range_max])

        return fig

    @app.callback(Output('live-update-graph-nitrite', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'nitrite': []
        }

        nitrites = Nitrite.query.filter_by(user_id=current_user.id).all()

        for nitrite in nitrites:
            data['nitrite'].append(nitrite.value)
            data['time'].append(nitrite.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['Nitrite'],
        #     'name': 'Nitrite',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["nitrite"], "Nitrite", "#FDD66E", "black")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        nitrite_range_min = min(data["nitrite"]) - 10
        nitrite_range_max = max(data["nitrite"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Nitrite", range=[nitrite_range_min, nitrite_range_max])

        return fig

    @app.callback(Output('live-update-graph-nitrate', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'nitrate': []
        }

        nitrates = Nitrate.query.filter_by(user_id=current_user.id).all()

        for nitrate in nitrates:
            data['nitrate'].append(nitrate.value)
            data['time'].append(nitrate.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['Nitrate'],
        #     'name': 'Nitrate',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["nitrate"], "Nitrate", "#F6CAAF", "black")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        nitrate_range_min = min(data["nitrate"]) - 10
        nitrate_range_max = max(data["nitrate"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Nitrate", range=[nitrate_range_min, nitrate_range_max])

        return fig

    @app.callback(Output('live-update-graph-oxygen', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'oxygen': []
        }

        oxygens = Oxygen.query.filter_by(user_id=current_user.id).all()

        for oxygen in oxygens:
            data['oxygen'].append(oxygen.value)
            data['time'].append(oxygen.timestamp)

        # Create the graph with subplots
        # fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
        # fig['layout']['margin'] = {
        #     'l': 30, 'r': 10, 'b': 30, 't': 10
        # }
        # fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
        #
        # fig.append_trace({
        #     'x': data['time'],
        #     'y': data['Oxygen'],
        #     'name': 'Oxygen',
        #     'mode': 'lines+markers',
        #     'type': 'scatter'
        # }, 1, 1)

        fig = create_fig(data["time"], data["oxygen"], "Oxygen", "#1DB1ED", "white")

        time_range_min = data["time"][0] - datetime.timedelta(seconds=300)
        time_range_max = data["time"][len(data["time"]) - 1] + datetime.timedelta(seconds=300)

        oxygen_range_min = min(data["oxygen"]) - 10
        oxygen_range_max = max(data["oxygen"]) + 10

        fig.update_xaxes(title_text="Time", range=[time_range_min, time_range_max])
        fig.update_yaxes(title_text="Oxygen", range=[oxygen_range_min, oxygen_range_max])

        return fig

    return app.server
