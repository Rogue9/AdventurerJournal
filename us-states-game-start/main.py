import turtle
import pandas
data = pandas.read_csv('50_states.csv')


# TODO 4: Use a loop to allow more guesses
# TODO 5: Record guesses in a list
# TODO 6: Keep track of score
#         len(correct_guesses)
score = 0
correct_states = []
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
all_states= data.state.to_list()
print(data)
turtle.shape(image)
while score < 50:
# TODO 1:Convert guess to title case
    if score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="Enter a state!").title()
    if score >0:
        answer_state = screen.textinput(title=f"Score: {score} of 50", prompt="Enter another state (or exit)!").title()
    # TODO 2:Check if guess is one of states
    #       Compare to 50 states csv
    # TODO 3: Write guesses on the map
    #       Pull coords from row in 50_states
    if answer_state == "Exit":
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv('states_to_learn.csv')
        break
    for guess in data['state']:

        if answer_state in correct_states:
            pass
        elif answer_state == guess:
            score +=1
            correct_states.append(guess)
            all_states.remove(answer_state)
            state = data[data.state == guess]
            new_x = int(state.x)
            new_y = int(state.y)
            tina = turtle.Turtle(visible=False)
            tina.penup()
            tina.goto(new_x, new_y)
            tina.write(guess, align='center', font=("Arial", 8, 'normal'))
