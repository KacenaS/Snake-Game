from turtle import Turtle
import os

ALIGMNET = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 290)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", move=False, align=ALIGMNET, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
            

        self.score = 0
        self.update_scoreboard()

    def increase_points(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


