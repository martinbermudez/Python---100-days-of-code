from turtle import Turtle, Screen
from paleta import Paleta
from pelota import Pelota
import time
from puntaje import Puntaje

pantalla = Screen()
pantalla.bgcolor("black")
pantalla.setup(width=800, height=800)
pantalla.title("Pong")
pantalla.tracer(0)

d_paleta = Paleta(350)
i_paleta = Paleta(-350)
pelota = Pelota()
cartel = Puntaje()

pantalla.listen()
pantalla.onkey(d_paleta.arriba,"Up")
pantalla.onkey(d_paleta.abajo,"Down")
pantalla.onkey(i_paleta.arriba,"w")
pantalla.onkey(i_paleta.abajo,"s")

juego_sigue = True
while juego_sigue:
    time.sleep(pelota.velocidad)
    pantalla.update()
    pelota.move()

    #detectar colisión
    if pelota.ycor() > 380 or pelota.ycor() < -380:
        pelota.rebota_y()

    #detectar colision con d_paleta y i_paleta
    if pelota.distance(d_paleta) < 50 and pelota.xcor() > 320 or pelota.distance(i_paleta) < 50 and pelota.xcor() < -320:
        pelota.rebota_x()
        pelota.velocidad *= 0.9

    # detectar cuando pierde la derecha
    if pelota.xcor() > 380:
        pelota.reseteo()
        cartel.i_punto()

     # detectar cuando pierde la izquierda
    if pelota.xcor() < -380:
        pelota.reseteo()
        cartel.d_punto()

















pantalla.exitonclick()
