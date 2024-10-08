from const import *
from turtle import * 
import random

class Ball(Turtle): 

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(DRAW_BALL)
        self.penup()
        self.goto(BALL_POSITION)
        self.color(BALL_COLOR)
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.x_move = 10
        self.y_move = 10
        self.speed(BALL_SPEED)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 
    def bounce_x(self):
        self.x_move *= -1

    def new_ball(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        
   