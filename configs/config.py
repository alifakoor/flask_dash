import os


class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.environ.get('MYSQL_USER', 'root'),
        os.environ.get('MYSQL_PASSWORD', ''),
        os.environ.get('MYSQL_URI', 'localhost'),
        os.environ.get('MYSQL_DB_NAME', 'shrimp')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN = {'username': 'admin',
             'email': 'admin',
             'password': 'admin'}

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.environ.get('MYSQL_USER', 'root'),
        os.environ.get('MYSQL_PASSWORD', ''),
        os.environ.get('MYSQL_URI', 'localhost'),
        os.environ.get('MYSQL_DB_NAME', 'shrimp')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
