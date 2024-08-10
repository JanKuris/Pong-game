from turtle import * 
from const import * 
from playground import Playground
from game_elements.rackets import PongRacket
from game_elements.ball import Ball


playground = Playground()
racket_1 = PongRacket()
racket_2 = PongRacket()
ball = Ball()

game_run = True
screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width= SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen.listen()
screen.onkey(racket_1.up, "Up")
screen.onkey(racket_1.down, "Down") 
playground.drawing_border()
playground.drawing_mid()
racket_1.player_racket()
racket_2.computer_racket()

while game_run:
    
    screen.update()
    ball.move()

    #detect colision with ball
    if ball.ycor() > SCREEN_HEIGHT / 2 or ball.ycor() <  -SCREEN_HEIGHT / 2: 
        ball.bounce_y()
    if ball.distance(racket_1) < 50 and abs(ball.xcor() - racket_1.xcor()) < 20: 
        ball.bounce_x()
    elif ball.distance(racket_2) < 50 and abs(ball.xcor() - racket_2.xcor()) < 20: 
        ball.bounce_x()

