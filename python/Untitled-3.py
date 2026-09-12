#same thing in python:

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Operation not recognized"

print("The result is:", result)