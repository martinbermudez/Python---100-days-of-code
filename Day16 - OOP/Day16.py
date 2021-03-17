from turtle import Turtle, Screen
from prettytable import PrettyTable
"""
jose = Turtle()
print(jose)
jose.shape("turtle")
jose.color("Dark Orchid")
jose.fd(100)
mi_pantalla = Screen()
print(mi_pantalla.canvheight)
mi_pantalla.exitonclick()
"""
table = PrettyTable()
table.field_names = ["Cafe", "Precio"]
table.add_row(["Espresso", 2.20])
table.add_row(["Mocha", 5.00])
table.add_row(["Latte", 2.50])

table.align = "l"
print(table)