import pytest
import sqlite3

from proton.db import get_db, close_db

def test_get_db(app):
    """
    Test that we can fetch the database.
    """
    with app.app_context():
        db = get_db()
        assert db is not None

def test_close_db(app):
    """
    Test that we can successfully close the database.
    """
    with app.app_context():
        db = get_db()
        close_db()

        with pytest.raises(sqlite3.ProgrammingError) as e:
            db.execute('select * from feed;')

        assert 'closed database' in str(e)
