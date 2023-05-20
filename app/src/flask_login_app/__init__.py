from logging.config import dictConfig
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(filename)s - %(name)s(%(lineno)d) - %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'default',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/usr/src/apps/flask_login_app/logs/info.log',
            'when': 'MIDNIGHT',
            'backupCount': 31
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi', 'file']
    }
})


# flask extensions
db = SQLAlchemy()   
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # FlaskのConfigを読み込む
    app.config.from_object('flask_login_app.config.AppConfig')

    # Flask-SQLAlchemy初期化
    db.init_app(app)

    # Flask-Bcrypt初期化
    bcrypt.init_app(app)

    # Flask-Login初期化
    login_manager = LoginManager()
    login_manager.login_view = 'auth.signin'
    login_manager.init_app(app)

    # ログインユーザーの取得
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .views.auth import auth_blueprint
    from .views.main import main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
