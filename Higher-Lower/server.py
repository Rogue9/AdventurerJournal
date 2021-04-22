from flask import Flask
app = Flask(__name__)
import random
colors = ["blue", "red", "green", "pink", "purple", "cyan", "magenta", "orange"]

correct_number = random.randint(0, 9)
@app.route("/")
def game_begin():

    color = random.choice(colors)
    return f'<h1 style="color:{color}">Guess a number between 0 and 9</h1>\n<img src="https://media.giphy.com/media/jFCmxwb7sZUkSkUtli/giphy.gif"> {correct_number}'

@app.route("/<number>")

def check_answer(number):
    color = random.choice(colors)
    if int(number) == int(correct_number):
        return f'<h1 style="color:{color}">That is right!</h1>\n<img src="https://media.giphy.com/media/egw7kCG9AzQcyqNkTp/giphy.gif">'
    elif int(number) <= int(correct_number):
        return f'<h1 style="color:{color}">That is too low!</h1>\n<img src="https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif">'

    elif int(number) >= int(correct_number):
        return f'<h1 style="color:{color}">That is too high!</h1>\n<img src="https://media.giphy.com/media/41g6S55zT5h9RpxgW0/giphy.gif">'

if __name__== "__main__":
    app.run(debug=True)