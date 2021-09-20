from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.goto(0,0)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x_cord = self.xcor() + self.x_move
        new_y_cord = self.ycor() + self.y_move
        self.goto(new_x_cord, new_y_cord)

    def deflect_wall(self):
        self.y_move *= -1

    def deflect_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.deflect_paddle()