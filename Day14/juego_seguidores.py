#Quien tiene mas seguidores?
from data_juego import concursantes
import random
import os

def formateo_data(cuenta):
    """Formatea la data de los diccionarios de data_juego"""
    cuenta_nombre = cuenta["nombre"]
    cuenta_descrp = cuenta["descripción"]
    cuenta_pais = cuenta["pais"]
    return f"{cuenta_nombre}, es un {cuenta_descrp}, de {cuenta_pais}."

def chequeo_respuesta(respuesta,a_seguidores, b_seguidores):
    """Compara la respuesta con la cantidad de seguidores y devuelve T o F."""
    if a_seguidores > b_seguidores:
        return respuesta =="a"
    else:
        return respuesta == "b"

puntaje = 0
continua_el_juego = True
cuenta_b = random.choice(concursantes)

while continua_el_juego:
        
    cuenta_a = cuenta_b
    cuenta_b = random.choice(concursantes)
    
    while cuenta_a == cuenta_b:
        cuenta_b = random.choice(concursantes)

    print(f"Compara A:{formateo_data(cuenta_a)}")
    print(f"Contra B:{formateo_data(cuenta_b)}")

    respuesta = input("Quien tiene más seguidores? Ingresa 'A' o 'B': ").lower()

    a_cant_seguidores = cuenta_a["cant_seguidores"]
    b_cant_seguidores = cuenta_b["cant_seguidores"]

    es_correcto = chequeo_respuesta(respuesta,a_cant_seguidores,b_cant_seguidores)

    os.system('cls')

    if es_correcto:
        puntaje +=1
        print("¡Acertaste!")
    else:
        continua_el_juego = False
        print(f"Lamentablemente, te equivocaste. Tu puntaje final es: {puntaje}")