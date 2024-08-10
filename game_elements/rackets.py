from turtle import * 
from const import * 

class PongRacket(Turtle):

    def __init__(self):
        super().__init__()
        self.player_racket()
        self.computer_racket()

    def player_racket(self):
        self.shape("square")
        self.speed(DRAW_PLAYER)
        self.penup()
        self.goto(PLAYER_POSITION)
        self.color(PLAYER_COLOR)
        self.shapesize(stretch_wid= 5, stretch_len= 1)

    def down(self):
        new_y =  self.ycor() - 20
        self.goto(self.xcor(), new_y)
    def up(self):
        new_y =  self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def computer_racket(self):
        self.shape("square")
        self.speed(DRAW_COMPUTER)
        self.penup()
        self.goto(COMPUTER_POSITION)
        self.color(COMPUTER_COLOR)
        self.shapesize(stretch_wid= 5, stretch_len= 1)