#Calculo de área
"""
import math
cobertura = 5
alto = float(input("Cual es la altura de la pared a pintar:\n"))
ancho = float(input("Cual es el ancho de la pared a pintar:\n"))

def area_pintar(alto,ancho,cobertura):
    cantidad_latas = math.ceil((alto*ancho)/cobertura)
    print(f"Necesita {cantidad_latas} latas de pintura para pintar una pared de {alto}x{ancho}")

area_pintar(alto,ancho,cobertura)
"""
#Es un numero primo?
"""
def es_primo(numero):
    es_primo = True
    for i in range(2, numero):
        if numero%i == 0:
            es_primo= False
    if es_primo:
        print(f"El {numero} es primo.")
    else:
        print(f"El {numero} no es primo.")

num = int(input("Ingrese el numero que desea corroborar si es primo:\n"))
es_primo(num)
"""

#Caesar Cipher

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def Caesar_Cipher(texto,giros,direccion):
    texto_encriptado = ""
    if direccion == "desencriptado":
            giros *= -1
    for caracter in texto:
        if caracter in alfabeto:
            posicion = alfabeto.index(caracter)
            nueva_posicion = posicion + giros
            texto_encriptado += alfabeto[nueva_posicion]
        else:
            texto_encriptado += caracter
    print(f"El texto {direccion} es {texto_encriptado}")

continuar = True
while continuar:
    direccion = input("Ingresa 'encriptado' para encriptar o 'desencriptado' para desencriptar el mensaje:\n").lower()
    texto = input("Ingresa tu mensaje:\n").lower()
    giros = int(input("Ingresa la cantidad de giros:\n"))
    giros = giros % 26
    Caesar_Cipher(texto,giros,direccion)
    resultado = input("Desea continuar utilizando el des/encriptado Caesar? 'si' o 'no'").lower()
    if resultado == "si":
        continuar = True
    elif resultado == "no":
        continuar = False
        print("Gracias por usuar Caesar Cipher!")
    else:
        print("Comando Invalido.")



"""
def encriptado(texto,giros):
    texto_encriptado = ""
    for letra in texto:
        posicion = alfabeto.index(letra)
        nueva_posicion = posicion + giros
        nueva_letra = alfabeto[nueva_posicion]
        texto_encriptado +=nueva_letra
    print(f"El texto encriptado es {texto_encriptado}")

def desencriptado(texto_encriptado,giros):
    texto_desencriptado = ""
    for letra in texto_encriptado:
        posicion = alfabeto.index(letra)
        nueva_posicion = posicion - giros
        nueva_letra = alfabeto[nueva_posicion]
        texto_desencriptado += nueva_letra
    print(f"El texto desencriptado es {texto_desencriptado}")

if direccion == "encriptado":
    encriptado(texto,giros)
elif direccion == "desencriptado":
    desencriptado(texto,giros)
else:
    print("Acción invalida!")
"""