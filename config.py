import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess thing'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	FLASKY_ADMIN = '1043545633@qq.com'

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
								"mysql://root:root@localhost:3306/dev_db"
	UPLOADED_PHOTOS_DEST = os.path.join(os.path.dirname(os.path.realpath(__file__)), "biofiles") 

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
								"mysql://root:root@localhost:3306/test_db"


class  ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
								"mysql://root:root@localhost:3306/pro_db"


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production':DevelopmentConfig,

	'default': DevelopmentConfig
}