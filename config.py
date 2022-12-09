import os


class Config(object):
	TESTING = False

class ProductionConfig(Config):
	MYSQL_DB_HOST = os.environ.get('MYSQL_DB_HOST')
	MYSQL_DB_PORT = os.environ.get('MYSQL_DB_PORT')
	MYSQL_DB_USER = os.environ.get('MYSQL_DB_USER')
	MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME')
	MYSQL_DB_PASSWORD = os.environ.get('MYSQL_DB_PASSWORD')

	MYSQL_DB_CONFIG = {
		'host': MYSQL_DB_HOST,
		'port': MYSQL_DB_PORT,
		'user': MYSQL_DB_USER,
		'password': MYSQL_DB_PASSWORD,
		'db': MYSQL_DB_NAME
	}
