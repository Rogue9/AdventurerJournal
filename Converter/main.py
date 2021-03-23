from tkinter import *


def convert():
    miles = input.get()
    km = int(miles) * 1.609
    result.config(text=round(km, 1))


window = Tk()
window.title("Miles to KM")
window.config(padx=50, pady=70)

input = Entry(width=20)
input.grid(column=1, row=0)
# input.config(padx=20, pady=5)

miles = Label(text="miles")
miles.grid(column=2, row=0)
miles.config(padx=20, pady=5)

equals = Label(text = "is equal to")
equals.grid(column=0, row=1)
equals.config(padx=20, pady=5)

result = Label(text= "?")
result.grid(column=1, row=1)
result.config(padx=20, pady=5)

kilometers= Label(text= "KM")
kilometers.grid(column=2, row=1)
kilometers.config(padx=20, pady=5)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)
button.config(padx=20, pady=5)





window.mainloop()