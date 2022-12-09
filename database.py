from typing import Dict, List

import pymysql


def select(config: Dict, statement: str) -> List:
	output = []

	connection = pymysql.connect(**config)
	with connection:
		with connection.cursor() as cursor:
			cursor.execute(statement)
			schema = [column[0] for column in cursor.description]
			for row in cursor.fetchall():
				output.append(dict(zip(schema, row)))
	return output
