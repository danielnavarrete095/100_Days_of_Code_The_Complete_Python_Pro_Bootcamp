from socket import gethostbyname_ex
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2 - 5
MAX_Y = SCREEN_HEIGHT / 2 - 5
BALL_SPEED_INIT = 5
BALL_SPEED_INC = 0.1
screen = None
paddle_right = None
paddle_left = None
ball = None
scoreboard = None

def set_key_bindings():
    global screen, paddle_right, paddle_left
    screen.listen()
    screen.onkeypress(key="Up", fun=paddle_right.set_moving_up)
    screen.onkeypress(key="Down", fun=paddle_right.set_moving_down)
    screen.onkeypress(key="w", fun=paddle_left.set_moving_up)
    screen.onkeypress(key="s", fun=paddle_left.set_moving_down)
    screen.onkeyrelease(key="Up", fun=paddle_right.reset_moving)
    screen.onkeyrelease(key="Down", fun=paddle_right.reset_moving)
    screen.onkeyrelease(key="w", fun=paddle_left.reset_moving)
    screen.onkeyrelease(key="s", fun=paddle_left.reset_moving)

def detect_wall_collision(ball, y_border):
    y_ball = ball.pos()[1]
    if y_ball > y_border - 15 or\
       y_ball < - y_border + 15:
        ball.dir_changed = False
        return True
    return False

def detect_paddle_collision(ball):
    x_ball = ball.pos()[0]
    y_ball = ball.pos()[1]
    x_paddle_r = paddle_right.pos()[0]
    x_paddle_l = paddle_left.pos()[0]

#Detect collision witth right paddle
    if x_ball >= x_paddle_r - 20 and \
        ball.distance(paddle_right) <= 50:
            print("Right paddle collision")
            return True
#Detect collision witth left paddle
    if x_ball <= x_paddle_l + 20 and \
        ball.distance(paddle_left) <= 50:
        return True
    return False

def detect_out_of_bounds(ball):
    x_ball = ball.pos()[0]
    if x_ball > 0 and x_ball >= MAX_X - 20:
        return True
    if x_ball < 0 and x_ball <= -MAX_X + 10:
        return True
    return False

def reset_game():
    global screen, paddle_right, paddle_left, ball
    paddle_right.home()
    paddle_left.home()
    ball.home()
    ball.moving_speed = BALL_SPEED_INIT

def main():
    global screen, paddle_right, paddle_left, ball, scoreboard
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong game 🎾🕹")
    screen.bgcolor("black")
    screen.tracer(0)
    
    scoreboard = Scoreboard(MAX_X, MAX_Y)
    
    paddle_right = Paddle(370, 0, MAX_Y)
    paddle_left = Paddle(-380, 0, MAX_Y)
    ball = Ball(0, 0, BALL_SPEED_INIT)
    set_key_bindings()

    game_is_on = True
    while(game_is_on):
        screen.update()
        if not ball.dir_changed:
            if detect_wall_collision(ball, MAX_Y):
                ball.bounce_y()
                ball.dir_changed = False
            if detect_paddle_collision(ball):
                ball.bounce_x()
                ball.dir_changed = False
                ball.moving_speed += BALL_SPEED_INC
                print(f"New ball speed: {ball.moving_speed}")
        
        #detect out of bounds
        if detect_out_of_bounds(ball):
            # game_is_on = False
            if ball.pos()[0] > 0:
                scoreboard.update(l_score=True)
            else:
                scoreboard.update(r_score=True)
            reset_game()
            ball.angle += 180
            time.sleep(0.5)
        
        ball.move()
        paddles = (paddle_left, paddle_right)
        for paddle in paddles:
            if paddle.moving == "up":
                paddle.move_up()
            elif paddle.moving == "down":
                paddle.move_down()
        time.sleep(0.005)

    screen.exitonclick()

if __name__ == '__main__':
    main()