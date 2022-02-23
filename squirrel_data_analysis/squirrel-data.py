import pandas
def main():
    data = pandas.read_csv("squirrel-data.csv")
    # print(data)
    # squirrel_color_list = data["Primary Fur Color"].to_list()
    # print(squirrel_color_list)
    # gray_squirrels = squirrel_color_list.count('Gray')
    # cinnamon_squirrels = squirrel_color_list.count('Cinnamon')
    # black_squirrels = squirrel_color_list.count('Black')
    gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
    cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

    squirrel_dict = {
        "Fur color": ['Gray', 'Red', 'Black'],
        "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
    }
    dataframe = pandas.DataFrame(squirrel_dict)
    print(dataframe)
    dataframe.to_csv("squirrel_colors.csv")

if __name__ == '__main__':
    main()