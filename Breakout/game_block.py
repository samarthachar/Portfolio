from turtle import Turtle

class Block(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.goto(position)
        self.shape('square')
        self.color(f'{color}')
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=2)
    def break_block(self):
        self.hideturtle()
        self.clear()