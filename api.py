from flask import current_app, render_template

from database import select


def greeting():
	return '<b>Hello world</b>'

def fetch_customers():
	db_config = current_app['MYSQL_DB_CONFIG']
	customers = select(db_config, "SELECT login, password FROM customers LIMIT 10")
	return render_template('customer_list.html', customers=customers)
