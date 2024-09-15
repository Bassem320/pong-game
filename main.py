from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up, key='Up')
screen.onkey(r_paddle.paddle_down, key='Down')
screen.onkey(l_paddle.paddle_up, key='w')
screen.onkey(l_paddle.paddle_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if (280 < ball.ycor()) or (ball.ycor() < -280):
        ball.bounce_y()

    # Detect collision with paddel
    if (ball.xcor()>320 and ball.distance(r_paddle)<50) or (ball.xcor()<-320 and ball.distance(l_paddle)<50):
        ball.bounce_x()

    # Detect R paddle misses
    if 380 < ball.xcor():
        # left score increase
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        # right score increase
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()