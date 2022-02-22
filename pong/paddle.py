from turtle import Turtle

WIDTH = 20
HEIGHT = 100
WIDTH_FACTOR = WIDTH / 20
HEIGHT_FACTOR = HEIGHT / 20

class Paddle(Turtle):

    def __init__(self, pos_x, pos_y, bound_y) -> None:
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.x_start = pos_x
        self.y_start = pos_y
        self.home()
        self.shapesize(HEIGHT_FACTOR, WIDTH_FACTOR, 0)
        self.bound_y = bound_y
        self.moving = None

    def home(self):
        super().home()
        self.setpos(self.x_start, self.y_start)

    def move_up(self):
        if self.pos()[1] < self.bound_y - HEIGHT / 2 - 10:
            y = self.pos()[1]
            self.sety(y + 10)

    def move_down(self):
        if self.pos()[1] > - self.bound_y + HEIGHT / 2 + 10:
            y = self.pos()[1]
            self.sety(y - 10)

    def set_moving_up(self):
        self.moving = "up"
    def set_moving_down(self):
        self.moving = "down"
    def reset_moving(self):
        self.moving = "None"