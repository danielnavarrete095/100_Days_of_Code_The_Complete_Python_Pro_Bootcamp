from turtle import Turtle
class Food(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pu()
        self.setpos(pos_x, pos_y)
        self.color("red")
        self.shape("turtle")
        self.shapesize(0.5, 0.5, 0)