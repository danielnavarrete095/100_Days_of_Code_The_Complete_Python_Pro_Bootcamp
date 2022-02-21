from turtle import Turtle, Screen, clear as turtle_clear

my_turtle = Turtle()
screen = Screen()

def move_forwards():
    my_turtle.fd(10)
def move_backwards():
    my_turtle.bk(10)
def turn_cw():
    my_turtle.right(10)
def turn_ccw():
    my_turtle.left(10)
def clear_screen():
    my_turtle.clear()
    my_turtle.pu()
    my_turtle.home()
    my_turtle.pd()

def set_key_bindings():
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="Up", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="Down", fun=move_backwards)
    screen.onkey(key="a", fun=turn_ccw)
    screen.onkey(key="Left", fun=turn_ccw)
    screen.onkey(key="d", fun=turn_cw)
    screen.onkey(key="Right", fun=turn_cw)
    screen.onkey(key="c", fun=clear_screen)
    
def main():
    set_key_bindings()
    screen.exitonclick()


if __name__ == '__main__':
    main()