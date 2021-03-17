#Blind auction
import os

siguen_ofertando = True
participantes = {}
def oferentes(nombre, oferta):
        participantes[nombre] = oferta


while siguen_ofertando:

    nombre = input("Ingrese su nombre:\n")
    oferta = float(input("Ingrese su oferta:\n"))
    oferentes(nombre, oferta)
    
    resultado = input("Desea ofertar? -Si o -No\n").lower()
    os.system('cls')
    if resultado == "no":
        siguen_ofertando = False

mejor_oferta = 0
mejor_postor = ""
for participante in participantes:
    if participantes[participante] > mejor_oferta:
        mejor_oferta = participantes[participante]
        mejor_postor = participante

print(f"La mejor oferta fue de {mejor_postor} con un valor de ${mejor_oferta}")


    

    

