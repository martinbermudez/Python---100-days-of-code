#Heights calculator
"""
altura_estudiantes = input("Ingrese una lista de las alturas de los estudiantes: \n").split()
for n in range(0,len(altura_estudiantes)):
    altura_estudiantes[n] = int(altura_estudiantes[n])
print(altura_estudiantes)
a = 0
for e in altura_estudiantes:
    a += e
promedio = round(a /len(altura_estudiantes),2)
print(promedio)
"""

#Gauss problem
"""
total = 0
for num in range(1,101):
    total += num
print(total)
"""
#Gauss even
"""
total = 0
for num in range(1,101):
    if num %2 == 0:
        total += num

print(total)
"""

#FizzBuzz
"""
for num in range(1, 101):
    if num % 15==0:
        print("FizzBuzz")
    elif num % 5==0:
        print("Buzz")
    elif num %3==0:
        print("Fizz")
    else:
        print(num)
"""
#Generador de Contraseñas:
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letras= int(input("Cuantas letras debe contener la contraseña?\n"))
numeros = int(input("Cuantos numeros debe contener la contraseña?\n"))
simbolos = int(input("Cuantos simbolos debe contener la contraseña?\n"))
contraseña = []

for l in range(1,letras +1):
    contraseña += letters[random.randint(0,len(letters)-1)]
for n in range(1, numeros +1):
    contraseña += numbers[random.randint(0,len(numbers)-1)]
for s in range(1, simbolos +1):
    contraseña += symbols[random.randint(0,len(symbols)-1)]
print(contraseña)
random.shuffle(contraseña)

contraseña_real = ""
for i in contraseña:
    contraseña_real += i
print(contraseña_real)