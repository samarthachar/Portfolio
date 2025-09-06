from turtle import Screen
from paddle import Paddle
from ball import Ball
from game_block import Block
from scoreboard import Scoreboard
import time

def create_rows():
    y = 200
    blocks = []
    colors = ['blue', 'red', 'yellow', 'green']
    colour_count = 0
    for _ in range(4):
        for x in [-194, -139, -83, -28, 28, 83, 139, 194]:
            position = (x,y)
            block = Block(position, colors[colour_count])
            blocks.append(block)
        y -= 30
        colour_count += 1


    return blocks

def up_clicked():
    global game_is_on
    game_is_on = True

screen = Screen()
screen.setup(width= 500, height=500)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0,-200))

ball = Ball(0,-175)

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(up_clicked, "Up")
game_is_on = False

blocks = create_rows()
while not game_is_on:
    screen.update()

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_x()
    if ball.ycor() > 230:
        ball.bounce_y()
    if ball.distance(paddle) < 50 and ball.ycor() < -180:
        ball.bounce_y()

    if ball.ycor() < -250:
        scoreboard.game_over()
        game_is_on = False

    if not blocks:
        time.sleep(5)
        blocks = create_rows()
    for block in blocks[:]:
        if block.distance(ball) < 15:
            scoreboard.point()
            ball.bounce_y()
            block.break_block()
            blocks.remove(block)
            scoreboard.update_scoreboard()

screen.exitonclick()