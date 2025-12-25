if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")