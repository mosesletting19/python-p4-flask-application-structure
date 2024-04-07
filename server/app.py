from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # This will print the string to the console
    return f'<p>{text}</p>'

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(num + 1))  # Adjusted range to include 0 to num
    return f'<pre>{numbers}</pre>'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return str(result) if result is not None else 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
