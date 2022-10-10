from helper.Player import Player 
import math 

class Team:
    ## definition
    def __init__(self, name, chemistry_multiplier=0.3):
        self.name = name
        self.squad = set()
        self.chemistry_multiplier = chemistry_multiplier
        self.score = 100
        self.chemistry = chemistry_multiplier 
        self.total_games = 0 

    def __str__(self):
        return f"<name: {self.name} | multiplier: {self.chemistry_multiplier} | chemistry: {self.chemistry}>"

    def __eq__(self, other_name):
        if self.name == other_name:
            return True
        else:
            return False

    ## methods
    def validate_player(self, player):
        if player not in self.squad:
            assert( f"Player {player.name} is not in team {self.name}!")

    def update_chemistry(self):
        self.chemistry = self.score * self.chemistry_multiplier

    def add_new_player(self, player):
        if not player.team:
            self.squad.add( player )
            self.score += math.log(player.score)
            self.update_chemistry()
            player.team = self


    def remove_player(self, player) :
        self.validate_player(player)
        self.squad.remove( player )
        self.score -= math.log(player.score)
        self.update_chemistry()
        player.team = None

    def transfer_player_to(self, player, other_team):
        self.validate_player(player)
        self.remove_player(player)
        other_team.add_new_player(player)

    def winning_probability(self, other):
        if self.chemistry > other.chemistry:
            return 1 - (other.chemistry / self.chemistry)/2
        else:
            return (self.chemistry / other.chemistry)/2


if __name__ == "__main__":
    p1 = Player("p_a", score = 81)
    p2 = Player("p_b", score = 79)
    p3 = Player("p_c", score = 67)
    p4 = Player("p_d", score = 98)
    p5 = Player("p_e", score = 56)
    p6 = Player("p_f", score = 75)
    p7 = Player(name="Suat", dob="1989", score=89)
    p8 = Player(name="Gulsum", dob="1996", score=96) 

    players = [p1, p2, p3, p4, p5, p6, p7, p8]

    A = Team("Team A", chemistry_multiplier=0.4)
    B = Team("Team B", chemistry_multiplier=0.6)


    for i, player in enumerate( players ):
        if i%2:
            A.add_new_player(player)
        else:
            B.add_new_player(player)
    
    print( A )
    print( B )