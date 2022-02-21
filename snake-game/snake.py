from turtle import Turtle

class Snake:

    directions = {"right" : 0, "up" : 90, "left" : 180, "down" : 270}

    def __init__(self, size, screen):
        self.body = []
        self.size = size
        self.direction = "right"
        self.SQUARE_SIZE = 20

    def createBody(self, screen):
        for i in range(self.size):
            # create new square
            square = Turtle()
            square.pu()
            square.shape("square")
            square.color("white")
            square.setx(- i * self.SQUARE_SIZE)
            self.body.append(square)
        screen.update()
        
    def move(self, screen):
        direction = self.direction
        prev_direction = ""
        prev_x = 0
        prev_y = 0
        for i, square in enumerate(self.body):
            square_direction = self.get_square_direction(square)
            # head should follow global direction
            if i == 0:
                if direction != square_direction:
                    self.set_square_direction(square, direction)
                square.fd(self.SQUARE_SIZE)
            # body should follow previous square direction
            else:
                # fd()
                # if not in the right direction
                # if coordinate is right, turn dir
                square.fd(self.SQUARE_SIZE)
                prev_square = self.body[i - 1]
                prev_direction = self.get_square_direction(prev_square)
                if square_direction != prev_direction:
                    prev_x = round(prev_square.pos()[0])
                    prev_y = round(prev_square.pos()[1])
                    cur_x = round(square.pos()[0])
                    cur_y = round(square.pos()[1])
                    # if dir is up or down check x coord
                    if prev_direction == "up" or prev_direction == "down":
                        # if coord == prev_coord, change dir
                        if prev_x == cur_x:
                            self.set_square_direction(square, prev_direction)
                        # else:
                        #     print(f"{i} x: {cur_x}, {i - 1} x: {prev_x}")
                    # if dir is left or right check y coord
                    elif prev_direction == "right" or prev_direction == "left":
                        # if coord == prev_coord, change dir
                        if prev_y == cur_y:
                            self.set_square_direction(square, prev_direction)
                        # else:
                        #     print(f"{i} y: {cur_y}, {i - 1} y: {prev_y}")
        screen.update()
        
    def set_direction(self, dir):
        direction = self.direction
        # If direction is right or left can only change to up/down
        if(direction == "right" or direction == "left") and (dir == "up" or dir == "down"):
            self.direction = dir
        # If direction is up or down can only change to right/left
        elif(direction == "up" or direction == "down") and (dir == "right" or dir == "left"):
            self.direction = dir
            
    def get_square_direction(self, square):
        square_direction = square.heading()
        for dir in self.directions:
            if self.directions[dir] == square_direction:
                return dir
                
    def set_square_direction(self, square, direction):
        square.setheading(self.directions[direction])
            

