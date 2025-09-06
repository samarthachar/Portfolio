from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 220)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))


    def point(self):
        self.score += 50

    def game_over(self):
        self.goto(0,0)
        self.write(arg = "GAME OVER", align="center", font=("Courier", 80, "normal"))
