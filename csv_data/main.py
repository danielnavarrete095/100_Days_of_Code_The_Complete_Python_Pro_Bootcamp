from audioop import avg
import os
import csv
import pandas
def main():
    # with open("weather_data.csv", 'r') as file:
    #     data = file.readlines()
    # for i, line in enumerate(data):
    #     data[i] = line.replace('\n', '')
    # print(data)
    
    # with open("weather_data.csv", 'r') as file:
    #     data = csv.reader(file)
    #     temperatures = []
    #     print(data)
    #     for row in data:
    #         print(row)
    #         temp_str = row[1]
    #         if temp_str != "temp":
    #             temperatures.append(int(temp_str))
    #     print(temperatures)
    
    data = pandas.read_csv("weather_data.csv")
    # Convert a dataframe(table) to a dict
    data_dict = data.to_dict()
    # print(data_dict)
    # Convert a series(column) to a list
    temp_list = data["temp"].to_list()
    # print(temp_list)
    # avg_temp = 0
    # for temp in temp_list:
    #     avg_temp += temp
    # avg_temp /= len(temp_list)
    # print(avg_temp)
    avg_temp = sum(temp_list) / len(temp_list)
    # print(avg_temp)

    avg_temp = data["temp"].mean()
    # print(avg_temp)

    max_temp = data["temp"].max()
    # print(max_temp)

    # print(data.temp)

    # Get a row
    # data_row = data[data["day"] == "Monday"]
    # print(data_row)
    # Get the row with the max temp
    # max_temp_row = data[data["temp"] == data["temp"].max()]
    # print(max_temp_row)
    
    monday = data[data["day"] == "Monday"]
    print(monday.condition)
    monday_temp_f = int(monday.temp) * 9 / 5 + 32
    print(monday_temp_f)

    # Create a dataframe from scratch
    data_dict = {
        "students": ["Daniel", "Melissa", "Edith"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    print(data)
    data.to_csv("new_data.csv")


if __name__ == '__main__':
    main()