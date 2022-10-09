from helper.Player import Player 
from helper.Team import Team 
from helper.Game import Game 
from helper.match_info import *


data_folder = "./data"  

country_folders = get_countries_from_data( data_folder )
country_folder = country_folders[0]

season_folders = get_seasons_from_country( country_folder )
season_folder = season_folders[0]

leagues = get_leagues_from_season( season_folder ) 
league_txt_file = leagues[0] 

print( league_txt_file )

games = obtain_games_in_league( league_txt_file )