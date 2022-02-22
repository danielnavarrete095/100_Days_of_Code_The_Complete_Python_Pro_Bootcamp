from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.color("black")
        self.home()
        self.moving = False
        self.released = False

    def home(self):
        super().home()
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move(self):
            y = self.pos()[1]
            self.sety(y + 5)

    def set_moving(self):
        self.moving = True

    def reset_moving(self):
        self.moving = False