#Adivina el numero!
import random

print("Bienvenido a... ¡Adivina el numero!")
print("Estoy pensando un numero del 1 al 100... ¿Podes adivinar cual es?")
numero = random.choice(range(1,100))
print(f"Psst, la respuesta correcta es {numero}") 
intentos = 0

dificultad = input("Ingrese la dificultad. Ingrese 'facil' o 'dificil':\n")
fin_del_juego = False

if dificultad == "facil":
    intentos = 10
    print(f"Tenes {intentos} intentos para adivinar el numero!")
elif dificultad == "dificil":
    intentos = 5
    print(f"Tenes {intentos} intentos para adivinar el numero!")
else:
    print("Error de comando!")

while not fin_del_juego:
    num = int(input("Adivina el numero: "))
    intentos -= 1
    print(f"Te quedan {intentos} intentos para adivinar el numero.")
    if num == numero:
        print(f"Acertaste! el numero era: {numero}. Solo fueron {intentos} intentos!")
        fin_del_juego = True
    elif intentos == 0:
        print("Te quedaste sin intentos! Perdiste.")
        fin_del_juego = True
    elif num < numero:
        print("Muy bajo!")
    else:
        print("Muy alto!")