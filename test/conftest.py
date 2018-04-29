import pytest
import tempfile
import os

from proton import create_app
from proton.db import init_db, get_db


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    """
    Create a proton app to be used for testing.
    """
    fd, path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE_FILE': path})

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(fd)
    os.unlink(path)

@pytest.fixture
def client(app):
    """
    Returns a test client for the proton app.
    """
    return app.test_client()
