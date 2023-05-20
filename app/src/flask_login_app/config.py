"""
FlaskのConfigを提供する
https://flask.palletsprojects.com/en/2.3.x/config/
"""


class AppConfig(object):
    # セッション Cookie に安全に署名するために使用される秘密キー
    SECRET_KEY = 'fbc0b8ddc8deba4769b780a959405de3370c883f6c6b47499487e364e17b24a1'

    # セッション Cookieの名前
    SESSION_COOKIE_NAME = 'flask_login_app'

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': "flask_login_app",
      'password': "flask_login_app",
      'host': "flask_login_app_db",
      'db_name': "flask_login_app_db"
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False