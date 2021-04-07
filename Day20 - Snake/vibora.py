from turtle import Turtle

POSICION_INICIAL= [(0,0), (-20,0), (-40,0)]
DISTANCIA_MOVIMIENTO = 20
ARRIBA = 90
ABAJO = 270
DERECHA = 0
IZQUIERDA = 180

class Viborita():
    
    def __init__(self):
        self.segmentos = []
        self.nueva_vibora()
        self.head = self.segmentos[0]

    def nueva_vibora(self):
        for posicion in POSICION_INICIAL:
            self.añadir_segmento(posicion)

    def añadir_segmento(self, posicion):
        tortu = Turtle("square")
        tortu.color("White")
        tortu.penup()
        tortu.goto(posicion)
        self.segmentos.append(tortu)

    def extension(self):
        self.añadir_segmento(self.segmentos[-1].position())

    
    def reset(self):
        for seg in self.segmentos:
            seg.goto(1000,1000)
        self.segmentos.clear()
        self.nueva_vibora()
        self.head = self.segmentos[0]

    def movimiento(self):
        for seg in range(len(self.segmentos)-1, 0, -1):
            new_x = self.segmentos[seg - 1].xcor()
            new_y = self.segmentos[seg - 1].ycor()
            self.segmentos[seg].goto(new_x, new_y)
        self.head.fd(DISTANCIA_MOVIMIENTO)

    def arriba(self):
        if self.head.heading() != ABAJO:
            self.head.setheading(ARRIBA)
    
    def abajo(self):
        if self.head.heading() != ARRIBA:
            self.head.setheading(ABAJO)
    
    def derecha(self):
        if self.head.heading() != IZQUIERDA:
            self.head.setheading(DERECHA)
    
    def izquierda(self):
        if self.head.heading() != DERECHA:
            self.head.setheading(IZQUIERDA)
            