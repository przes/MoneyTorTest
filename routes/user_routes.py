from flask import Blueprint

from controllers.user_controller import UserController

controller = UserController()

person_bp = Blueprint('person_bp', __name__)
person_bp.route('/', methods = ['GET'])(controller.index)
person_bp.route('/fetch', methods = ['GET'])(controller.fetch)

