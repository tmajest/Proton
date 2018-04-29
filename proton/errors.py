import os
from flask import current_app, render_template 

def not_found(*args, **kwargs):
    """
    Render 404 error.
    """
    path = os.path.join('errors', 'not_found.html')
    return render_template(path), 404

def server_error(*args, **kwargs):
    """
    Render 500 server error.
    """
    path = os.path.join('errors', 'server_error.html')
    return render_template(path), 500
    
