from turtle import * 
from const import *
from game_elements.playground import Playground
from game_elements.rackets import PongRacket
from game_elements.ball import Ball
from game_elements.score import Score

playground = Playground()
racket_1 = PongRacket()
racket_2 = PongRacket()
ball = Ball()
score = Score()

game_run = True
screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width= SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen.listen()
screen.onkey(racket_1.up, "Up")
screen.onkey(racket_1.down, "Down") 
playground.drawing_bounds()
playground.drawing_mid()
racket_1.player_racket()
racket_2.computer_racket()

while game_run:
    screen.update()
    ball.move()

     # Computer racket (racket_2) behavior - follow the ball
    if racket_2.ycor() < ball.ycor() and abs(racket_2.ycor() - ball.ycor()) > 10:
        racket_2.sety(racket_2.ycor() + C0MPUTER_SPEED)
    elif racket_2.ycor() > ball.ycor() and abs(racket_2.ycor() - ball.ycor()) > 10:
        racket_2.sety(racket_2.ycor() - C0MPUTER_SPEED)

      #detect colision with ball
    if ball.ycor() > SCREEN_HEIGHT / 2 - 20 or ball.ycor() <  -SCREEN_HEIGHT / 2 + 20: 
        ball.bounce_y()
    elif ball.distance(racket_1) < 55 and abs(ball.xcor() - racket_1.xcor()) < 30: 
        ball.bounce_x()
    elif ball.distance(racket_2) < 55 and abs(ball.xcor() - racket_2.xcor()) < 30: 
        ball.bounce_x()
    #detect goal
    if ball.xcor() >= RIGHT_PART:
        score.set_computer_score()
        screen.update()       
        ball.new_ball()
    elif ball.xcor() <= LEFT_PART:
        score.set_player_score()
        screen.update()       
        ball.new_ball()
    #border limits 
    if racket_1.ycor() > UPPER_PART - 70:
        racket_1.sety(UPPER_PART - 70)
    elif racket_1.ycor() < LOWER_PART + 70:
        racket_1.sety(LOWER_PART + 70)
    elif racket_2.ycor() > UPPER_PART - 70:
        racket_2.sety(UPPER_PART - 70)
    elif racket_2.ycor() < LOWER_PART + 70:
        racket_2.sety(LOWER_PART + 70)