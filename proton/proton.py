from flask import render_template, g, Blueprint, abort
from .feed import Feed
from .utils import get_time_str
from .provider import get_feed, get_feeds, get_entries

bp = Blueprint('proton', __name__)

@bp.route('/')
def index():
    """
    Fetches the index page. The index page contains a side panel
    with links to the feed details page of each feed. It also contains
    a middle panel with a list of all of the lastest entries.
    """
    feeds = get_feeds()
    feeds.sort(key=lambda feed: feed.name)

    entries = get_entries(feeds)
    entries.sort(key=lambda entry: entry.date, reverse=True)

    return render_template(
        'index.html', 
        feeds=feeds, 
        entries=entries, 
        get_time_str=get_time_str)

@bp.route('/feed/<name>')
def feed_details(name):
    """
    Returns the feed details page. The feed details page lists all of the
    entries for a given feed.
    """
    feed = get_feed(name)
    if not feed:
        abort(404, "Feed {0} does not exist.".format(name))

    all_feeds = get_feeds()
    all_feeds.sort(key=lambda feed: feed.name)

    entries = get_entries([feed])
    entries.sort(key=lambda entry: entry.date, reverse=True)

    return render_template(
        'feed-details.html',
        feed=feed,
        feeds=all_feeds,
        entries=entries,
        get_time_str=get_time_str)

