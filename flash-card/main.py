from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/french_words.csv")
finally:
    words = word_data.to_dict(orient="records")
current_word = {}


def knows_word():
    global current_word, words
    words.remove(current_word)
    to_learn= pandas.DataFrame(words)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_word()


def new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words)
    french_word = current_word["French"]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip)



def flip():
    canvas.itemconfig(canvas_image, image=card_back)
    english_word = current_word["English"]
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=english_word, fill="white")



window = Tk()
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Cards")
flip_timer= window.after(3000, func=flip)
card_back = PhotoImage(file='../images/card_back.png')
card_front = PhotoImage(file="../images/card_front.png")
right_img = PhotoImage(file="../images/right.png")
wrong_img = PhotoImage(file="../images/wrong.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.config(borderwidth=0, command=knows_word)
wrong_button.config(borderwidth=0, command=new_word)
canvas_image = canvas.create_image(400,263,image=card_front)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, 'italic'), tags="language")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, 'bold'), tags="word")
new_word()




window.mainloop()


