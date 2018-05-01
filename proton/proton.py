from flask import abort, Blueprint, g, render_template, request, url_for
from .feed import Feed
from .utils import parse_int_query, get_time_str
from .provider import get_feed, get_feeds, get_entries

import itertools

bp = Blueprint('proton', __name__)

TAKE = 20

def get_skip():
    """
    Get skip query parameter. Only allow skip pagination in multiples of 20.
    """
    skip = parse_int_query('skip') or 0
    skip = 0 if skip < 0 else skip
    return skip - (skip % TAKE)

@bp.route('/')
def index():
    """
    Fetches the index page. The index page contains a side panel
    with links to the feed details page of each feed. It also contains
    a middle panel with a list of all of the lastest entries.
    """
    feeds = get_feeds()
    feeds.sort(key=lambda feed: feed.name)

    skip = get_skip()
    entries = get_entries(feeds)
    entries.sort(key=lambda entry: entry.date, reverse=True)
    paged_entries = entries[skip : skip + TAKE]

    prev_url, next_url = '', ''
    if skip > 0:
        prev_url = url_for('proton.index', skip = skip - TAKE)
    if skip + TAKE < len(entries):
        next_url = url_for('proton.index', skip = skip + TAKE)

    return render_template(
        'index.html', 
        feeds=feeds, 
        entries=paged_entries,
        prev_url=prev_url,
        next_url=next_url,
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

    skip = get_skip()
    entries = get_entries([feed])
    entries.sort(key=lambda entry: entry.date, reverse=True)
    paged_entries = entries[skip : skip + TAKE]

    prev_url, next_url = '', ''
    if skip > 0:
        prev_url = url_for(
            'proton.feed_details', 
            skip = skip - TAKE,
            name=name)
    if skip + TAKE < len(entries):
        next_url = url_for(
            'proton.feed_details', 
            skip = skip + TAKE,
            name=name)

    return render_template(
        'feed-details.html',
        feed=feed,
        feeds=all_feeds,
        entries=paged_entries,
        prev_url=prev_url,
        next_url=next_url,
        get_time_str=get_time_str)

