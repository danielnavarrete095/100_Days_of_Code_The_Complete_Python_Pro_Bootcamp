from textwrap import fill
from turtle import Turtle, Screen, colormode as turtle_set_colormode
import random

NUM_OF_TURTLES = 10

def fill_turtle_list(list):
    for i in range(NUM_OF_TURTLES):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.resizemode("user")
        turtle.speed("fastest")
        turtle.color(get_random_color())
        turtle.pu()
        x_coord = -screen.screensize()[0] - 50
        y_coord = NUM_OF_TURTLES * 50 / 2 - i * 50
        turtle.setposition(x_coord, y_coord)
        list.append(turtle)

def advance_turtles_list(list):
    winner = None
    while not winner:
        for turtle in list:
            if not advance_turtle(turtle):
                winner = turtle
                print(winner.color())



def advance_turtle(turtle):
    if turtle.pos()[0] < screen.screensize()[0] + 50:
        distance = random.randint(5, 10)
        turtle.fd(distance)
        return True
    return False

def get_random_color():
    r = round(random.random() * 255)
    g = round(random.random() * 255)
    b = round(random.random() * 255)
    return (r, g, b)

screen = Screen()
def main():

    turtle_set_colormode(255)
    screen.bgcolor((211, 211, 211))

    turtle_list = []
    fill_turtle_list(turtle_list)
    advance_turtles_list(turtle_list)

    screen.exitonclick()

    
if __name__ == '__main__':
    main()