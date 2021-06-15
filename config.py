import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    ADMINS = ['your-email@example.com']

    LANGUAGES = ['en', 'es']

    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    POSTS_PER_PAGE = 25

    MONEY_TOR_API = 'https://randomuser.me/api/'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'APP_PRODUCTION_DATABASE_URI') or 'mysql://root:123456@127.0.0.1/moneytor'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'APP_PRODUCTION_DATABASE_URI') or 'mysql://root:123456@127.0.0.1/moneytor'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'APP_PRODUCTION_DATABASE_URI') or 'mysql://root:123456@127.0.0.1/moneytor'


config_names = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}

# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#     #                           'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DATABASE_URL') or 'mysql://root:123456@127.0.0.1/centurytex'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
