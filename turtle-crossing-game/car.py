from turtle import Turtle

CAR_SIZE = (50 / 20, 20 / 20)

class Car(Turtle):
    def __init__(self, pos_x, pos_y, color, speed):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color(color)
        self.setpos(pos_x, pos_y)
        self.shapesize(CAR_SIZE[1], CAR_SIZE[0], 0)
        self.setheading(180)
        self.moving = None
        self.car_speed = speed

    def move(self):
            x = self.pos()[0]
            self.setx(x - self.car_speed)

    def set_moving(self):
        self.moving = True

    def reset_moving(self):
        self.moving = False
