from socket import gethostbyname_ex
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2 - 5
MAX_Y = SCREEN_HEIGHT / 2 - 5
screen = None
paddle_right = None
paddle_left = None

def set_key_bindings():
    global screen, paddle_right, paddle_left
    screen.listen()
    screen.onkey(key="Up", fun=paddle_right.move_up)
    screen.onkey(key="Down", fun=paddle_right.move_down)
    screen.onkey(key="w", fun=paddle_left.move_up)
    screen.onkey(key="s", fun=paddle_left.move_down)

def main():
    global screen, paddle_right, paddle_left
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong game 🎾🕹")
    screen.bgcolor("black")
    screen.tracer(0)
    
    paddle_right = Paddle(360, 0)
    paddle_left = Paddle(-380, 0)
    
    ball = Ball(0, 0)
    set_key_bindings()

    game_is_on = True
    while(game_is_on):
        screen.update()
        if not ball.dir_changed:
            if detect_wall_collision(ball, MAX_Y):
                ball.bounce()
                ball.dir_changed = False
        if detect_paddle_collision(ball, paddle_right):
            print("Right paddle collision")
            break
        if detect_paddle_collision(ball, paddle_left):
            print("Left paddle collision")
            break
        ball.move()
        time.sleep(0.1)

    screen.exitonclick()

def detect_wall_collision(ball, y_border):
    y_ball = ball.pos()[1]
    if y_ball > y_border - 15 or\
       y_ball < - y_border + 15:
        ball.dir_changed = False
        return True
    return False

def detect_paddle_collision(ball, paddle):
    x_ball = abs(ball.pos()[0])
    y_ball = abs(ball.pos()[1])
    x_paddle = abs(paddle.pos()[0])
    y_paddle = abs(paddle.pos()[1])
    if x_ball >= x_paddle and \
        (y_ball <= y_paddle + 50 or y_ball >= - y_paddle + 50):
        ball.dir_changed = False
        return True
    return False

if __name__ == '__main__':
    main()