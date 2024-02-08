# Task 02

# Write a program that calculates the user’s body mass index (BMI) and classify it as underweight,normal, overweight, or obese, based on the table from the United States Centers for Disease Control.

def calculateBMI(weight , height):
    return weight / (height** 2)

def classifyBMI(bmi):
    if(bmi > 0  and bmi < 18.5 ):
        print("you are underWeight")
    elif (bmi >= 18.5 and bmi < 25):
        print("you are  normal")
    elif (bmi >= 25 and bmi < 30):
        print("you are over weight")
    elif (bmi >= 30):
        print("you are obesity")
    else:
        print("Please write down the correct range")

bmi = calculateBMI(90,5)
print(bmi)
classifyBMI(bmi)

# Task 03

# Write a program to compute quotient and remainder of a number without using division ('/')operator and modulo ('%') operator. Also mention procedure for calculating

