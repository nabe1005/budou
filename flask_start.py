from flask import Flask
from pressure import *
from humidity import *
from temperature import *
app = Flask(__name__)


@app.route('/')
def index():
    temp = temp_start()
    hum = hum_start()
    press = press_start()
    return str(temp) + '　/　' + str(hum) + '　/　' + str(press)


@app.route('/temp')
def temp_check():
    return temp_start()


@app.route('/press')
def press_check():
    return press_start()


@app.route('/hum')
def hum_check():
    return hum_start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
