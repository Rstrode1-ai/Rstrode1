class Calculator:
    def calculate(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operation"

if __name__ == "__main__":
    calc = Calculator()
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        result = calc.calculate(num1, num2, operation)
        print("Result:", result)

        if input("Calculate again? (y/n): ").lower() != "y":
            break