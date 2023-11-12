import json

from flask import Flask, request, Response

app = Flask(__name__)
print(__name__)
@app.route('/')
def get_root():
    return 'Moro'


@app.route('/fuck')  #http://127.0.0.1:5000/fuck?name=daaaaaaamn & lol=kek
def get_fuck():
    print(request.args)
    name = request.args.get('name')
    lol = request.args.get('lol')
    return f'Fuck! {name} /// {lol} '

@app.route('/damn/<name>')  #http://127.0.0.1:5000/damn/fuck!
def get_damn(name):
    return f'Daaaaaaamn! {name}'

@app.route('/multiply/<num>')
def multiply(num):
    num = int(num)   # try: ... exept ValueError: 'print error on the screen'
    if 0 < num < 100:
        result = num * num
        response_data = {'msg': 'calculation complete', 'input_num': num, 'result': result}
        return response_data
    else:
        response_data = { 'msg': 'input out of bounds' }
        # convert python dict to json format 'manually'
        response_data = json.dumps(response_data)
        response = Response(response=response_data, status=400, nimetype='application/json')  #content type in web
        return response

if __name__ == '__main__':
    app.run(use_reloader=True) # host='127.0.0.1', port=3000