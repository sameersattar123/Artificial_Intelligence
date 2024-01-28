# Exercise Python input /output Basic operations

# (i) Write a Python program to swap 4 variables values (input four values

# a = int(input("Enter the value of a"))
# b = int(input("Enter the value of b"))
# c = int(input("Enter the value of c"))
# d = int(input("Enter the value of d"))

# print("Before swapping")
# print(f"a={a} , b={b} , c={c} , d={d}")

# temp1 = a 
# a = d
# d = temp1

# temp2 = b
# b = c 
# c = temp2

# print("After swapping")
# print(f"a={a} , b={b} , c={c} , d={d}")

# (ii) Write a Python program to convert temperatures to and from celsius,Fahrenheit.

# def celsiusToFahrenheit(celsius):
#     return (celsius * 9/5) + 32
# def FahrenheitToCelsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# celsius_input = float(input("Enter the temperature in Celsius"))
# fahrenheit_Output  = celsiusToFahrenheit(celsius_input)
# print(f"Temperature in Fahrenheit is {fahrenheit_Output}F")

# fahrenheit_input = float(input("Enter the temperature in Celsius"))
# celsius_Output  = FahrenheitToCelsius(fahrenheit_input)
# print(f"Temperature in Fahrenheit is {celsius_Output}C")

# Exercise: Dictionaries

# (ii)Write a Python script to concatenate following dictionaries to create a new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# result_dic = {}

# result_dic.update(dic1)
# result_dic.update(dic2)
# result_dic.update(dic3)

# print("Expected Result:",result_dic)

# Exercise: List Comprehensions
# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five. 


# original_list = ["ali" , "sameer", "sattar" , "wasey" , "rehman" , "ashar"]

# lowercase_long_words = [word.lower() for word in original_list if len(word) > 5]

# print(lowercase_long_words)

