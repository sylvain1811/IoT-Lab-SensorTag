from flask import Flask, jsonify, request
from backend import read_temp, buzzer, sensors_macaddr
from threading import Thread

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/temperature/<int:sensor_id>')
def read_temperature(sensor_id):
    temp = read_temp(sensor_id)
    if temp is not None:
        return jsonify(sensor=sensor_id, temperature=temp)
    else:
        return "Unkown sensor id"


@app.route('/buzz', methods=['GET', 'POST'])
def start_buzz():
    if request.method == 'POST':
        content = request.get_json()
        if all(item in content.keys() for item in ['sensor_id', 'n_bip']):
            sensor_id = int(content['sensor_id'])
            n_bip = int(content['n_bip'])
            if sensor_id not in sensors_macaddr.keys():
                return "Unknoww sensor"
            t = Thread(target=buzzer, args=(sensor_id, n_bip))
            t.start()
            return "Buzz started"
    return 'Use POST method'


if __name__ == '__main__':
    app.run(host='localhost', port=5004)
