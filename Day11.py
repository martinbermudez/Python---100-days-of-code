#Black Jack
import random
import os
cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def repartir_cartas():
    """ Devuelve una carta random del mazo"""
    return random.choice(cartas)

def calcular_puntaje(cartas):
    """Suma el puntaje de las cartas en la lista (parametro)"""
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
        
    if 11 in cartas and sum(cartas) >21:
        cartas.remove(11)
        cartas.append(1)

    return sum(cartas)

def comparar(puntaje_usu, puntaje_compu):
    """Compara ambos puntajes"""
    if puntaje_usu == puntaje_compu:
        return "EMPATE!"
    elif puntaje_compu == 0:
        return "La computadora gana con BLACKJACK!"
    elif puntaje_usu == 0:
        return "El usuario gana con BLACKJACK!"
    elif puntaje_usu > 21:
        return f"Sumaste {puntaje_usu}!, PERDISTE!"
    elif puntaje_compu > 21:
        return f"La computadora sumó {puntaje_compu}!, GANASTE!"
    elif puntaje_compu > puntaje_usu:
        return f"La computadora sumó {puntaje_compu} y vos sumaste {puntaje_usu}, PERDISTE!"
    else:
        return f"La computadora sumó {puntaje_compu} y vos sumaste {puntaje_usu}, GANASTE!"

def jugar_blackjack():
    fin_juego = False
    mano_usuario = []
    mano_computadora = []

    for _ in range(2):
        mano_usuario.append(repartir_cartas())
        mano_computadora.append(repartir_cartas())

    while not fin_juego:

        puntaje_usuario = calcular_puntaje(mano_usuario)
        puntaje_computadora = calcular_puntaje(mano_computadora)
        print(f"Cartas usuario: {mano_usuario}, puntaje: {puntaje_usuario}")
        print(f"La primera carta de la computadora es: {mano_computadora[0]}")

        if puntaje_usuario == 0 or puntaje_computadora == 0 or puntaje_usuario >21:
            fin_juego = True
        else:
            respuesta = input("Ingrese 'si', para obtener una nueva carta, ingrese 'no' para pasar: ").lower()
            if respuesta == "si":
                mano_usuario.append(repartir_cartas())
            else:
                fin_juego = True

    while puntaje_computadora != 0 and puntaje_computadora < 17:
        mano_computadora.append(repartir_cartas())
        puntaje_computadora = calcular_puntaje(mano_computadora)

    print(mano_usuario)
    print(mano_computadora)
    print(comparar(puntaje_usuario,puntaje_computadora))

jugar_blackjack()

while input("Queres seguir jugando al BlackJack? -si o -no: ") == "si":
    os.system('cls')
    jugar_blackjack()