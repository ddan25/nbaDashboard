from dash import Input, Output, callback
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

@callback(
    Output('player-stats-output', 'children'),
    Input('player-dropdown', 'value')
)
def update_stats(player_name):
    if not player_name:
        return "Select a player to see stats."

    stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2024-25').get_data_frames()[0]
    player_data = stats[stats['PLAYER_NAME'] == player_name]

    if player_data.empty:
        return "No data found."

    return f"{player_name} is averaging {player_data['PTS'].values[0]} points per game."
