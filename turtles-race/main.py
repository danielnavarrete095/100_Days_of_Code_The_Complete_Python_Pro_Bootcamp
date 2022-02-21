from textwrap import fill
from turtle import Turtle, Screen, colormode as turtle_set_colormode
import random

NUM_OF_TURTLES = 8
drawing_turtle = Turtle()
drawing_turtle.hideturtle()
drawing_turtle.speed("fastest")
turtle_colors = [
    "blue",
    "deep sky blue",
    "cyan",
    "pale green",
    "spring green",
    "lime",
    "orange red",
    "salmon",
    "blue violet",
    "lavender"
]

def fill_turtle_list():
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
        turtle_list.append(turtle)

def advance_turtles_list():
    winner = None
    while not winner:
        for turtle in turtle_list:
            if not advance_turtle(turtle):
                winner = turtle
                print(winner.color())

def draw_track(num_of_participants):
    color = "burlywood"
    x_coord = -screen.screensize()[0] - 50
    for i in range(num_of_participants):
        color = "navajo white" if color == "burlywood" else "burlywood"
        y_coord = NUM_OF_TURTLES * 50 / 2 - i * 50 - 25
        draw_rectangle((x_coord, y_coord), screen.screensize()[0]*2, 50, color)
    color = "burlywood"
    x_coord += screen.screensize()[0]*2
    draw_rectangle((x_coord, y_coord), 50, 50 * num_of_participants, "light sea green")

# ->,^,<-,v 
def draw_rectangle(initial_xy, width, height, color):
    drawing_turtle.pu()
    drawing_turtle.fillcolor(color)
    drawing_turtle.setposition(initial_xy[0], initial_xy[1])
    drawing_turtle.begin_fill()
    drawing_turtle.setx(drawing_turtle.pos()[0] + width)
    drawing_turtle.sety(drawing_turtle.pos()[1] + height)
    drawing_turtle.setx(drawing_turtle.pos()[0] - width)
    drawing_turtle.sety(drawing_turtle.pos()[1] - height)
    drawing_turtle.end_fill()

def advance_turtle(turtle):
    if turtle.pos()[0] < screen.screensize()[0] + 50:
        distance = random.randint(1, 10)
        turtle.fd(distance)
        return True
    return False

def get_random_color():
    # r = round(random.random() * 255)
    # g = round(random.random() * 255)
    # b = round(random.random() * 255)
    # return (r, g, b)
    color = random.choice(turtle_colors)
    turtle_colors.remove(color) 
    return color

screen = Screen()
turtle_list = []
def main():
    # screen.setup(width = 500, height = NUM_OF_TURTLES * 50)
    response = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a number from 1-{NUM_OF_TURTLES}")
    turtle_set_colormode(255)
    screen.bgcolor((211, 211, 211))

    # my_turtle = Turtle()
    # my_turtle.write("1aadsfdgsgewg34670")
    # draw_rectangle((0,0), 100, 100, "white")
    draw_track(NUM_OF_TURTLES)
    fill_turtle_list()
    # screen.onkey(key="space", fun=advance_turtles_list)
    advance_turtles_list()

    screen.exitonclick()

if __name__ == '__main__':
    main()