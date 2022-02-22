from turtle import Turtle
WIDTH = 20
HEIGHT = 100
WIDTH_FACTOR = WIDTH / 20
HEIGHT_FACTOR = HEIGHT / 20
class Paddle(Turtle):

    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.setpos(pos_x, pos_y)
        self.shapesize(HEIGHT_FACTOR, WIDTH_FACTOR, 0)

    def move_up(self):
        y = self.pos()[1]
        self.sety(y + 20)

    def move_down(self):
        y = self.pos()[1]
        self.sety(y - 20)
