from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def starting_point():
    return 'Goodbye America'


@app.route('/hello')
def hello():
    return 'Hello America'


@app.route('/summa')  # summa? num1=32 & num2=38
def sum_function():
    arguments = request.args
    num1 = arguments.get('num1')
    num2 = arguments['num2']
    my_sum = int(num1) + int(num2)
    #print(arguments)
    return {
        'summa': my_sum
    }

@app.route('/summa/<num1>/<num2>')
def function_sum(num1, num2):
    summa = int(num1) + int(num2)
    return {
        'summa': summa
    }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
