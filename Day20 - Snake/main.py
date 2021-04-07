import random
from turtle import Screen, Turtle
import time
from vibora import Viborita
from comida import Food
from puntaje import Puntaje
import os

os.chdir(r"C:\Users\Martin\Desktop\Python\Python - 100 days of code\Day20 - Snake")
pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("La viborita")
pantalla.tracer(0)

jorge = Viborita()
comida = Food()
cartel = Puntaje()


pantalla.listen()
pantalla.onkey(jorge.arriba,"Up")
pantalla.onkey(jorge.abajo,"Down")
pantalla.onkey(jorge.derecha,"Right")
pantalla.onkey(jorge.izquierda,"Left")


sigue_el_juego = True
while sigue_el_juego:
    pantalla.update()
    time.sleep(0.1)

    jorge.movimiento()

    #Detectar colision con la comida
    if jorge.head.distance(comida) < 15:
        comida.refresco()
        jorge.extension()
        cartel.nuevo_puntaje()

    #Detectar colision con las paredes
    if jorge.head.xcor() > 280 or jorge.head.xcor() < -280 or jorge.head.ycor() > 280 or jorge.head.ycor() < -280:
        cartel.reset()
        jorge.reset()
    
    #Detectar colision con la cola de la viborita
    for segmento in jorge.segmentos[1:]:
        if jorge.head.distance(segmento) < 10:
            cartel.reset()
            jorge.reset()







pantalla.exitonclick()
