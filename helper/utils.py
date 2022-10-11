import re 
import datetime as datetime 

def get_country(country_folder):
    c = country_folder.split("/")[-1] 
    return re.search( "[a-z]+", c).group(0).capitalize()

def get_league(league_txt_file):
    l = league_txt_file.split("/")[-1]  
    return re.search( "([\w]+).txt", l).group(1).capitalize()

def get_season(season_folder):
    return season_folder.split("/")[-1]  


def format_date(season, date):
    if "/" in season:
        season = season.replace("/", "-")
        
    y = int( season.split("-")[0] )
    a, b, d = [elt for elt in date.replace(" ", "/").split("/") if elt] 
    date_str = f"{y} {b} {d}"
    format_data = "%Y %b %d"
    date = datetime.strptime(date_str, format_data)
    
    if a == date.strftime("%a"):
        return date 
    else:
        y+=1 
        date_str = f"{y} {b} {d}"
        return datetime.strptime(date_str, format_data)


season = "2003/04"
date = "[Sat Aug/23]"

print( format_date(season, date) )