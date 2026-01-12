def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

def get_number(prompt):
    return float(input(prompt))

while True:
    n1 = get_number("Enter the first number: ")
    n2 = get_number("Enter the second number: ")
    op = input("Enter an operator (+, -, *, /): ")

    result = calculate(n1, n2, op)
    print("Result:", result)

    if input("Do another calculation? (y/n): ").lower() != "y":
        break

print("Goodbye!")