from helper.Team import Team 

class Game:
    def __init__(self, game_details ):  
        self.home   = game_details["home"]
        self.away   = game_details["away"]
        self.score  = game_details["score"]
        self.date   = game_details["date"]
        
        self.expected_win_prob = self.get_expected_win_prob()
        self.true_win_prob = self.get_true_win_prob()

    def __str__(self):
        return f"At {self.date}: {self.home.name} {self.score} {self.away.name}"

    def get_winner(self):
        h, a = [ int(s) for s in self.score.split("-") ]
        if h > a:
            return self.home 
        elif a > h:
            return self.away 
        else:
            return "Draw"

    
    def get_true_win_prob(self):
        h, a = [ int(s) for s in self.score.split("-") ]
        total_goals = h + a 
        if total_goals:
            return [ h/total_goals, a/total_goals ]
        else:
            return [ 1/2, 1/2 ]

    def get_expected_win_prob(self):
        home_wins = self.home.winning_probability(self.away)
        return [ home_wins, 1-home_wins ]
