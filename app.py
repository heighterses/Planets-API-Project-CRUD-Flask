from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(message='Hello World!')


@app.route('/not found')
def status_code():
    return jsonify(message='')


@app.route('/parameters')
def param():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f'Hi! {name}, You are not old enough')
    else:
        return jsonify(message=f'Welcome {name}!, Nice to see you')


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message=f'Hi! {name}, You are not old enough')
    else:
        return jsonify(message=f'Welcome {name}!, Nice to see you')


if __name__ == '__main__':
    app.run()
