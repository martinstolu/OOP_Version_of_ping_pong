from turtle import Turtle
MOVE = 40

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)

    def upper(self):
        if self.ycor() < 165:
            new_y = self.ycor() + MOVE
            self.goto(x=self.xcor(), y=new_y)

    def lower(self):
        if self.ycor() > -165:
            new_y = self.ycor() - MOVE
            self.goto(x=self.xcor(), y=new_y)