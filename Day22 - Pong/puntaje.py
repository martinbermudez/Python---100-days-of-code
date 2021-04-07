from turtle import Turtle



class Puntaje(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.i_puntaje= 0
        self.d_puntaje= 0
        self.actualizar_puntaje()
        
    def actualizar_puntaje(self):
        self.clear()
        self.goto(-150,270)
        self.write(self.i_puntaje, align="center", font=("Courier",80,"normal"))
        self.goto(150,270)
        self.write(self.d_puntaje, align="center", font=("Courier",80,"normal"))

    def i_punto(self):
        self.i_puntaje += 1
        self.actualizar_puntaje()
    
    def d_punto(self):
        self.d_puntaje += 1
        self.actualizar_puntaje()