from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.paddle_up, key='Up')
screen.onkey(r_paddle.paddle_down, key='Down')
screen.onkey(l_paddle.paddle_up, key='w')
screen.onkey(l_paddle.paddle_down, key='s')

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()