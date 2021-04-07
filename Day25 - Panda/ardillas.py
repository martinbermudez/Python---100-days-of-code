import os
import pandas

os.chdir("./Python - 100 days of code/Day25 - Panda")

data = pandas.read_csv("2018_Ardillas.csv")

cant_grises = len(data[data["Primary Fur Color"] == "Gray"])
cant_rojas = len(data[data["Primary Fur Color"] == "Cinnamon"])
cant_negras = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Color": ["Gris", "Roja", "Negro"],
    "Cantidad": [cant_grises, cant_rojas, cant_negras]
}

data_f = pandas.DataFrame(data_dict)
data_f.to_csv("Conteo_ardillas.csv")