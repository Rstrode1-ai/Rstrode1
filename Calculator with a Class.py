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

    input("Calculate again? (y/n): ").lower() != "y":
    