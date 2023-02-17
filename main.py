import turtle
import pandas


screen = turtle.Screen()
screen.title(' U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)
guess = 0
answer_dict = []
on_game = False
while not on_game:
    data = pandas.read_csv('50_states.csv', names=['state', 'x', 'y'])
    answer_state = screen.textinput(title=f'{guess}/50 States Correct', prompt='What is another states name?').title()
    states = data['state']

    if answer_state in data.state.values:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        guess += 1
        answer_dict.append(answer_state)
        coords = data.loc[data['state'] == answer_state]
        xcord = int(coords['x'])
        ycord = int(coords['y'])
        t.goto(xcord, ycord)
        t.write(answer_state)

    if answer_state == 'Exit':
        missing_states = []
        for state in data['state']:
            if state not in answer_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States_to_learn.csv')
        break




screen.exitonclick()
