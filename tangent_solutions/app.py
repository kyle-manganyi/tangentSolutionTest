from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import re


# init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.leaves')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init DB
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)

# models


class employee(db.Model):
    emp_number = db.Column(db.String(30), unique=True, primary_key=True)
    phone_number = db.Column(db.String(10))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    leaves = db.relationship("leave")

    def __init__(self, emp_number, phone_number, first_name, last_name):
        self.emp_number = emp_number
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name


class leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_number = db.Column(db.Integer, db.ForeignKey('employee.emp_number'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    days_of_leave = db.Column(db.Integer)
    status = db.Column(db.String(15))

    def __init__(self, emp_number, start_date, end_date, days_of_leave, status):
        self.emp_number = emp_number
        self.start_date = start_date
        self.end_date = end_date
        self.days_of_leave = days_of_leave
        self.status = status

# Schemas


class employeeSchema(ma.Schema):
    class Meta:
        fields = ('emp_number', 'phone_number', 'first_name', 'last_name')


class leaveSchema(ma.Schema):
    class Meta:
        fields = ('emp_number', 'days_of_leave', 'status')


# init Schema
leave_schema = leaveSchema(strict=True)
leaves_schema = leaveSchema(many=True, strict=True)
employee_schema = employeeSchema(strict=True)

# Api routes
@app.route('/')
def home():
  return 'kyle is here'

@app.route('/leave', methods=['GET'])
def view_leave():
    all_leaves = leave.query.all()
    result = leaves_schema.dump(all_leaves)
    return jsonify(result.data)


@app.route('/leave/<id>/<status>', methods=['PUT'])
def edit_product(id, status):
    changed_status = leave.query.get(id)
    changed_status.status = status
    db.session.commit()
    return leave_schema.jsonify(changed_status)


@app.route('/user', methods=['POST'])
def create_user():
    emp_number = request.json['emp_number']
    pattern = re.compile("TS\d{4}")
    if(pattern.match(emp_number)):

        phone_number = request.json['phone_number']
        first_name = request.json['first_name']
        last_name = request.json['last_name']

        new_user = employee(emp_number, phone_number, first_name, last_name)

        db.session.add(new_user)
        db.session.commit()

        return "okay"
    else:
        return "invalid employee number"


@app.route('/leave', methods=['POST'])
def create_leave():
    emp_number = request.json['emp_number']
    employee_leave = employee.query.get(emp_number)
    start_date = datetime.strptime(request.json['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(request.json['end_date'], '%Y-%m-%d')
    days_of_leave = request.json['days_of_leave']
    status = "New"
    if(employee_leave is not None):
        if(start_date < end_date):

            leave_request = leave(emp_number, start_date,
                                  end_date, days_of_leave, status)

            db.session.add(leave_request)
            db.session.commit()

            return leave_schema.jsonify(leave_request)
        else:
            return "dates invalid"
    else:
        return "Employee Does not exist"


# run server
if __name__ == "__main__":
  db.create_all()
  app.run(host='0.0.0.0',port=5000)
