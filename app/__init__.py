from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_install import UploadSet, TEXT, configure_uploads




bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
file = UploadSet('file', TEXT)

login_manager.session_protection = 'strong'


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	configure_uploads(app, file)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	return app