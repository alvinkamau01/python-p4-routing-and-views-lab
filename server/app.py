from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Python Operations with Flask Routing and Views</h1>"""

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    
    for i in range(1, param + 1):
        return str(i)



@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):

    num1 = int(num1)
    num2 = int(num2)

    if operation == 'div':
            return num1 / num2

    result = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '%': num1 % num2,
    }.get(operation)  # Use a dictionary for efficient calculations

    return str(result)  # Return the result as a string

if __name__ == '__main__':
    app.run(port=5555, debug=True)