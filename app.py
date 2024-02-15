from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
db = SQLAlchemy(app)


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


# database

class User(db.Model):
    __tablename__= 'users'
    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


if __name__ == '__main__':
    app.run()
