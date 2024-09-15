from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])
def math_operations():
    if(request.method == 'POST'):
        ops = request.form['operator']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = f"The addition of number {num1} and {num2} is {r}"
        if(ops == 'sub'):
            r = num1 - num2
            result = f"The subtraction of number {num2} from {num1} is {r}"
        if(ops == 'div'):
            r = num1 / num2
            result = f"The division of number {num1} by {num2} is {r}"
        if(ops == 'mul'):
            r = num1 * num2
            result = f"The multiplication of number {num1} and {num2} is {r}"
        if(ops == 'pow'):
            r = num1 ** num2
            result = f"The power of number {num1} to {num2} is {r}"
        return render_template('results.html', result=result)

@app.route('/postman', methods = ['POST'])
def math_operations1():
    if(request.method == 'POST'):
        ops = request.json['operator']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = f"The addition of number {num1} and {num2} is {r}"
        if(ops == 'sub'):
            r = num1 - num2
            result = f"The subtraction of number {num2} from {num1} is {r}"
        if(ops == 'div'):
            r = num1 / num2
            result = f"The division of number {num1} by {num2} is {r}"
        if(ops == 'mul'):
            r = num1 * num2
            result = f"The multiplication of number {num1} and {num2} is {r}"
        if(ops == 'pow'):
            r = num1 ** num2
            result = f"The power of number {num1} to {num2} is {r}"
        return jsonify(result)

if __name__ == '__main__':
    app.run('0.0.0.0')