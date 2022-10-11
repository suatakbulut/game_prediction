from helper.Team import Team 

class Game:

    def __init__(self, home=None, away=None, score=None, date=None, country=None, league=None, season=None, matchday=0 ):  

        self.home   = home
        self.away   = away
        self.score  = score 
        self.date   = date
        self.country = country
        self.league = league
        self.season = season
        self.matchday = matchday

        self.home.total_games += 1
        self.away.total_games += 1
        self.expected_win_prob = self.get_expected_win_prob()
        self.true_win_prob = self.get_true_win_prob() 
        self.loss  = self.calculate_loss()

    def __str__(self):
        return f"{self.country} {self.league} {self.season} {self.date} \n {self.home.name} {self.score} {self.away.name}"

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

    def calculate_loss(self):
        '''
        true = self.true_win_prob 
        est = self.expected_win_prob
        loss = (true-est)**2 
        return loss 
        '''
        return 0