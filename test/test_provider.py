import io
import pytest

from proton.provider import get_feeds, get_feed, get_entries

def test_get_feeds(app):
    """
    Tests that we can fetch all of the feeds from the test database.
    """
    with app.app_context():
        feeds = sorted(get_feeds(), key=lambda feed: feed.name)

    assert len(feeds) == 3

    assert feeds[0].name == 'testsite1'
    assert feeds[1].name == 'testsite2'
    assert feeds[2].name == 'testsite3'

    assert feeds[0].feed_link == 'testsite1-feedlink.com'
    assert feeds[1].feed_link == 'testsite2-feedlink.com'
    assert feeds[2].feed_link == 'testsite3-feedlink.com'

    assert feeds[0].site_link == 'testsite1-sitelink.com'
    assert feeds[1].site_link == 'testsite2-sitelink.com'
    assert feeds[2].site_link == 'testsite3-sitelink.com'

@pytest.mark.parametrize(['feedname', 'feedlink', 'sitelink'], [
    ('testsite1', 'testsite1-feedlink.com', 'testsite1-sitelink.com'),
    ('testsite2', 'testsite2-feedlink.com', 'testsite2-sitelink.com'),
    ('testsite3', 'testsite3-feedlink.com', 'testsite3-sitelink.com')])
def test_get_feed_by_name_success(app, feedname, feedlink, sitelink):
    """
    Test that we can get feeds by name.
    """
    with app.app_context():
        feed = get_feed(feedname)

    assert feed is not None
    assert feed.name == feedname
    assert feed.feed_link == feedlink
    assert feed.site_link == sitelink

@pytest.mark.parametrize('feedname', [None, '', 'invalid'])
def test_get_feed_by_name_failure(app, feedname):
    """
    Test that get_feed returns None with invalid site name.
    """
    with app.app_context():
        assert get_feed(feedname) == None


