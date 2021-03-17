#Calculadora
def suma(n1, n2):
    """Suma de parametros"""
    return n1 + n2
def resta(n1,n2):
    """Resta de parametros"""
    return n1 - n2
def multiplacacion(n1,n2):
    """Multiplicacion de parametros"""
    return n1*n2
def division(n1,n2):
    """Division de parametros"""
    return n1/n2

Operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplacacion,
    "/": division
}

def calculadora():
    num1 = float(input("Ingrese el primer numero: "))
    continuar = True
    while continuar:
        for op in Operaciones:
            print(op)
        op_simbolo = input("Ingrese una operación: ")

        num2 = float(input("Ingrese el siguiente numero: "))

        operacion_calcular = Operaciones[op_simbolo]
        resultado = operacion_calcular(num1,num2)

        print(f"{num1} {op_simbolo} {num2} = {resultado}")
        
        if input(f"Desea continuar operando con el resultado: {resultado}? -si o -no: ").lower() == "si":
            num1 = resultado
        else:
            continuar = False
            calculadora()

calculadora()