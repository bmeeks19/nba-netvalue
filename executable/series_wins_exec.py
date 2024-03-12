from nba_api.stats.endpoints import scoreboardv2
import datetime
from nba_api.stats.static import teams
import pandas as pd
from series_standing_class import process_scoreboard_data
from net_wins_dictionary import generate_net_wins_dictionary  # Import the function

pd.options.mode.chained_assignment = None

if __name__ == "__main__":
    teams_data = teams.get_teams()
    teams_df = pd.DataFrame(teams_data)
    today = datetime.date.today()
    scoreboard = scoreboardv2.ScoreboardV2(game_date=today)
    dfs = process_scoreboard_data(scoreboard, teams_df)
    sorted_df = dfs['sorted_df']
    net_wins_dict = generate_net_wins_dictionary(sorted_df)
    print("Net Wins Dictionary:")
    print(net_wins_dict)