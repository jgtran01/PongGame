from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position_tuple):
        super().__init__()
        self.shape('square')
        self.shapesize(5.0, 1.0)
        self.color('white')
        self.penup()
        self.goto(position_tuple)

    def up(self):
        new_y= self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y= self.ycor() - 20
        self.goto(self.xcor(), new_y)