#!/usr/bin/python3
""" This flask implementation returns id a number is 
passed"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnh():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return "C {}".format(text.replace("_"," "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>',strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{:d} is a number".format(n)


if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000)