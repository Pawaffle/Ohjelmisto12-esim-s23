from flask import Flask, Response
import mysql.connector, json

app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='username',
         password='password',
         autocommit=True
         )

def get_airport_by_icao_code(ICAO_code):
    cursor = yhteys.cursor()
    cursor.execute(f"select name, municipality from airport where ident = '{ICAO_code}'")
    result = cursor.fetchone()
    if result:
        data = {
            'ICAO': ICAO_code,
            'Name': result[0],
            'Municipality': result[1]
        }
        status_code = 200

    else:
        data = {
            'ICAO': ICAO_code,
            'Name': 'Not found or doesn\'t exist',
            'Municipality': 'Not found or doesn\'t exist'
        }
        status_code = 400

    return data, status_code


@app.route('/')
def get_root():
    return 'Now <i>"<a href=\'http://127.0.0.1:3000/kenttä\'>http://127.0.0.1:3000/kenttä</a>"</i> is avalable'

@app.route('/kenttä')
def instructions():
    return ('U can add any number to the url: "http://127.0.0.1:3000/kenttä/<b><i>your_ICAO</i></b>", '
            'then program will return is it Prime number or not')

@app.route('/kenttä/<ICAO>')
def airport(ICAO):
    response_data, status_code = get_airport_by_icao_code(ICAO)
    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=status_code, mimetype="application/json")
    return response


app.run(use_reloader=True, host='127.0.0.1', port=3000)