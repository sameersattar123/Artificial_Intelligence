import datetime

# Exercise 1
# Perform the given operations
# I. a Python program to square and cube every number in a given list of integers using Lambda. 

numbers = [1, 2, 3, 4, 5]

square = lambda x: x * x 
cube = lambda x: x * x * x

squared_numbers = list(map(square, numbers))
cubed_numbers = list(map(cube, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Cubed numbers:", cubed_numbers)

# II. a Python program to find if a given string starts with a given character using Lambda.

starts_with_char = lambda string, char: string.startswith(char)

print(starts_with_char("sameer", "s"))
print(starts_with_char("sameer", "S"))


# III. a Python program to extract year, month, date and time using Lambda.

Datetime = datetime.datetime.now()

extractYear = lambda dt: dt.year
extractMonth = lambda dt: dt.month
extractDay = lambda dt: dt.day
extractTime = lambda dt: dt.time()

year = extractYear(Datetime)
month = extractMonth(Datetime)
day =  extractDay(Datetime)
time = extractTime(Datetime)

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)







