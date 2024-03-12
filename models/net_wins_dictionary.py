def generate_net_wins_dictionary(sorted_df):
    net_wins_dict = {}
    for index, row in sorted_df.iterrows():
        home_team = row['Home_Team']
        away_team = row['Away_Team']
        home_net_wins = row['HOME_TEAM_NET_WINS']
        away_net_wins = row['AWAY_TEAM_NET_WINS']

        net_wins_dict[home_team] = home_net_wins
        net_wins_dict[away_team] = away_net_wins
    
    net_wins_list = [(team, net_wins) for team, net_wins in net_wins_dict.items()]
    sorted_net_wins = sorted(net_wins_list, key=lambda x: x[1], reverse=True)

    sorted_net_wins_dict = dict(sorted_net_wins)
    
    return sorted_net_wins_dict
