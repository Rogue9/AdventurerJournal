import tkinter
def button_clicked():
    my_label['text'] = input.get()


window=tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = tkinter.Label(text= "I am a label")
my_label['text'] = 'Butt Stuff'
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button= tkinter.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

input = tkinter.Entry(width="10")
input.grid(column=3, row=2)

button2 = tkinter.Button(text="Hey stupid")
button2.grid(column=2, row=0)



window.mainloop()
