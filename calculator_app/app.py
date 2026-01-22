  
from flask import Flask, render_template, request 
from calculator import Calculator
app=Flask(__name__)
calc = Calculator()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = calc.add(num1, num2)
                
            elif operation == "subtract":
                result = calc.subtract(num1, num2)
            elif operation == "multiply":
                result = calc.multiply(num1, num2)
            elif operation == "divide":
                result = calc.divide(num1, num2)
               
               
            return render_template("index.html", result=result)
                                   
    if __name__ == "__main__":
        app.run(debug=True)
