from flask import Flask

app = Flask(__name__)

def prime_number(var):

    loppu = int((var ** 0.5) + 1)

    for i in range(2, loppu):
        if var % i == 0:
            output = False
            var = 'luku'
            return output

    if var != 'luku':
        output = True
        return output

def error(var):
    try:
        var = int(var)
        return False
    except ValueError:
        return True

@app.route('/')
def get_root():
    return 'Now <i>"<a href=\'http://127.0.0.1:3000/alkuluku\'>http://127.0.0.1:3000/alkuluku</a>"</i> is avalable'

@app.route('/alkuluku')
def instructions():
    return ('U can add any number to the url: "/alkuluku/<b><i>your_num</i></b>", '
            'then program will return is it Prime number or not')

@app.route('/alkuluku/<num>')
def alkuluku(num):
    if error(num):
        output = str(num) + ' - not a num 😠 '
        return output

    num = int(num)
    boolean = prime_number(num)
    output = {"Number":num, "isPrime":boolean}
    return output

app.run(use_reloader=True, host='127.0.0.1', port=3000)

