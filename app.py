from flask import Flask

from api import greeting, fetch_customers


def init_routes(app: Flask) -> None:
	app.add_url_rule('/', 'greeting', greeting, methods=['GET'])
	app.add_url_rule('/customers', 'customers', fetch_customers, methods=['GET'])

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.ProductionConfig')
	print(app.config['MYSQL_DB_CONFIG'])
	init_routes(app)

	return app

if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0', port=5001)
