from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
paddle = Paddle(x= 350, y= 0)
screen.update()

def update_screen(func):
    func()
    screen.update()

screen.listen()
screen.onkey(lambda : update_screen(paddle.paddle_up), key='Up')
screen.onkey(lambda : update_screen(paddle.paddle_down), key='Down')



screen.exitonclick()