#!/usr/bin/python3
"""This my first Flask instantation"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return  "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnh():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return "C {}".format(text.replace("_"," "))

@app.route('/python/<text>',strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000)