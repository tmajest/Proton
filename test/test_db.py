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

def test_fetch_db_data(app):
    """
    Test that we can fetch test data from the database.
    """
    with app.app_context():
        query = 'select name, feedlink, sitelink from feed order by id'
        rows = get_db().execute(query).fetchall()

    assert rows[0]["name"] == 'testsite1'
    assert rows[1]["name"] == 'testsite2'
    assert rows[2]["name"] == 'testsite3'

    assert rows[0]["feedlink"] == 'testsite1-feedlink.com'
    assert rows[1]["feedlink"] == 'testsite2-feedlink.com'
    assert rows[2]["feedlink"] == 'testsite3-feedlink.com'

    assert rows[0]["sitelink"] == 'testsite1-sitelink.com'
    assert rows[1]["sitelink"] == 'testsite2-sitelink.com'
    assert rows[2]["sitelink"] == 'testsite3-sitelink.com'

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
