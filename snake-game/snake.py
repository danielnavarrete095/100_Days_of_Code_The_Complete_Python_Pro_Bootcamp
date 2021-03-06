from turtle import Turtle

class Snake:

    directions = {"right" : 0, "up" : 90, "left" : 180, "down" : 270}

    def __init__(self, size, shape):
        self.body = []
        self.size = size
        self.shape = shape
        self.direction = "right"
        self.dir_queue = None
        self.SEGMENT_SIZE = 20
        self.head = None
        self.head = None

    def create_body(self):
        for i in range(self.size):
            # create new segment
            pos_x = - i * self.SEGMENT_SIZE
            pos_y = 0
            segment = self.create_segment(pos_x, pos_y)
            self.body.append(segment)
        self.head = self.body[0]
        self.tail = self.body[len(self.body) - 1]

    def create_segment(self, x = None, y = None):
        segment = Turtle()
        segment.pu()
        segment.shape(self.shape)
        segment.color("white")
        if x:
            segment.setx(x)
        if y:
            segment.setx(y)
        return segment

    def move(self):
        direction = self.direction
        prev_x = 0
        prev_y = 0
        for segment in self.body:
            segment_direction = self.get_segment_direction(segment)
            new_x = prev_x
            new_y = prev_y
            prev_x = segment.pos()[0]
            prev_y = segment.pos()[1]
            # head should follow global direction
            if segment == self.head:
                if direction != segment_direction:
                    self.set_segment_direction(segment, direction)
                segment.fd(self.SEGMENT_SIZE)
                self.dir_attended = True
            # body should occupy previous segment position
            else:
                segment.setpos(new_x, new_y)

    def can_turn(self, new_dir):
        direction = self.direction
        # If direction is right or left can only change to up/down
        # If direction is up or down can only change to right/left
        if((direction == "right" or direction == "left") and\
          (new_dir == "up" or new_dir == "down")) or\
          ((direction == "up" or direction == "down") and\
          (new_dir == "right" or new_dir == "left")):
            return True
        return False

    def set_direction(self, dir):
        # If direction was already attended
        if self.dir_attended:
            # If there's no dir in queue, change direction
            if self.dir_queue == None:
                if self.can_turn(dir):
                    self.direction = dir
                    self.dir_attended = False
            # else, there is something in queue, make direction = queue and clear queue
            else:
                self.direction = self.dir_queue
                self.dir_attended = False
                self.dir_queue = None
        # else, save direction in queue
        else:
            if self.can_turn(dir):
                self.dir_queue = dir

    def grow(self):
        # create new segment
        new_segment = self.create_segment()
        self.body.append(new_segment)
        self.tail = new_segment

    def get_segment_direction(self, segment):
        segment_direction = segment.heading()
        for dir in self.directions:
            if self.directions[dir] == segment_direction:
                return dir

    def set_segment_direction(self, segment, direction):
        segment.setheading(self.directions[direction])

    def tail_collision(self):
        tail = self.body[2:]
        for segment in tail:
            if self.head.distance(segment) < 5:
                return True
        return False

    def reset(self, size):
        for segment in self.body:
            segment.setpos(1000, 1000)
        self.body.clear()
        self.size = size
        self.direction = "right"
        self.dir_queue = None
        self.SEGMENT_SIZE = 20
        self.head = None
        self.head = None
        self.create_body()