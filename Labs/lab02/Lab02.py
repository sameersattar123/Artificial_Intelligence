# Task 01

# Write a program that converts a positive integer into the Roman number system. The Roman number
# system has digits I (1), V (5), X (10), L (50), C(100), D(500) and M(1000). Numbers up to 3999 are
# formed according to the following rules:
# a) As in the decimal system, the thousands, hundreds, tens and ones are expressed separately.
# b) The numbers 1 to 9 are expressed as: 1 I 6 VI 2 II 7 VII 3 III 8 VIII4 IV 9 IX 5 V (An I preceding
# a V or X is subtracted from the value, and there cannot be more than threeI’s in a row.)
# c) Tens and hundreds are done the same way, except that the letters X, L, C, and C, D, Mare used
# instead of I, V, X respectively.
# Example: Your program should take an input, such as 1978, and convert it to Roman numerals,
# MCMLXXVIII.

def integer_to_roman(num):
    if num <= 0 or num >= 4000:
        return "Invalid number"

    # Define symbols and their values
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Initialize result string
    result = ''

    # Convert integer to Roman numerals
    i = 0
    while num > 0:
        if num - values[i] >= 0:
            result += symbols[i]
            num -= values[i]
        else:
            i += 1

    return result

# Convert 1978 to Roman numerals
roman_numeral = integer_to_roman(1876)
print("Roman numeral for 1978:", roman_numeral)




# Task 02

# Write a program that calculates the user’s body mass index (BMI) and classify it as underweight,normal, overweight, or obese, based on the table from the United States Centers for Disease Control.

# def calculateBMI(weight , height):
#     return weight / (height** 2)

# def classifyBMI(bmi):
#     if(bmi > 0  and bmi < 18.5 ):
#         print("you are underWeight")
#     elif (bmi >= 18.5 and bmi < 25):
#         print("you are  normal")
#     elif (bmi >= 25 and bmi < 30):
#         print("you are over weight")
#     elif (bmi >= 30):
#         print("you are obesity")
#     else:
#         print("Please write down the correct range")

# bmi = calculateBMI(90,5)
# print(bmi)
# classifyBMI(bmi)

# Task 03

# Write a program to compute quotient and remainder of a number without using division ('/')operator and modulo ('%') operator. Also mention procedure for calculating

# def findQuotientAndReminder(dividend , divisor):
#     quotient = 0
#     reminder = 0
#     while dividend >= divisor:
#      dividend -= divisor
#      quotient += 1
    
#     reminder = dividend
#     return quotient , reminder



# dividend = int(input("Enter the dividend: "))
# divisor = int(input("Enter the divisor: "))
# if divisor == 0:
#         print("Cannot divide by zero.")
# else:
#     quotient , reminder = findQuotientAndReminder(dividend, divisor)
# print(quotient)
# print(reminder)
        