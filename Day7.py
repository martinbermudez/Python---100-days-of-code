#Juego - Ahorcado
import random
import os

def clear():
    os.system('cls')

etapas = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fin_del_juego = False
vidas = 6
lista_palabras = ["anillo", "placard", "agua"]
palabra = random.choice(lista_palabras)
#print(f"Palabra elegida: {palabra}")

display = []

for letra in range(len(palabra)):
    display+="_"
print(display)


while not fin_del_juego:
    letra_elegida = input("Ingrese una letra:\n").lower()
    
    if letra_elegida in display:
        print(f"Ya elegiste esta letra {letra_elegida}! Proba con otra!")
    
    clear()

    for posicion in range(len(palabra)):
        letra = palabra[posicion]
        if letra == letra_elegida:
            display[posicion] = letra
    
    if letra_elegida not in palabra:
        vidas -= 1
        print(f"La letra {letra_elegida} no esta en la palabra! Te quedan {vidas} intentos.")
        if vidas == 0:
            fin_del_juego = True
            print("PERDISTE")
            break    

    print(display)

    if "_" not in display:
        fin_del_juego = True
        print("GANASTE!")
    
    print(etapas[vidas])