from turtle import Turtle
import json
HIGH_SCORE_F = "high_score.json"
ALIGNMENT = "center"
FONT = "Calibri", 15, "bold"
class Scoreboard(Turtle):
    def __init__(self, y):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.text = f"Score: {self.score}  High Score: {self.high_score}"
        self.hideturtle()
        self.pu()
        self.y_init = y - 30
        self.sety(self.y_init)
        self.color("white")
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.text = f"Score: {self.score}  High Score: {self.high_score}"
        self.write(self.text, align=ALIGNMENT, font=FONT)
    
    def write_centered(self, text, y):
        self.home()
        self.write(text, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        self.sety(self.y_init)
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
    
    def save_high_score(self):
        highscore = {"highscore": self.high_score}
        json_string = json.dumps(highscore)
        print(json_string)
        with open(HIGH_SCORE_F, "w") as file:
            file.write(json_string)
    
    def read_high_score(self):
        with open(HIGH_SCORE_F, "r") as file:
            highscore = json.load(file)
        return highscore["highscore"]