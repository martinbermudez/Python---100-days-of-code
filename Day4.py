#Banker roulette
import random
"""
people = input("Ingrese el nombre de todas las personas, separadas por una coma.")
nombres = people.split(",")
#people = ["Martin", "Josefina","Alan", "Tomas","Barbara","Sofia"]
num = random.randint(1,len(nombres))
print(f"{nombres[num]}, is going to buy the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[0][0])
"""
#Treasure Chest v2
"""
fila1 = ['⬜️', '⬜️', '⬜️']
fila2= ['⬜️', '⬜️', '⬜️']
fila3= ['⬜️', '⬜️', '⬜️']
map = [fila1, fila2, fila3]
print(f"{fila1}\n{fila2}\n{fila3}")

posicion = input("Ingrese la posición donde desea esconder el tesoro:\n")
horizontal = int(posicion[0])
vertical = int(posicion[1]) 

map[vertical -1][horizontal-1] = "X"

print(f"{fila1}\n{fila2}\n{fila3}")
"""

#Piedra, papel o tijera
print("PIEDRA, PAPEL O TIJERA!!\n")
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
opciones = [piedra,papel,tijera]

opcion_u1 = int(input("Ingrese 0 por Piedra, 1 por Papel o 2 por Tijera:\n"))

if opcion_u1 >= 3 or opcion_u1<0:
    print("Numero fuera de rango! PERDISTE!")
else:
    print(opciones[opcion_u1])

    opcion_u2 = random.randint(0,2)
    print(opciones[opcion_u2])

    if opcion_u1 == 0 and opcion_u2 == 2:
        print("GANASTE!")
    elif opcion_u2 == 0 and opcion_u1 == 2:
        print("PERDISTE!")
    elif opcion_u2 > opcion_u1:
        print("PERDISTE!")
    elif opcion_u1 > opcion_u2:
        print("GANASTE!")
    else:
        print("EMPATASTE!")



