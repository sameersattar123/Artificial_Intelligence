import datetime

# Exercise 1

# Perform the given operations
# I. a Python program to square and cube every number in a given list of integers using Lambda. 

# numbers = [1, 2, 3, 4, 5]

# square = lambda x: x * x 
# cube = lambda x: x * x * x

# squared_numbers = list(map(square, numbers))
# cubed_numbers = list(map(cube, numbers))

# print("Original numbers:", numbers)
# print("Squared numbers:", squared_numbers)
# print("Cubed numbers:", cubed_numbers)

# # II. a Python program to find if a given string starts with a given character using Lambda.

# starts_with_char = lambda string, char: string.startswith(char)

# print(starts_with_char("sameer", "s"))
# print(starts_with_char("sameer", "S"))


# III. a Python program to extract year, month, date and time using Lambda.

# Datetime = datetime.datetime.now()

# extractYear = lambda dt: dt.year
# extractMonth = lambda dt: dt.month
# extractDay = lambda dt: dt.day
# extractTime = lambda dt: dt.time()

# year = extractYear(Datetime)
# month = extractMonth(Datetime)
# day =  extractDay(Datetime)
# time = extractTime(Datetime)

# print("Year:", year)
# print("Month:", month)
# print("Day:", day)
# print("Time:", time)

# Exercise 2

# I. You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number 
# of cities from the keyboard and store the data in a file in the order in which they’re entered.

cityData = []
while(True):
    city = input("Enter city name:")
    population = input("Enter population:")
    mayor = input("Enter mayor name:")
    cityData.append({"city":city, "population":population, "mayor":mayor})
    more_data = input("Do you want more data to be added(Y=yes or N=no):")
    if(more_data == 'N' or more_data == 'n'):
        break

f = open("cityData.txt", "w")
f.write("City  Population  Mayor \n")
for i in range(len(cityData)):
    f.write(cityData[i]["city"]+" ")
    f.write(" "+cityData[i]["population"]+ " ")
    f.write(" "+cityData[i]["mayor"]+"  \n")
f.close()



# II. Write a python program to create a data file student.txt and append the message “Now we are AI students”

f = open("student.txt", "a")
f.write("Now we are AI students")
f.close()









