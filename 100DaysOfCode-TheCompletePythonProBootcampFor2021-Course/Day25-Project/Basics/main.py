# ##### Read a csv file and convert eash line to a list called data
# with open("weather_data.csv") as data:
#     data = data.readlines()
#     data_stripped = []
#     for lines in data:
#         data_stripped.append(lines.strip())
#     print(data_stripped)


##### Now use csv library
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)