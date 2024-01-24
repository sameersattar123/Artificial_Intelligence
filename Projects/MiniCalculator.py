num1 = int(input("Enter the value of num1"))
num2 = int(input("Enter the value of num1"))
operator = input("Enter the operator")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
elif operator == "%":
    result = num1 % num2
    print(result)
else: 
    print("No result")