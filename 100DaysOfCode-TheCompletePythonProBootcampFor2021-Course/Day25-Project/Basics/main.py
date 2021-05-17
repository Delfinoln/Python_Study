# ##### Read a csv file and convert eash line to a list called data
# with open("weather_data.csv") as data:
#     data = data.readlines()
#     data_stripped = []
#     for lines in data:
#         data_stripped.append(lines.strip())
#     print(data_stripped)


# ##### Now use csv library
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


##### Starting with pandas
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])

data_list = data["temp"].to_list()
print(data_list)

sum_list = sum(data_list)
len_list = len(data_list)

avg_list = sum_list/len_list
print(avg_list)

# OR

print(data["temp"].mean())

max_value = data["temp"].max()
print(max_value)

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

print(data[data.temp == max(data.temp)])

monday = data[data.day == "Monday"]
print(monday)
print(monday.condition)

# Create a Dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
