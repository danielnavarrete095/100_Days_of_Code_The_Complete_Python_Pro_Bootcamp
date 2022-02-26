import random
from car import Car
from collections import deque
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2 - 25
LANE_SIZE = 30
CAR_SIZE = (50, 20)
NUMBER_OF_LANES = SCREEN_HEIGHT / LANE_SIZE - 3
STARTING_Y = -280

class CarManager:
    def __init__(self) -> None:
        self.cars = deque()
        # self.cars = []
        self.last_lane = None
        self.car_speed = 5
    
    def create_car(self):
        random_lane = random.randint(1, NUMBER_OF_LANES)
        if random_lane != self.last_lane:
            self.last_lane = random_lane
        else:
            random_lane = random.randint(1, NUMBER_OF_LANES)

        init_x = MAX_X + CAR_SIZE[0]
        init_y = STARTING_Y + random_lane * LANE_SIZE
        color = random.choice(COLORS)
        car = Car(init_x, init_y, color, self.car_speed)
        self.cars.append(car)

        
    def can_create_car(self):
        init_x = MAX_X + CAR_SIZE[0]
        if len(self.cars) > 0:
            # create car randomnly
            chances = 3
            random_chance = random.randint(1, chances)
            if random_chance == 1:
                # create car if latest already advanced enough
                if self.cars[-1].pos()[0] < init_x - 50:
                    return True
        else:
            return True
        return False
    
    def move_cars(self):
        if self.out_of_bounds(self.cars[0]):
            # print(len(self.cars))
            self.cars.popleft()
        for car in self.cars:
            # if self.out_of_bounds(car):
            #     self.cars.remove(car) 
            # else:
                car.move()
    
    def out_of_bounds(self, car):
        car_x = car.pos()[0]
        if car_x <= - MAX_X - 50:
            return True
        return False
