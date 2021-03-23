from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 2 != 0:
        countdown(work_sec)
        timer_label.config(text="WORK BITCH", fg=GREEN)
    elif reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps, timer
    minutes = '{:0>2}'.format(math.floor(count/60))
    seconds = '{:0>2}'.format(count % 60)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count>0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✅"
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text= canvas.create_text(100, 132, text="00:00", fill='white', font =(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=RED, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(column=1, row=0)
start = Button(text="Start", command=start_timer, highlightthickness=0, fg=YELLOW, bg=RED)
start.grid(column=0, row=2)
reset = Button(text="Reset", command=reset_timer, highlightthickness=0, fg=YELLOW, bg=RED)
reset.grid(column=2, row=2)
check = Label(fg=RED)
check.grid(column=1, row=3)
window.mainloop()