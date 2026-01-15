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
        return a / b
calc = Calculator()

while True:
    num1 = float(input("Enter first number: ")) 
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+,-,*,/):")

    if operation == '+':
        print(calc.add(num1, num2))
    elif operation == '-':
        print(calc.subtract(num1, num2))
    elif operation == '*':
        print(calc.multiply(num1, num2))
    elif operation == '/':
        print(calc.divide(num1, num2))
    else:
        print("Invalid operation")  

    if input("Calculate again? (y/n): ").lower() != "y":
        break
