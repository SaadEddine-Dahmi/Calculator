from tkinter import *
from tkinter import ttk
window = Tk()
window.title ("Calculator test")
window.resizable(0, 0)

def insert(text):
	if text != "=":
		En.insert(END , text)
	else:
		var = En.get()
		try:
			operation = eval(var)
			En.delete(0, "end")
			En.insert(0, "{}".format(operation))
		except:
			En.delete(0, "end")
			En.insert(0, string)


def button(text , clmn ,rw):
	ttk.Button(window , text = text , command = lambda:insert(text)).grid(column = clmn , row = rw , ipadx= 1 , ipady= 6 )

En = ttk.Entry(window , font = "arial 15")
En.grid(column = 0 , row = 0 , columnspan = 4 , ipadx = 4 , ipady = 8)

button("1", 0, 1)
button("2", 1, 1)
button("3", 2, 1)
button("+", 3, 1)

button("4", 0, 2)
button("5", 1, 2)
button("6", 2, 2)
button("-", 3, 2)

button("7", 0, 3)
button("8", 1, 3)
button("9", 2, 3)
button("*", 3, 3)



button("/", 3, 5)
button(".", 1, 5)
button("=", 2, 5)
button("0", 0, 5)


window.mainloop()