class Player:
    ## definition
    def __init__(self, name, dob = "2000", score = 19):
        self.name = name
        self.dob = dob
        self.team = None
        self.score = score

    def __str__(self):
        return f"Player name: {self.name} - score: <{self.score}>" 

if __name__ == "__main__":
    p1 = Player(name="Suat", dob="1989", score=89)
    p2 = Player(name="Gulsum", dob="1996", score=96)
    p3 = Player(name="Goktan", dob="2000", score=99)
    p4 = Player(name="Ahmet", dob="1998", score=98)
    players = [p1, p2, p3, p4]
    for ind, player in enumerate(players):
        print(f"{ind+1}. {player}")