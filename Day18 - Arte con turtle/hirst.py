import turtle as t
import random

tortu = t.Turtle()
tortu.speed(12)
tortu.pensize(3)
pantalla = t.Screen()
pantalla.colormode(255)

lista_colores = []
def lista_colores_random():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)

for _ in range(30):
    lista_colores.append(lista_colores_random())

tortu.penup()
tortu.setheading(225)
tortu.forward(500)
tortu.setheading(0)

def puntueado_fila():
    for _ in range(14):
        tortu.dot(20,random.choice(lista_colores))
        tortu.fd(50)
        tortu.penup()

puntueado_fila()

pantalla.exitonclick()