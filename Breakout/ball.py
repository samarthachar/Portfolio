from turtle import Turtle

class Ball(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_distance = 12.5
        self.x_move = self.move_distance
        self.y_move = self.move_distance

        self.goto(xcor, ycor)
    def move(self):
        new_x =  self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1