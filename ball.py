from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.width(20)
        self.x_move = 10
        self.y_move = 10



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def left_miss(self):
        self.goto(0, 0)
        time.sleep(.5)
        self.paddle_bounce()

    def right_miss(self):
        self.goto(0, 0)
        time.sleep(.5)
        self.paddle_bounce()
