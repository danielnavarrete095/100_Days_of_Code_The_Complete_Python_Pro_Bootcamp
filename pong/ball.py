from turtle import Turtle
WIDTH = 20
HEIGHT = 20
WIDTH_FACTOR = WIDTH / 20
HEIGHT_FACTOR = HEIGHT / 20
class Ball(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("circle")
        self.setpos(pos_x, pos_y)
        self.shapesize(HEIGHT_FACTOR, WIDTH_FACTOR, 0)
        self.angle = 85
        self.dir_changed = False

    def move(self):
        self.setheading(self.angle)
        self.fd(15)
        
    def bounce(self):
            self.angle = 360 - self.angle
            self.dir_changed = True