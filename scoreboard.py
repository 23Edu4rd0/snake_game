from turtle import Turtle
ALLIGHMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scorebord()
        
    def update_scorebord(self):
        self.write(f'Score: {self.score}', align=ALLIGHMENT, font=FONT)
        
        
    def incriase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebord()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align=ALLIGHMENT, font=FONT)

