import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2 - 5
MAX_Y = SCREEN_HEIGHT / 2 - 5
screen = None
player = None
carmanager = None
scoreboard = None

def detect_collision():
    global player, carmanager
    for car in carmanager.cars:
        if car.distance(player) < 30:
            return True
    return False

def level_passed():
    if player.pos()[1] + 10 >= MAX_Y:
        return True
    return False

def reset_game():
    global player
    player.home()

def main():
    global screen, player, carmanager
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    
    screen.tracer(0)
    screen.bgcolor("gray")

    player = Player()
    screen.listen()
    screen.onkeypress(key="Up", fun=player.set_moving)
    screen.onkeyrelease(key="Up", fun=player.reset_moving)

    carmanager = CarManager()
    scoreboard = Scoreboard(MAX_X, MAX_Y)
    
    game_is_on = True
    while game_is_on:
        if player.moving == True and player.released:
            player.move()
        if carmanager.can_create_car():
            carmanager.create_car()
        carmanager.move_cars()
        if not player.released:
            if carmanager.cars[0].pos()[0] < player.pos()[0]:
                print("Player released!")
                player.released = True
        if detect_collision():
            game_is_on = False
        if level_passed():
            scoreboard.level += 1
            carmanager.car_speed += 1
            print(f"New car speed: {carmanager.car_speed}")
            scoreboard.update()
            reset_game()
        time.sleep(0.001)
        screen.update()
    scoreboard.write_centered("GAME OVER", 0, "black")
    screen.exitonclick()

if __name__ == '__main__':
    main()
