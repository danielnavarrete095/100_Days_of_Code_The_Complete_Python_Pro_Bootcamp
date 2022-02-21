from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from random import randint, choice as ranchoice

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2 - 5
MAX_Y = SCREEN_HEIGHT / 2 - 5
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
def get_food_random_place():
    # create food in random place
    max_x = MAX_X - 10
    max_y = MAX_Y -10
    # position should be a multiple of 20
    max_x_multiple = round(max_x / 20)
    max_y_multiple = round(max_y / 20)
    sign = ranchoice((-1,1))
    pos_x = randint(1, max_x_multiple) * 20 * sign
    pos_y = randint(1, max_y_multiple) * 20 * sign
    print(f"Food at: {pos_x}, {pos_y}")
    return (pos_x, pos_y)
    
def main():
    global my_snake
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    # print(screen.screensize())
    screen.bgcolor("black")
    screen.title("Snake Game 🐍")
    screen.tracer(0)

    screen.listen()
    screen.onkey(key="Right", fun=move_right)
    screen.onkey(key="Left", fun=move_left)
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    
    #create snake
    my_snake = Snake(3, shape="circle")
    my_snake.create_body()

    food_pos = get_food_random_place()
    food = Food(food_pos[0], food_pos[1])

    # start game
    game_is_on = True
    while(game_is_on):
        my_snake.move()
        time.sleep(0.1)
        screen.update()

        # Detect collision with food
        distance_to_food = my_snake.head.distance(food)
        if distance_to_food < 15:
            print("food coillision!")
            # Eat food
            food_pos = get_food_random_place()
            food.setpos(food_pos[0], food_pos[1])
            # Grow snake
            my_snake.grow()
        # Detect collision borders
        distance_to_border_x = MAX_X - my_snake.head.pos()[0]
        distance_to_border_y = MAX_Y - my_snake.head.pos()[1]
        if distance_to_border_x < 5 or distance_to_border_y < 5:
            print("border coillision!")
            drawing_turtle = Turtle()
            drawing_turtle.hideturtle()
            drawing_turtle.speed("fastest")
            drawing_turtle.pu()
            drawing_turtle.home()
            drawing_turtle.color("white")
            drawing_turtle.write("Game over!")
            break
    screen.exitonclick()
if __name__ == '__main__':
    main()