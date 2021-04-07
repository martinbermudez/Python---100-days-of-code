import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width= 500, height = 300)
window.config(padx = 20, pady = 20)

def button_clicked():
    nuevo_texto = textbox.get()
    my_label.config(text = nuevo_texto)
    print("I got clicked")


#Label
my_label = tkinter.Label(text ="Label", font=("Arial",24,"italic"))
my_label.grid(column = 0, row= 0)
my_label.config(padx = 50, pady=50)

#Button
button = tkinter.Button(text = "Clic", command = button_clicked)
button.grid(column= 1, row = 1)

new_button = tkinter.Button(text = "New button", command = button_clicked)
new_button.grid(column= 3, row = 0)
#Entry
textbox = tkinter.Entry(width = 10)
textbox.grid(column = 4, row = 3)


window.mainloop()