num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2    
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

else:
    result = "Invalid operation"

print("Result:", result)
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")

    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != "y":
        break
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation."

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    operation = input("Choose an operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)
    print("Result:", result)

    if input("Calculate again? (y/n): ").lower() != "y":
        break
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
            return a/b
calc = Calculator()
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    if operation == "+":
        print("Result:", calc.add(num1, num2))
    elif operation == "-":
        print("Result:", calc.subtract(num1, num2))
    elif operation == "*":
        print("Result:", calc.multiply(num1, num2))
    elif operation == "/":
        print("Result:", calc.divide(num1, num2))
    else:
        print("Invalid operation")
    if input("Calculate again? (y/n): ").lower() != "y":
        break