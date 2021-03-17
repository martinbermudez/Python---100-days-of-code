MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "costo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 3.0,
    }
}

ganancia = 0
recursos = {
    "agua": 300,
    "leche": 200,
    "cafe": 100,
}

def hay_suficiente_recursos(ingredientes_orden):
    for ing in ingredientes_orden:
        if ingredientes_orden[ing] >= recursos[ing]:
            print(f"Lamentablemente no hay suficiente {ing}.")
            return False
    return True

def proceso_monedas():
    """Devuelve el total calculado de las monedas ingresadas"""
    print("Ingrese las monedas.")
    total = int(input("Cuantos 'quarters'?: ")) * 0.25
    total += int(input("Cuantos 'dimes'?: ")) * 0.1
    total += int(input("Cuantos 'nickles'?: ")) * 0.05
    total += int(input("Cuantos 'pennies'?: ")) * 0.01
    return total

def transaccion_completa(dinero_recibido, costo_de_bebida):
    """Devuelve True cuando el pago es aceptado o Falso si la plata es insuficiente"""
    if dinero_recibido >= costo_de_bebida:
        cambio = round(dinero_recibido - costo_de_bebida,2)
        print(f"El cambio de la transacción es de ${cambio}")
        global ganancia
        ganancia += costo_de_bebida
        return True
    else:
        print("Lo lamento, no es suficiente dinero. Devolveré el dinero.")
        return False

def preparacion_cafe(nombre_cafe, ingredientes_orden):
    """Elimina los ingredientes de la bebida seleccionada de los recursos de la maquina"""
    for item in ingredientes_orden:
        recursos[item] -= ingredientes_orden[item]
    print(f"Su cafe {nombre_cafe} esta servido.☕")

encendido = True

while encendido:
    eleccion = input("Que tipo de cafe te puedo servir? (espresso/latte/cappuccino): ").lower()
    if eleccion == "off":
        encendido = False
    elif eleccion == "reporte":
        print(f"agua: {recursos['agua']} ml")
        print(f"leche: {recursos['leche']} ml")
        print(f"cafe: {recursos['cafe']} kgs")
        print(f"plata: ${ganancia}")
    else:
        bebida = MENU[eleccion]
        if hay_suficiente_recursos(bebida["ingredientes"]):
            pago = proceso_monedas()
            if transaccion_completa(pago,bebida["costo"]):
                preparacion_cafe(eleccion, bebida["ingredientes"])
