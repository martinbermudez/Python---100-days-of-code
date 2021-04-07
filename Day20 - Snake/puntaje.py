from turtle import Turtle

ALINEAMIENTO = "center"
FUENTE = ("Tahoma", 20, "normal")

class Puntaje(Turtle):
    
    def __init__(self):
        super().__init__()
        self.puntaje = 0
        with open('data.txt') as data:
            self.puntaje_maximo = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.actualizar_tabla()
        self.hideturtle()

    def actualizar_tabla(self):
        self.clear()
        self.write(f"Puntaje: {self.puntaje} Maximo puntaje: {self.puntaje_maximo}",align=ALINEAMIENTO, font=FUENTE)

    def reset(self):
        if self.puntaje > self.puntaje_maximo:
            self.puntaje_maximo = self.puntaje
            with open ("data.txt", mode="w") as data:
                data.write(f"{self.puntaje_maximo}")
        self.puntaje = 0
        self.actualizar_tabla()

    def nuevo_puntaje(self):
        self.puntaje +=1
        self.clear()
        self.actualizar_tabla()
