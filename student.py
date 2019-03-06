from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.root_path,'student.db')
db = SQLAlchemy(app)
 
class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(35))
    place_birth = db.Column(db.String(25))


@app.route('/')
@app.route('/student',methods=['GET'])
def get_students():
    return "get student"

@app.route('/student',methods=['POST'])
def add_student():
    return "student added"

@app.route('/student',methods=['UPDATE'])
def update_student():
    return "update student"

@app.route('/student',methods=['DELETE'])
def delete_student():
    return "delete student"



if __name__ == "__main__":
   app.run(debug=True)