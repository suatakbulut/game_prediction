import os 
import re 
from helper.Game import Game 
from helper.Team import Team 

def get_countries_from_data( data_folder ):
    country_folders = [ f.path for f in os.scandir( data_folder ) if f.is_dir() ]
    return country_folders


def get_seasons_from_country( country_folder ):
    season_folders = [ f.path for f in os.scandir( country_folder ) if f.is_dir() and "-" in f.path.split("/")[-1] ]
    return season_folders

def get_leagues_from_season( season_folder ):
    leagues = [os.path.join(season_folder, f) for f in os.listdir( season_folder ) if f.endswith('.txt') ]
    return leagues 

teams = {}

def validate_create__team(team_name): 
    team_name = team_name.strip() 
    if team_name not in teams.keys():
        team = Team(name = team_name)
        teams[team_name] = team 
        return team 
    else: 
        return teams[team_name]

def obtain_game_in_line( line ): 
    pattern = re.compile("(.*)(\d+\-\d+)(.*)")
    x = re.match( pattern, line)
    if x:
        home = validate_create__team( x.group(1) )
        away = validate_create__team( x.group(3) )
        score = x.group(2)
        date = "2022_10_08" 
        return Game( {"home" : home, "score" : score, "away" : away, "date" : date} ) 
   

def obtain_games_in_league( league_txt_file , games = []):
    textfile = open(league_txt_file, 'r')
    for line in textfile:
        game = obtain_game_in_line( line ) 
        if game:
            games.append( game )
    textfile.close()
    return games 
    

