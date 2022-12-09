from flask import current_app, render_template

from database import select


def greeting():
	return '<b>Hello world</b>'

def fetch_customers():
	db_config = current_app.config['MYSQL_DB_CONFIG']
	customers = select(db_config, "SELECT login, password FROM user LIMIT 10")
	return render_template('customer_list.html', customers=customers)

def fetch_items():
	db_config = current_app.config['MYSQL_DB_CONFIG']
	items = select(db_config, "SELECT name, price, total FROM items LIMIT 10")
	return render_template('item_list.html', items=items)
