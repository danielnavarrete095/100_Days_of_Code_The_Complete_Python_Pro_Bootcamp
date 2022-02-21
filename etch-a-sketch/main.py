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
    screen.onkeypress(key="w", fun=move_forwards)
    screen.onkeypress(key="Up", fun=move_forwards)
    screen.onkeypress(key="s", fun=move_backwards)
    screen.onkeypress(key="Down", fun=move_backwards)
    screen.onkeypress(key="a", fun=turn_ccw)
    screen.onkeypress(key="Left", fun=turn_ccw)
    screen.onkeypress(key="d", fun=turn_cw)
    screen.onkeypress(key="Right", fun=turn_cw)
    screen.onkeypress(key="c", fun=clear_screen)
    
def main():
    set_key_bindings()
    screen.exitonclick()


if __name__ == '__main__':
    main()