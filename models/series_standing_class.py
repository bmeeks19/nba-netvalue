import pandas as pd

def process_scoreboard_data(scoreboard, teams_df):
    scoreboard_json = scoreboard.get_json()
    scoreboard_dict = scoreboard.get_dict()
    dfs = {}
    for result_set in scoreboard_dict['resultSets']:
        name = result_set['name']
        headers = result_set['headers']
        data = result_set['rowSet']
        dfs[name] = pd.DataFrame(data, columns=headers)

    series_standings_df = dfs['SeriesStandings']
    merged_df = merge_scoreboard_data(series_standings_df, teams_df)
    reorg_df = reorganize_dataframe(merged_df)
    sorted_df = add_home_net_wins_column(reorg_df)
    sorted_df = add_away_net_wins_column(sorted_df)
    sorted_df = sort_dataframe(sorted_df)
    return {'sorted_df': sorted_df}

def merge_scoreboard_data(series_standings_df, teams_df):
    merged_df = series_standings_df.merge(teams_df, left_on='HOME_TEAM_ID', right_on='id', suffixes=('_standings', '_home'))
    merged_df = merged_df.merge(teams_df, left_on='VISITOR_TEAM_ID', right_on='id', suffixes=('_home', '_visitor'))
    merged_df.drop(columns=['full_name_visitor','full_name_home', 'GAME_ID', 'id_home', 'id_visitor'], inplace=True)
    merged_df.rename(columns={'nickname_home': 'Home_Team','nickname_visitor': 'Away_Team', 'TEAM_NAME_home': 'HOME_TEAM_NAME', 'TEAM_NAME_visitor': 'VISITOR_TEAM_NAME'}, inplace=True)
    return merged_df

def reorganize_dataframe(merged_df):
    desired_columns = ['Home_Team', 'Away_Team', 'SERIES_LEADER', 'HOME_TEAM_WINS', 'HOME_TEAM_LOSSES', 'GAME_DATE_EST']
    return merged_df[desired_columns]

def sort_dataframe(reorg_df):
    return reorg_df.sort_values(by=['HOME_TEAM_NET_WINS', 'HOME_TEAM_LOSSES'], ascending=False)

def add_home_net_wins_column(sorted_df):
    sorted_df['HOME_TEAM_NET_WINS'] = sorted_df['HOME_TEAM_WINS'] - sorted_df['HOME_TEAM_LOSSES']
    return sorted_df

def add_away_net_wins_column(sorted_df):
    sorted_df['AWAY_TEAM_NET_WINS'] = sorted_df['HOME_TEAM_LOSSES'] - sorted_df['HOME_TEAM_WINS']
    return sorted_df
