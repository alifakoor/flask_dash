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

url_base = '/dash/app2/'

layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=1 * 10000,  # in milliseconds
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

        # Collect some data
        for i in range(180):
            time = datetime.datetime.now() - datetime.timedelta(seconds=i * 20)
            temp = random.uniform(22, 25)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="Temperature", range=[0, 50], autorange=False)
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
            ph = random.uniform(7, 8)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="pH", range=[0, 14], autorange=False)

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
            orp = random.uniform(145, 150)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="ORP", range=[0, 400], autorange=False)

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
            ec = random.uniform(1357, 1387)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="EC", range=[0, 4000], autorange=False)

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
            ammonia = random.uniform(1455, 1470)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="Ammonia", range=[0, 2000], autorange=False)

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
            nitrite = random.uniform(11, 20)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="Nitrite", range=[0, 50], autorange=False)

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
            nitrate = random.uniform(30, 40)

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

        fig.update_xaxes(title_text="Time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="Nitrate", range=[0, 50], autorange=False)

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
            oxygen = random.uniform(50, 70)

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

        fig.update_xaxes(title_text="time", range=[data["time"][0], data["time"][179]], autorange=False)
        fig.update_yaxes(title_text="Oxygen", range=[0, 100], autorange=False)

        return fig

    return app.server
