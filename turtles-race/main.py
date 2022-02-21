from textwrap import fill
from turtle import Turtle, Screen, colormode as turtle_set_colormode
import random

NUM_OF_TURTLES = 5
drawing_turtle = Turtle()
drawing_turtle.hideturtle()
drawing_turtle.speed("fastest")
screen = Screen()
turtle_list = []
turtle_colors = [
    "blue",
    "yellow",
    "red",
    "orange",
    "purple",
    "green",
    "black",
    "brown",
    "pink",
    "gray"
]

def fill_turtle_list():
    used_colors = []
    for i in range(NUM_OF_TURTLES):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.resizemode("user")
        turtle.speed("fastest")
        
        new_color = get_random_color()
        while new_color in used_colors:
            new_color = get_random_color()
        used_colors.append(new_color)
        turtle.color(new_color)

        turtle.pu()
        x_coord = -screen.screensize()[0] / 2 + 25
        y_coord = NUM_OF_TURTLES * 50 / 2 - i * 50 - 25
        turtle.setposition(x_coord, y_coord)
        turtle_list.append(turtle)

def advance_turtles_list():
    winner = None
    while not winner:
        for turtle in turtle_list:
            if not advance_turtle(turtle):
                winner = turtle
    return winner

def draw_track(num_of_participants):
    color = "burlywood"
    x_coord = -screen.screensize()[0] / 2
    for i in range(num_of_participants):
        color = "navajo white" if color == "burlywood" else "burlywood"
        y_coord = NUM_OF_TURTLES * 50 / 2 - i * 50 - 50
        draw_rectangle((x_coord, y_coord), screen.screensize()[0], 50, color)

        drawing_turtle.goto((x_coord + 10, y_coord + 17))
        drawing_turtle.write(str(i + 1))
        
    color = "burlywood"
    x_coord += screen.screensize()[0] - 50
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
    if turtle.pos()[0] < screen.screensize()[0] / 2 - 50:
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
    return color

def main():
    while(True):
        turtle_set_colormode(255)
        screen.bgcolor((211, 211, 211))
        screen.setup(width = 910, height = 510)
        screen.title("Turtle Race 🏁")
        canvas_width = 900
        canvas_height = NUM_OF_TURTLES * 50
        screen.screensize(canvas_width, canvas_height)



        draw_track(NUM_OF_TURTLES)
        fill_turtle_list()
        response = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a number from 1-{NUM_OF_TURTLES}")
        winner_index = advance_turtles_list()
        winner_turtle = turtle_list.index(winner_index) + 1

        if int(response) == winner_turtle:
            title = "You won! congratulations."
        else:
            title = "Sorry, you lost."
        message = f"The winner is #{winner_turtle}."
        message += "\nType 'yes' to play again or 'no' to exit"
        response = screen.textinput(title=title, prompt=message)
        if response.lower() == "yes" or response.lower() == "y":
            screen.clearscreen()
            turtle_list.clear()
        else:
            screen.bye()
            break
    # screen.exitonclick()

if __name__ == '__main__':
    main()