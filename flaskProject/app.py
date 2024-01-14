from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World! :) </h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f"hello {name}"


def convert_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


@app.route('/temperature/<celcius>')
def temperature(celcius="0.0"):
    result = f"Celcius is {celcius}. Fahrenheit is " + str(convert_to_fahrenheit(celcius))
    return result


if __name__ == '__main__':
    app.run()
