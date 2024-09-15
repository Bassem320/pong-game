import turtle
from turtle import Turtle
from turtledemo.penrose import start


class Paddle(Turtle):
    
    locations = []
    
    def __init__(self, start_position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(start_position)
        self.penup()
        
        
    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)