from turtle import Turtle
WIDTH = 20
HEIGHT = 20
WIDTH_FACTOR = WIDTH / 20
HEIGHT_FACTOR = HEIGHT / 20
class Ball(Turtle):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("circle")
        self.x_start = pos_x
        self.y_start = pos_y
        self.home()
        self.shapesize(HEIGHT_FACTOR, WIDTH_FACTOR, 0)
        self.angle = -45
        self.dir_changed = False
        self.moving_speed = speed

    def home(self):
        super().home()
        self.setpos(self.x_start, self.y_start)

    def move(self):
        self.setheading(self.angle)
        self.fd(self.moving_speed)
        
    def bounce_y(self):
        self.angle = 360 - self.angle
        self.dir_changed = True
    def bounce_x(self):
        if self.angle <= 180:
            self.angle = 180 - self.angle
        else:
            self.angle = (360 - self.angle) + 180
        self.dir_changed = True
            