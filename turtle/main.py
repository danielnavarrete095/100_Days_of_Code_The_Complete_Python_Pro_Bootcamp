from turtle import Turtle, Screen, colormode
from colors import colors_list
import random
def draw_square(turtle, length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_dashed_line(turtle, length):
    dash_size = 10
    distance = 0
    pen_down = True
    while(distance < length):
        turtle.fd(dash_size)
        if pen_down:
            turtle.pu()
            pen_down = False
        else:
            turtle.pd()
            pen_down = True
        distance += dash_size

def draw_polygon(turtle, sides, length):
    color = random.choice(colors_list)
    turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        turtle.fd(length)
        turtle.right(angle)
        
def random_walk(turtle, distance, times):
    for _ in range(times):
        color = get_random_color()
        # color = random.choice(colors_list)
        turtle.color(color)
        angle_list = (90, 180, 270, 360)
        angle = random.choice(angle_list)
        turtle.right(angle)
        turtle.fd(distance)
        
def spirograph(turtle, radius, num_of_circles):
    angle = 360 / num_of_circles
    for _ in range(num_of_circles):
        color = get_random_color()
        turtle.color(color)
        turtle.circle(radius)
        # turtle.right(angle)
        turtle.setheading(turtle.heading() + angle)

def get_random_color():
    r = round(random.random() * 255)
    g = round(random.random() * 255)
    b = round(random.random() * 255)
    return (r, g, b)

def main():
    screen = Screen()
    colormode(255)
    screen.bgcolor((211, 211, 211))
    my_turtle = Turtle()
    my_turtle.shape("circle")
    my_turtle.resizemode("user")
    my_turtle.shapesize(0.2, 0.2, 0)
    # my_turtle.shapesize(0.5, 0.5, 0)
    my_turtle.pensize(2)
    # draw_square(my_turtle, 100)
    # draw_dashed_line(my_turtle, 300)
    # my_turtle.pu()
    # my_turtle.goto(-50,400)
    # my_turtle.pd()
    # for i in range(3, 25):
    #     draw_polygon(my_turtle, i, 100)
    my_turtle.speed('fastest')
    # random_walk(my_turtle, 20, 1000)

    spirograph(my_turtle, 100, 80)
    
    screen.exitonclick()
if __name__ == '__main__':
    main()