import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "Reading_CSV_Data/blank_states_img.gif"

screen.addshape(image)


turtle.shape(image)

#! It works o, but it really doesn't work like that, the game crashes if you provide a wrong state
# game_not_over = True

# while game_not_over:
#     answer_state = screen.textinput(
#         title="Guess the State", prompt="What is the state's name?").title()
#     data = pandas.read_csv("Reading_CSV_Data/50_states.csv")
#     state_data = data["state"]
#     x_data = data["x"]
#     y_data = data["y"]
#     if answer_state == "Stop":
#         game_not_over = False
#

#     dd = data[state_data == answer_state]


#     state_name = dd["state"]
#     x_position = int(dd["x"])
#     y_position = int(dd["y"])
#     state_name_string = state_name.item()

#     state_text = turtle.Turtle()
#     state_text.hideturtle()
#     state_text.penup()
#     state_text.goto(x_position, y_position)
#     state_text.write(arg=f"{state_name_string}", font=(
#         "courier", 10, "normal"))

data = pandas.read_csv("Reading_CSV_Data/50_states.csv")
all_states = data.state.to_list()
guessed_states = []
end_game = False

while len(guessed_states) < 50 and end_game == False:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}out of 50 states correct", prompt="What is the state's name?").title()

    state_data = data["state"]

    if answer_state == "Stop":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("Reading_CSV_Data/states_to learn.csv")
        end_game = True
    if answer_state in all_states:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_d = data[state_data == answer_state]
        tim.goto(int(state_d.x.iloc[0]), int(state_d.y.iloc[0]))
        tim.write(answer_state)
