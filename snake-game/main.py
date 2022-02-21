from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
my_snake = None

def move_right():
    global my_snake
    my_snake.set_direction("right")
def move_left():
    global my_snake
    my_snake.set_direction("left")
def move_up():
    global my_snake
    my_snake.set_direction("up")
def move_down():
    global my_snake
    my_snake.set_direction("down")

def main():
    global my_snake
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game 🐍")
    screen.tracer(0)

    screen.listen()
    screen.onkey(key="Right", fun=move_right)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    
    my_snake = Snake(3, screen)
    my_snake.createBody(screen)

    game_is_on = True
    while(game_is_on):
        my_snake.move(screen)
        time.sleep(0.1)

    screen.exitonclick()
if __name__ == '__main__':
    main()