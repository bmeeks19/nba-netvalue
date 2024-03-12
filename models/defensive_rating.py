from nba_api.stats.endpoints import TeamEstimatedMetrics

# Define the parameters
params = {
    "LeagueID": "00",  # NBA
    "Season": "2023-24",
    "SeasonType": "Regular Season"
}

# Instantiate the TeamEstimatedMetrics endpoint
team_estimated_metrics = TeamEstimatedMetrics(
    league_id=params["LeagueID"],
    season=params["Season"],
    season_type=params["SeasonType"]
)

def net_rating_value(sorted_data):
    if sorted_data['E_NET_RATING'] > 7:
        return 3
    elif sorted_data['E_NET_RATING'] > 3:
        return 2
    elif sorted_data['E_NET_RATING'] > 0:
        return 1
    elif sorted_data['E_NET_RATING'] > -3:
        return -1
    elif sorted_data['E_NET_RATING'] > -7:
        return -2
    elif sorted_data['E_NET_RATING']:
        return -3
    return sorted_data['E_NET_RATING']


# Get the data set
team_estimated_metrics_data = team_estimated_metrics.get_data_frames()[0]

sorted_data = team_estimated_metrics_data.sort_values(by='E_NET_RATING', ascending=False)

selected_columns = ['TEAM_NAME', 'E_NET_RATING']
selected_data = team_estimated_metrics_data[selected_columns]
sorted_data['NET_RATING'] = sorted_data.apply(net_rating_value, axis=1)

# Display the updated data
print(sorted_data.columns)
print(sorted_data[['TEAM_NAME', 'E_NET_RATING', 'NET_RATING', 'TEAM_ID']])