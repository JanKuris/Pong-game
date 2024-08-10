from turtle import * 
from const import * 

class Playground(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(DRAW_BORDER)
        self.pensize(LINE_THICK)
        self.color(BORDER_COLOR)
    
    def drawing_border(self):
        self.penup()
        self.hideturtle()
        self.goto(-SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 5)
        self.pendown()
        for line in range(2):
            self.pendown()
            self.forward(SCREEN_WIDTH)
            self.right(90)
            self.penup()
            self.forward(SCREEN_HEIGHT - 13) 
            self.right(90)

    def drawing_mid(self):
        self.penup()
        self.hideturtle()
        self.goto(0, SCREEN_HEIGHT / 2)
        self.pendown()
        self.right(90)
        self.forward(SCREEN_HEIGHT)