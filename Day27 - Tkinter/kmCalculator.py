import tkinter

window = tkinter.Tk()
window.title("Millas a Km")
window.config(padx = 30, pady = 30)

def millasAKm():
    milla = float(texto.get())
    kilometro = milla * 1.609
    resultado.config(text= round(kilometro,4))

#Boton
boton = tkinter.Button(text = "Calcular", command= millasAKm)
boton.grid(row = 2 , column = 1)

#Entrada de texto
texto = tkinter.Entry(width = 10,)
texto.grid(row = 0, column = 1)

#Labels
millas = tkinter.Label(text="Millas")
millas.grid(row = 0, column = 2)

igual = tkinter.Label(text="es igual a")
igual.grid(row = 1, column = 0)

resultado = tkinter.Label(text="0")
resultado.grid(row = 1, column = 1)

km = tkinter.Label(text="Km")
km.grid(row = 1, column = 2)

window.mainloop()