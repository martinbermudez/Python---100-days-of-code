import os
import csv
import pandas

print(os.getcwd())
os.chdir("./Python - 100 days of code/Day25 - Panda")

data = pandas.read_csv("weather_data.csv")

data_dicc = data.to_dict()
print(data_dicc)

lista_temp = data["temp"].to_list()
print(data["temp"].mean())
print(data["temp"].max())

lunes = data[data.day == "Monday"]
lunes_temp_F = int(lunes.temp) * 9/5 +32
print(lunes_temp_F)
"""
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperaturas = []
    for fila in data:
        if fila[1] != "temp":
            temperaturas.append(int(fila[1]))
    print(temperaturas)

data = pandas.read_csv("wheater_data.csv")
print(data)
"""