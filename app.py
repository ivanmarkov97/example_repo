from flask import Flask

from api import greeting, fetch_customers, fetch_items


def init_routes(app: Flask) -> None:
	app.add_url_rule('/', 'greeting', greeting, methods=['GET'])
	app.add_url_rule('/customers', 'customers', fetch_customers, methods=['GET'])
	app.add_url_rule('/items', 'items', fetch_items, methods=['GET'])

def create_app() -> Flask:
	app = Flask(__name__)
	app.config.from_object('config.ProductionConfig')
	init_routes(app)
	return app

if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0', port=5001)
