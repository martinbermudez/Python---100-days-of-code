import turtle as t
import os
import pandas


os.chdir("./Python - 100 days of code/Day25 - Panda/Estados de USA")
IMAGE = "blank_states_img.gif"

data = pandas.read_csv("50_states.csv")

screen = t.Screen()
screen.title("Los estados unidos")
screen.addshape(IMAGE)
turt = t.Turtle()
turt.shape(IMAGE)

guessed_states = []
states = data.state.to_list()

while len(guessed_states) < 50:
    respuesta = screen.textinput(title=f"{len(guessed_states)}/50 Estados correctos", 
    prompt="Indica los estados que conoces:").title()
    
    if respuesta == "Exit":
        states_to_learn = [estado for estado in states if estado not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if respuesta in states:
        guessed_states.append(respuesta)
        marc = t.Turtle()
        marc.hideturtle()
        marc.penup()
        state_row = data[data.state == respuesta]
        marc.goto(int(state_row.x),int(state_row.y))
        marc.write(respuesta)




