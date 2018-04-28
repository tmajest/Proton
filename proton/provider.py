from flask import g
from dateutil import parser

from .feed import Feed, FeedEntry
from .db_utils import get_db

import feedparser

FEED_QUERY = 'select name, feedlink, sitelink from feed'

def get_feeds(path):
    """
    Get all feeds in the given database. Fetch each RSS/Atom feed and
    parse their entries.
    """
    db = get_db(path)
    cursor = db.execute(FEED_QUERY)
    rows = cursor.fetchall()
    feeds = []
    
    for row in rows:
        name = row['name']
        feedlink = row['feedlink']
        sitelink = ''
        if 'sitelink' in row.keys():
            sitelink = row['sitelink']
        feed = Feed(name, feedlink, sitelink)
        feeds.append(feed)

    return feeds

def get_entries(feeds):
    """
    Get and parse all entries for the given feed.
    """
    entries = []
    for feed in feeds:
        feed_xml = feedparser.parse(feed.feed_link)

        # Only parse feeds with correct status code, feed details, and at least one feed entry
        if feed_xml == None \
            or feed_xml.get('status', 404) != 200 \
            or not feed_xml.get('feed', None) \
            or feed_xml.get('entries', []) == []:
            continue

        # Get feed name and description. Fall back to feed name in database if it
        # is not present in the rss feed.
        feed_details = feed_xml.feed
        feed.name = feed_details.get('title', feed.name)
        feed.description = feed_details.get('subtitle', '')

        for entry_xml in feed_xml.entries:
            # Only parse feed entries with a title and link
            if not entry_xml.get('title', '') \
                or not entry_xml.get('link', ''):
                continue

            #pdb.set_trace()
            entry_name = entry_xml.title
            entry_link = entry_xml.link
            entry_description = entry_xml.get('summary', '')
            entry_date = parser.parse(entry_xml.get('published', ''))
            entry = FeedEntry(feed, entry_name, entry_link, entry_description, entry_date)
            entries.append(entry)

    return entries
