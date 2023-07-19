import pandas

data = pandas.read_csv(
    "Reading_CSV_Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# colors = data[color_series == "Gray"]
# print(colors["Primary Fur Color"])

color_series = data["Primary Fur Color"]

full_list = color_series.to_list()

grey = 0
cinnamon = 0
black = 0

for item in full_list:
    if item == "Gray":
        grey += 1
    elif item == "Cinnamon":
        cinnamon += 1
    elif item == "Black":
        black += 1

squirrel_dic = {
    "Fur color": ["grey", "cinnamon", "black"],
    "Count": [grey, cinnamon, black]
}

squirrel_df = pandas.DataFrame(squirrel_dic)
squirrel_df.to_csv("Reading_CSV_Data/squirrel_count.csv")
