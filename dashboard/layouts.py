# dashboard/layouts.py

from dash import html, dcc

layout = html.Div([
    html.H1("NBA Dashboard"),
    dcc.Dropdown(id='player-dropdown', options=[], placeholder='Select a player'),
    html.Div(id='player-stats-output')
])
