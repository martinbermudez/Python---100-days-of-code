from turtle import Turtle

class Pelota(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.velocidad = 0.1
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def rebota_y(self):
        self.y_move *= -1

    def rebota_x(self):
        self.x_move *=-1
        self.velocidad = 0.1

    def reseteo(self):
        self.goto(0,0)
        self.rebota_x()