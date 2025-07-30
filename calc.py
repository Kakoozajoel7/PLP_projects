# calc.py
x = int(input("Enter the first number: "))
y= int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
elif operation == "/":

    if y == 0:
        result = "Error: Division by zero is undefined."
    else:
        result = x / y
else:
    result = "Invalid operation."

print(f"{x} {operation} {y} = {result}")
