from turtle import Turtle

ALIGNMENT = "center"
FONT = "Calibri", 80, "normal"
class Scoreboard(Turtle):
    def __init__(self, bound_x, bound_y):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.pu()
        self.color("white")
        self.bound_x = bound_x
        self.bound_y = bound_y
        self.print_scores()

    def update(self, r_score = False, l_score = False):
        self.clear()
        self.r_score += 1 if r_score else 0
        self.l_score += 1 if l_score else 0
        self.print_scores()

    def print_scores(self):
        self.setpos(-self.bound_x / 5, self.bound_y - 100)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.setpos(self.bound_x / 5, self.bound_y - 100)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)