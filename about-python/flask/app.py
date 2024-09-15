from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hw1')
def hello_world1():
    return 'Hello, World!1'

@app.route('/hw2')
def hello_world2():
    return '<h1>Hello, World!2</h1>'

@app.route('/test')
def test():
    a = 5+6
    return f"this is test route{a}"

@app.route('/test2/x')
def test2():
    data = request.args.get('x')
    return f"<h1>this is test2 data {data}</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0")