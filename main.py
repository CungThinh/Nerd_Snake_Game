import random
import time
from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

baby_snake = Snake()
food = Food()
score_board = ScoreBoard()
game_over = False

screen.listen()
screen.onkey(key="w", fun=baby_snake.go_up)
screen.onkey(key="a", fun=baby_snake.turn_left)
screen.onkey(key="s", fun=baby_snake.go_down)
screen.onkey(key="d", fun=baby_snake.turn_right)

while not game_over:
    if baby_snake.check_self_collision():
        game_over = True
        score_board.game_over()

    if baby_snake.head.distance(food) < 12:
        baby_snake.extend()
        food.refresh()
        score_board.increase_score()

    if (baby_snake.head.xcor() > 280 or baby_snake.head.ycor() > 280
            or baby_snake.head.xcor() < -280 or baby_snake.head.ycor() < -280):
        game_over = True
        score_board.game_over()

    baby_snake.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()