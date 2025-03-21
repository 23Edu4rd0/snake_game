from turtle import Turtle
ALLIGHMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scorebord()
        
    def update_scorebord(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALLIGHMENT, font=FONT)
        
        
        
    def incriase_score(self):
        self.score += 1
        self.update_scorebord()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scorebord()
        
        


