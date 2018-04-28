from flask import Flask, render_template, g, current_app, Blueprint
from .feed import Feed
from .utils import get_time_str
from .provider import get_feeds, get_entries

bp = Blueprint('proton', __name__)

@bp.route('/')
def index():
    """
    Fetches the index page. The index page contains a side panel
    with links to the feed details page of each feed. It also contains
    a middle panel with a list of all of the lastest entries.
    """
    feeds = get_feeds(current_app.config["DATABASE_FILE"])
    feeds.sort(key=lambda feed: feed.name)

    entries = get_entries(feeds)
    entries.sort(key=lambda entry: entry.date, reverse=True)

    return render_template(
        'index.html', 
        feeds=feeds, 
        entries=entries, 
        get_time_str=get_time_str)
