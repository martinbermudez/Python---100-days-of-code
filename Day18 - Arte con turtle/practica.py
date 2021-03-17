
import turtle as t
import random

tortu = t.Turtle()

tortu.shape("square")
#tortu.color("coral")
tortu.pensize(2)
tortu.speed(12)
colores = ["Coral","Dark orchid","medium aquamarine", "lemon chiffon","sienna","orchid","dark cyan","powder blue", "sandy brown","rosy brown","saddle brown"]
pantalla = t.Screen()
pantalla.colormode(255)

def color_random():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return(r,g,b)
#Shapes
"""
#for _ in range(15):
    tortu.pendown()
    tortu.fd(10)
    tortu.penup()
    tortu.fd(10)

def dibujo(lados):
    tortu.color(random.choice(colores))
    grados = 360/lados
    tortu.color()
    for _ in range(lados):
        tortu.fd(100)
        tortu.right(grados)
        
for i in range(3,11):
    dibujo(i)

"""

#Random walk
"""


direcciones = [0,90,180,270]

def random_walk():
    for _ in range(1,5):
        tortu.setheading(random.choice(direcciones))
        tortu.fd(30)

for _ in range(100):
    tortu.color(color_random())
    random_walk()
"""
# Spirographs
def Spirographs(tamaño_apertura):
    for _ in range(int(360/tamaño_apertura)):
        tortu.color(color_random())
        tortu.circle(100)
        tortu.right(tamaño_apertura)

Spirographs(8)

pantalla.exitonclick()