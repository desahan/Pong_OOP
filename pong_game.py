from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
SLEEP = 0.065

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0, "green")
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

l_paddle = Paddle(-350, 0, "cyan")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ping_pong = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(SLEEP)
    screen.update()
    ping_pong.move()

    # detect wall collision
    if ping_pong.ycor() > 280 or ping_pong.ycor() < -280:
        ping_pong.wall_bounce()

    # detect right paddle collision
    if ping_pong.distance(r_paddle) < 50 and ping_pong.xcor() > 320:
        ping_pong.paddle_bounce()
        ping_pong.color("green")

    # detect right paddle miss
    if ping_pong.xcor() > 420:
        ping_pong.right_miss()
        scoreboard.l_point()
        if SLEEP > 0.035:
            SLEEP -= 0.005

    # detect left paddle collision
    if ping_pong.distance(l_paddle) < 50 and ping_pong.xcor() < -320:
        ping_pong.paddle_bounce()
        ping_pong.color("cyan")

    # detect left paddle miss
    if ping_pong.xcor() < -420:
        ping_pong.left_miss()
        scoreboard.r_point()
        if SLEEP > 0.035:
            SLEEP -= 0.005

    if scoreboard.l_score > 8:
        scoreboard.winner()
        game_is_on = False

screen.exitonclick()