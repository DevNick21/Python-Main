import json

with open("password_manager\data.json", mode="r") as data_file:
    data = json.load(data_file)

print(data["ajajaja"]["password"])
