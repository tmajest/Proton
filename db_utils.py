import sqlite3

def connect_db(path):
	""" 
	Connect to the given database and return a connection to it.
	"""
	rv = sqlite3.connect(path)
	rv.row_factory = sqlite3.Row
	return rv

def get_db(path, g):
	"""
	Gets a connection to the databse. Creates it if one does not already exist and
	stores it in the g object.
	"""
	if not hasattr(g, 'sqlite_db'):
		db = connect_db(path)
		g.sqlite_db = db
	return db

def init_db(app):
	""" 
	Initialize the database.
	"""
	db_file = app.config["DATABASE_FILE"]
	db_schema = app.config["DATABASE_SCHEMA"]

	db = get_db(db_file)
	with app.open_resource(db_schema, mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

def close_db(g):
	"""
	Close the database connection.
	"""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

