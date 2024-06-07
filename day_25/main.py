#
# # with (open("weather_data.csv") as weather_data):
# #     data = weather_data.readlines()
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # print(data["temp"].max())
# #
# # #Get data in columns
# # print(data["condition"])
# # print(data.condition)
#
# #Get data in rows
# # print(data[data.temp == (data.temp.max())])
#
#
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # print((monday_temp * (9/5)) + 32)
#
#
# #Create dataframe from scratch
#
#

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
