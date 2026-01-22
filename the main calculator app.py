from flask import Flask, render_template, request 
from calculator import Calculator # This imports your class

app = Flask(__name__)
calc = Calculator() # This creates the tool

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            
            if operation == "+":
                result = calc.add(num1, num2)
            elif operation == "-":
                result = calc.subtract(num1, num2)
            elif operation == "*":
                result = calc.multiply(num1, num2)
            elif operation == "/":
                # Let the calculator class handle the division logic
                result = calc.divide(num1, num2)
            else:
                error = "Invalid operation"

        except ValueError:
            error = "Please enter valid numbers."
        except ZeroDivisionError:
             # If your Calculator class raises an error for 0, catch it here
            error = "Error: Cannot divide by zero"

    return render_template("index.html", result=result, error=error)
            