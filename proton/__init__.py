from flask import Flask

def create_app(config=None):
    """
    Initialize application. Use config if provided.
    """

    app = Flask(__name__, instance_relative_config=True)

    import os
    app.config.update(dict(
        DATABASE_FILE=os.path.join(app.instance_path, 'proton.db'),
        DATABASE_SCHEMA=os.path.join(app.root_path, 'conf', 'schema.sql')
    ))

    if config:
        app.config.update(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .db import init_app
    init_app(app)

    from . import proton
    app.register_blueprint(proton.bp)

    from .errors import not_found, server_error
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)

    return app
