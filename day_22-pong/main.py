from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() == 330 or ball.distance(l_paddle) < 60 and ball.xcor() == -330:
        ball.bounce_x()

    # Detect paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score("left")

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score("right")




screen.exitonclick()