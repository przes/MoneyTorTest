from flask import Flask
from flask_migrate import Migrate

from config import config_names
from models.model import db
from routes.user_routes import person_bp

app = Flask(__name__)
app.config.from_object(config_names['default'])
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(person_bp, url_prefix = '/persons')


@app.route('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run()
