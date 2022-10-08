from helper.Player import Player 
from helper.Team import Team 
from helper.Game import Game 

p1 = Player("p_a", score = 81)
p2 = Player("p_b", score = 79)
p3 = Player("p_c", score = 67)
p4 = Player("p_d", score = 50)
p5 = Player("p_e", score = 88)
p0 = Player("p_f", score = 75)
p6 = Player(name="Suat",   dob="1989", score=89)
p7 = Player(name="Gulsum", dob="1996", score=96) 

players = [p0, p1, p2, p3, p4, p5, p6, p7]

home = Team("Home team", chemistry_multiplier=0.6)
away = Team("Away team", chemistry_multiplier=0.4)


for i, player in enumerate( players ):
    if i%2:
        away.add_new_player(player)
    else:
        home.add_new_player(player)

print( f"Home: {home} vs {away} :Away" )
print(f"Home winning probaiblity is {home.winning_probability(away)}") 

print(f"Transferring {p6} from Home to Away")
home.transfer_player_to(p6, away)

#print(f"Transferring {p7} from Away to Home") 
#away.transfer_player_to(p7, home)

print(f"Home winning probaiblity is {home.winning_probability(away)}") 


print("\nGenerating a game:")
game_details = {"home": home, "away": away, "score": "4-2", "date":"Some Date"}
game = Game(game_details)
print( game )

print( f"Our guessed winning probabilities: {game.expected_win_prob}")
print( f"   Realized winning probabilities: {game.true_win_prob}")