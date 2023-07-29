from flask import Flask,request,render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/calculator", methods=["GET", "POST"])
def math_opertaion():
    operation = request.json["operation"]
    num1 = float(request.json["num1"])
    num2 = float(request.json["num2"])
    if operation == "add":
        result = num1+num2
    elif operation == "multiply":
        result = num1*num2    
    elif operation == "div":
        result = num1/num2
    else:
        result = num1-num2    
    return result     

print(__name__)
if __name__ == "__main__":
    app.run(debug=True)