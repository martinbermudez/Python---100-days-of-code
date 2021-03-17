from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maquina_dinero = MoneyMachine()
maquina_cafe = CoffeeMaker()
menu = Menu()

prendido = True
maquina_dinero.report()
maquina_cafe.report()

while prendido:
    opciones = menu.get_items()
    eleccion = input(f"Que te puedo servir? {opciones}: ")
    if eleccion == "off":
        prendido = False
    elif eleccion == "reporte":
        maquina_cafe.report()
        maquina_dinero.report()
    else:
        bebida = menu.find_drink(eleccion)
        if maquina_cafe.is_resource_sufficient(bebida) and maquina_dinero.make_payment(bebida.cost):
                maquina_cafe.make_coffee(bebida)