from turtle import Turtle


class Paleta(Turtle):

    def __init__(self,x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x_cor,0)

    def arriba(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def abajo(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)