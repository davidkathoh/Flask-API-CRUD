from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.root_path,'student.db')
db = SQLAlchemy(app)
 
class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(35))
    place_birth = db.Column(db.String(25))

    def __init__(self,name,place_birth):
        self.name = name
        self.place_birth = place_birth



@app.route('/')
@app.route('/student',methods=['GET'])
def get_students():
    students = Student.query.all()
    output = []

    for student in students:
        student_data = {}
        student_data['id'] = student.id
        student_data['name'] = student.name
        student_data['place_birth'] = student.place_birth
        output.append(student_data)

    return jsonify({"students":output})

@app.route('/student',methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name = data['name'],place_birth = data['place_birth'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"result":"success","message":"new user created!"})


@app.route('/student/<student_id>',methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.filter_by(id= student_id).first()
    if not student:
        return jsonify({"message":"no student found"})
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message":"student delete success"})



if __name__ == "__main__":
   app.run(debug=True)