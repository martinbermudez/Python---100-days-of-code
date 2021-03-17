import turtle as t

larry = t.Turtle()
screen = t.Screen()

def correr():
    larry.fd(10)

def derecha():
    larry.right(25)

def atras():
    larry.backward(10)

def izquierda():
    larry.left(25)

def borrar():
    screen.reset()
    larry.home()


screen.listen()
screen.onkey(correr,"w")
screen.onkey(derecha, "d")
screen.onkey(izquierda, "a")
screen.onkey(atras, "s")
screen.onkey(borrar, "c")

screen.exitonclick()