# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
import datetime
import random
import plotly.subplots

from dash import Dash
from dash.dependencies import Input, State, Output
from .Dash_fun import apply_layout_with_auth, load_object, save_object
from dash import dcc
from dash import html

url_base = '/dash/app1/'

layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    ),
    html.Div('Temperature / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-temp'),

    html.Div('pH / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-ph'),

    html.Div('ORP / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-orp'),

    html.Div('EC / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-ec'),

    html.Div('Ammonia / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-ammonia'),

    html.Div('Nitrite / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-nitrite'),

    html.Div('Nitrate / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-nitrate'),

    html.Div('Oxygen / Time'), html.Br(),
    dcc.Graph(id='live-update-graph-oxygen')
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

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            temp = random.uniform(0, 25)

            data['Temperature'].append(temp)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-ph', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'pH': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            ph = random.uniform(100, 110)

            data['pH'].append(ph)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-orp', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'ORP': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            orp = random.uniform(1, 5) * i

            data['ORP'].append(orp)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-ec', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'EC': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            ec = random.uniform(1, 2)

            data['EC'].append(ec)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-ammonia', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Ammonia': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            ammonia = random.uniform(1, 5) * random.uniform(2, 3) * i

            data['Ammonia'].append(ammonia)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-nitrite', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Nitrite': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            nitrite = i

            data['Nitrite'].append(nitrite)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-nitrate', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Nitrate': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            nitrate = random.uniform(1, 1000)

            data['Nitrate'].append(nitrate)
            data['time'].append(time)

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

        return fig

    @app.callback(Output('live-update-graph-oxygen', 'figure'),
                  Input('interval-component', 'n_intervals'))
    def update_graph_live(n):

        data = {
            'time': [],
            'Oxygen': []
        }

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            oxygen = (i * i) / random.uniform(1, 10)

            data['Oxygen'].append(oxygen)
            data['time'].append(time)

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

        return fig
    
    return app.server
