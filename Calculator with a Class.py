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

print("Result:"), result

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