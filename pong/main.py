from turtle import Screen
from paddle import Paddle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def set_key_bindings():
    screen.listen()
    screen.onkey(key="Right", fun=move_right)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)

def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong game 🎾🕹")
    screen.bgcolor("black")
    
    paddle_right = Paddle(360, 0)
    paddle_left = Paddle(-380, 0)


    screen.exitonclick()

if __name__ == '__main__':
    main()