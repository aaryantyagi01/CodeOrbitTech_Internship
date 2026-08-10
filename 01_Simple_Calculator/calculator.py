# Simple Calculator - CodeOrbit Tech Internship

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."

print("Result:", result)