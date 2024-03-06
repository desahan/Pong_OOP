from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def winner(self):
        self.goto(-260, 0)
        if self.l_score == 9:
            self.write("Winner with 9 points: Left paddle!", font=("Courier", 20, "normal"))
        else:
            self.write("Winner with 9 points: RightLeft paddle!", font=("Courier", 20, "normal"))
