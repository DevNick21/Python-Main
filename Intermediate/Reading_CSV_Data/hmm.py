import pandas

answer_state = "Ohio"

data = pandas.read_csv("Reading_CSV_Data/50_states.csv")
state_data = data["state"]
x_data = data["x"]
y_data = data["y"]

dd = data[state_data == answer_state]
state_name = dd["state"]
x_position = dd["x"]
y_position = dd["y"]
state_name_string = state_name.item()
state_name_x_position = int(dd.x.iloc[0])
state_name_y_position = int(dd.y.iloc[0])

print(state_name_string, state_name_x_position, state_name_y_position)
