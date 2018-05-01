import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext

def connect_db():
    """ 
    Connect to the given database and return a connection to it.
    """
    path = current_app.config["DATABASE_FILE"]
    rv = sqlite3.connect(path)
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """
    Gets a connection to the databse. Creates it if one does not already exist and
    stores it in the g object.
    """
    if 'sqlite_db' not in g:
        g.sqlite_db = connect_db()

    return g.sqlite_db

def init_db():
    """ 
    Initialize the database.
    """
    db_schema = current_app.config["DATABASE_SCHEMA"]

    db = get_db()
    with current_app.open_resource(db_schema, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def close_db(*args, **kwargs): 
    """
    Close the database connection.
    """
    db = g.pop('sqlite_db', None)
    if db:
        db.close()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    CLI command to initialize the database.
    """
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """
    Initialize the app. Makes sure that the database is closed when the appcontext is destroyed.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
