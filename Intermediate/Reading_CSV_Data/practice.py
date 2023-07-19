import pandas

data = pandas.read_csv("Reading_CSV_Data/weather_data.csv")

temp_list = data["temp"].to_list()

data_dict = data.to_dict()
# print(data_dict)
# print(temp_list)

maxi_temp = data.temp.max()

# print(data[data.temp == maxi_temp])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
fahrenheit = (monday_temp * 9/5) + 32
print(fahrenheit)
