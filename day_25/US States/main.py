import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle2 = turtle.Turtle()
turtle.shape(image)
turtle2.penup()
turtle2.hideturtle()
screen.setup(width=800, height=600)

total_correct = 0
correct_guesses = []
data = pandas.read_csv("50_states.csv")

while len(correct_guesses) < 50:
    answer_state = (screen.textinput(title=f"{total_correct}/50 States correct",
                                     prompt="What's another state's name?")).title()
    print(answer_state)
    list_of_states = data.state.to_list()
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in correct_guesses]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        #Alternate way I created the x/y coords
        # xcor = data[data.state == answer_state].x
        # ycor = data[data.state == answer_state].y
        # xcor = int(xcor.to_string(index=False))
        # ycor = int(ycor.to_string(index=False))
        # turtle2.goto(xcor, ycor)
        state_data = data[data.state == answer_state]
        turtle2.goto(int(state_data.x), int(state_data.y))
        turtle2.write(answer_state)
        correct_guesses.append(answer_state)
        total_correct += 1