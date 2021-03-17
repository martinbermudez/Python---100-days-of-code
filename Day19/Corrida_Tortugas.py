import turtle as t
import random

pantalla = t.Screen()
pantalla.setup(width=500,height =400)

colores = ["red", "blue", "yellow", "green", "pink", "orange"]


posiciones_eje_y = [-70,-40,-10,20,50,80]
carrera = False

competidoras = []

for tortu in range (0,6):
    nueva_tortuga = t.Turtle("turtle")
    nueva_tortuga.penup()
    nueva_tortuga.color(colores[tortu])
    nueva_tortuga.goto(x = -230, y=posiciones_eje_y[tortu])
    competidoras.append(nueva_tortuga)


apuesta = pantalla.textinput(title="ULTIMATE TURTLE RACE!",prompt= "On which turtle would you bet? Enter the color: ").lower()
while apuesta not in colores:
    apuesta = pantalla.textinput("ERROR!", "Please choose a color that matches the turtles:")

if apuesta:
    carrera = True

while carrera:

    for tortuga in competidoras:
        if tortuga.xcor() > 230:
            carrera = False
            color_ganador = tortuga.pencolor()
            if color_ganador == apuesta:
                print(f"You' have won! The {color_ganador} turtle is the winner!")
            else:
                print(f"You' have lost! The {color_ganador} turtle is the winner!")

        distancia = random.randint(0,10)
        tortuga.fd(distancia)
    
pantalla.exitonclick()