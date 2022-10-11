from itertools import count
from helper.Player import Player 
from helper.Team import Team 
from helper.Game import Game 
from helper.match_info import *
from helper.utils import *

data_folder = "./data"  

games = []
country_folders = get_countries_from_data( data_folder )
for country_folder in country_folders: 
    country = get_country(country_folder)
    season_folders = get_seasons_from_country( country_folder )
    for season_folder in season_folders: 
        season = get_season(season_folder) 
        leagues = get_leagues_from_season( season_folder ) 
        for league_txt_file in leagues: 
            league = get_league(league_txt_file)
            games = obtain_games_in_league( league_txt_file, games = games, country=country, season=season, league=league)

print("\nTotal num of Games:", len(games) )
print("Total num of Teams:", len(teams) )
print("\nA few selected games:")
for ind in (34000, 24567, 65000, 867):
    print( games[ind] )

