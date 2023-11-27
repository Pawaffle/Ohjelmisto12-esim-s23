from flask import Flask, Response

app = Flask(__name__)


@app.route('/summa/<first>/<last>')
def function_sum(first, last):
    sum = 0

    for i in range(int(first), int(last) + 1):
        sum += i

    response = {"first": first, "last": last, "sum": sum}

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
