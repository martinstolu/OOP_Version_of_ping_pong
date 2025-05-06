from turtle import Turtle
import time


FD = 1

class Ball(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)
        self.x_move = 3
        self.y_move = 2
        self.move_speed = 0.01

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor,new_y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed -= 0.0005
        if self.move_speed < 0.002:
            self.move_speed = 0.002

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.bounce_x()

