from helper.Player import Player 
from helper.Team import Team 
from helper.Game import Game 
from helper.match_info import *


data_folder = "./data"  

games = []
country_folders = get_countries_from_data( data_folder )
for country_folder in country_folders: 
    season_folders = get_seasons_from_country( country_folder )
    for season_folder in season_folders: 
        leagues = get_leagues_from_season( season_folder ) 
        for league_txt_file in leagues: 
            games = obtain_games_in_league( league_txt_file, games = games)

print( len(games) )