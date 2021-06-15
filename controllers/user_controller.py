import json

import requests
from dateutil.parser import parse
from flask import jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import model

db = SQLAlchemy()


class UserController:

    def index(self):
        data = db.session.query(model.Person, model.Address, model.Phone, model.Email) \
            .join(model.Address, model.Person.person_id == model.Address.person_id) \
            .join(model.Phone, model.Person.person_id == model.Phone.person_id) \
            .join(model.Email, model.Person.person_id == model.Email.person_id) \
            .add_columns(model.Person.person_id, model.Person.first_name, model.Person.last_name, model.Person.dob,
                         model.Address.street_number, model.Address.city, model.Phone.phone_no, model.Phone.cell_no,
                         model.Email.email) \
            .all()
        return render_template('index.html', title = 'Index', data = data)

    def fetch(self):
        uri = Config.MONEY_TOR_API
        try:
            response = requests.get(uri)
        except requests.ConnectionError:
            return "Connection Error"
        result = response.text

        data = json.loads(result)
        users = model.Person.query.all()
        # create object and save in db
        for item in data["results"]:
            print(item["name"])
            # date_time_obj = datetime.strptime(item["dob"]["date"], '%d/%m/%y %H:%M:%S')
            date_time_obj = parse(item["dob"]["date"])
            person = model.Person(item["login"]["uuid"], item["name"]["first"], item["name"]["first"],
                                  date_time_obj)
            db.session.add(person)
            db.session.flush()
            db.session.commit()

            email = model.Email(person.person_id, item["email"])
            phone = model.Phone(person.person_id, item["phone"], item["cell"])
            address = model.Address(person.person_id, int(item["location"]["street"]["number"]),
                                    item["location"]["city"])

            db.session.add(email)
            db.session.add(phone)
            db.session.add(address)
            db.session.flush()
            db.session.commit()

        return jsonify(data["results"])

    def show(self, person_id):
        pass

    def update(self, person_id):
        pass

    def delete(self, person_id):
        pass
