# user-dashboard/main.py

from dash import Dash, dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash.exceptions import DuplicateOutputError
import pandas as pd

def create_app():
    app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    app.layout = html.Div([
        html.H1('User Dashboard'),
        html.Div([
            dcc.Dropdown(id='filter-dropdown', options=[
                {'label': 'Filter 1', 'value': 'filter1'},
                {'label': 'Filter 2', 'value': 'filter2'}
            ], value='filter1'),
            dcc.Graph(id='graph')
        ]),
        dash_table.DataTable(id='table')
    ])

    @app.callback(
        Output('graph', 'figure'),
        [Input('filter-dropdown', 'value')]
    )
    def update_graph(filter_value):
        if filter_value == 'filter1':
            # generate figure for filter 1
            return {
                'data': [{'x': [1, 2, 3], 'y': [4, 5, 6]}],
                'layout': {'title': 'Filter 1'}
            }
        elif filter_value == 'filter2':
            # generate figure for filter 2
            return {
                'data': [{'x': [7, 8, 9], 'y': [10, 11, 12]}],
                'layout': {'title': 'Filter 2'}
            }
        else:
            raise PreventUpdate

    @app.callback(
        Output('table', 'data'),
        [Input('filter-dropdown', 'value')]
    )
    def update_table(filter_value):
        if filter_value == 'filter1':
            # return data for filter 1
            return [{'column1': 1, 'column2': 2}, {'column1': 3, 'column2': 4}]
        elif filter_value == 'filter2':
            # return data for filter 2
            return [{'column1': 5, 'column2': 6}, {'column1': 7, 'column2': 8}]
        else:
            raise PreventUpdate

    return app