from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy_utils import PhoneNumber

db = SQLAlchemy()


class Person(db.Model):
    __tablename__ = 'person'

    def __init__(self, uuid, first_name, last_name, dob):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    person_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    uuid = db.Column(db.String(256), unique = True, nullable = False)
    first_name = db.Column(db.String(120), nullable = True)
    last_name = db.Column(db.String(120), nullable = True)
    dob = db.Column(db.DateTime, nullable = True)
    addresses = db.relationship('Address', backref = 'person', lazy = True)
    phones = db.relationship('Phone', backref = 'person', lazy = True)
    emails = db.relationship('Email', backref = 'person', lazy = True)


class Address(db.Model):
    __tablename__ = 'Address'

    def __init__(self, person_id, street_number, city):
        self.person_id = person_id
        self.street_number = street_number
        self.city = city

    address_id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable = False)
    street_number = db.Column(db.Integer, nullable = False)
    city = db.Column(db.String(100), nullable = False)


class Phone(db.Model):
    __tablename__ = 'Phone'

    def __init__(self, person_id, phone_no, cell_no):
        self.person_id = person_id
        self.phone_no = phone_no
        self.cell_no = cell_no

    phone_id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable = False)
    phone_no = db.Column(db.String(20), nullable = False)
    cell_no = db.Column(db.String(20), nullable = False)


class Email(db.Model):
    __tablename__ = 'Email'

    def __init__(self, person_id, email):
        self.person_id = person_id
        self.email = email

    email_id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable = False)
    email = db.Column(db.String(256), nullable = False)
