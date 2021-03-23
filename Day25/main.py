import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list =data['temp'].to_list()
# average = sum(temp_list) / len(temp_list)
# print(round(average, 2))
#
# print(data['temp'].mean())
# print(data['temp'].max())
monday = data[data.day == 'Monday']
print(int(monday.temp)* (9/5) + 32)
#
# print(data[data.temp == data.temp.max()])
gray = 0
red = 0
black = 0
for i in data['Primary Fur Color']:
    if i == "Gray":
        gray +=1
    elif i == "Cinnamon":
        red += 1
    elif i == "Black":
        black += 1
squirrel_color = {
    "colors": ["Gray", "Red", "Black"],
    "Population": [gray, red, black]
}
data = pandas.DataFrame(squirrel_color)
data.to_csv('squirrel_color.csv')
