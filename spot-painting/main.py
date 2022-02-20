import colorgram
import os
import random
from turtle import Turtle, Screen, colormode as turtle_set_colormode

def get_color_list(image, num_of_colors):
    colors = colorgram.extract(image, num_of_colors)
    color_list = []
    for color in colors:
        rgb = color.rgb
        color_list.append((rgb.r, rgb.g, rgb.b))
    #remove whites/grays
    colors_to_remove = []
    for color in color_list:
        if color[0] > 200 and color[1] > 200 and color[2] > 200:
            colors_to_remove.append(color)
    for color in colors_to_remove:
        color_list.remove(color)
    return color_list
    
def get_random_color():
    r = round(random.random() * 255)
    g = round(random.random() * 255)
    b = round(random.random() * 255)
    return (r, g, b)

def create_dot_painting(turtle, width, height, color_list = None):
    x_init = 50 * (width - 1) / 2
    y_init = 50 * (height - 1) / 2
    turtle.goto(-x_init, -y_init)

    for _ in range(height):
        for _ in range(width):
            color = get_random_color() if color_list == None else random.choice(color_list)
            turtle.dot(20, color)
            turtle.fd(50)
        turtle.setx(-x_init)
        turtle.sety(turtle.ycor() + 50)

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    # my_image = os.path.join(THIS_FOLDER, "image.jpg")
    my_image = os.path.join(THIS_FOLDER, "picasso.jpg")
    print(my_image)
    color_list = get_color_list(my_image, 30)
    
    screen = Screen()
    turtle_set_colormode(255)
    screen.bgcolor((211, 211, 211))

    my_turtle = Turtle()
    my_turtle.shape("arrow")
    my_turtle.resizemode("user")
    my_turtle.shapesize(0.5, 0.5, 0)
    my_turtle.speed('fastest')
    my_turtle.pu()
    # create_dot_painting(my_turtle, 10, 10)
    create_dot_painting(my_turtle, 10, 10, color_list)
    my_turtle.hideturtle()

    screen.exitonclick()



if __name__ == '__main__':
    main()