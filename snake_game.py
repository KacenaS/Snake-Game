from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen settings
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
sboard = Scoreboard()

# Keybord settings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game mode
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        sboard.increase_points()
        snake.extend()

    # Collision with wall
    if (
        snake.head.xcor() > 300
        or snake.head.xcor() < -300
        or snake.head.ycor() > 350
        or snake.head.ycor() < -350
    ):
        sboard.reset()
        snake.reset()

# Collision with tail
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        sboard.reset()
        snake.reset()


screen.exitonclick()
