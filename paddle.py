from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x, position_y, colour):
        super().__init__()
        self.goto(x=position_x, y=position_y)
        self.shape("square")
        self.color(colour)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + 20
        self.goto(x_cor, y_cor)

    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 20
        self.goto(x_cor, y_cor)
