from flask import Flask, render_template, g
from feed import Feed
from utils import get_time_str

import db_utils
import os
import provider

app = Flask(__name__)
app.config.update(dict(
    DATABASE_FILE=os.path.join(app.root_path, 'db', 'proton.db'),
    DATABASE_SCHEMA=os.path.join(app.root_path, 'db', 'schema.sql')
))

@app.route('/')
def index():
    """
    Fetches the index page. The index page contains a side panel
    with links to the feed details page of each feed. It also contains
    a middle panel with a list of all of the lastest entries.
    """
    feeds = provider.get_feeds(app.config["DATABASE_FILE"], g)
    feeds.sort(key=lambda feed: feed.name)

    entries = provider.get_entries(feeds)
    entries.sort(key=lambda entry: entry.date, reverse=True)

    return render_template(
        'index.html', 
        feeds=feeds, 
        entries=entries, 
        get_time_str=get_time_str)


@app.teardown_appcontext
def close_db(error):
    db_utils.close_db(g)
