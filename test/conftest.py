import pytest
import tempfile
import os

from proton import create_app
from proton.db import init_db, get_db

@pytest.fixture
def app():
    """
    Create a proton app to be used for testing.
    """
    fd, db_file = tempfile.mkstemp()
    schema_file = os.path.join(os.path.dirname(__file__), 'testdata', 'data.sql')

    app = create_app({
        'TESTING': True,
        'DATABASE_FILE': db_file,
        'DATABASE_SCHEMA': schema_file
    })

    with app.app_context():
        init_db()

    yield app

    os.close(fd)
    os.unlink(db_file)

@pytest.fixture
def client(app):
    """
    Returns a test client for the proton app.
    """
    return app.test_client()
