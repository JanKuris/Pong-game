from turtle import * 
from const import *

class Score(Turtle): 

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(DRAW_SCORE)
        self.penup()
        self.goto(SCORE_POSITION)
        self.pencolor(SCORE_COLOR)
        self.player_score = -1
        self.computer_score = -1
        self.get_score()
        self.set_computer_score()
        self.set_player_score()

    def get_score(self): 
        self.clear()
        self.write(f"{self.computer_score}:{self.player_score}", align= "center", font=("comic sans", 30))


    def set_player_score(self):
        self.player_score += 1 
        self.get_score()
    def set_computer_score(self):
        self.computer_score += 1 
        self.get_score()
