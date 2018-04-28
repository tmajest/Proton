
class Feed(object):
    """
    Represents an RSS or Atom feed. Contains links to the original site and for the
    RSS/Atom feed.
    """

    def __init__(self, name, feed_link, site_link):
        self.name = name
        self.feed_link = feed_link
        self.site_link = site_link

    @classmethod
    def create(cls, **kwargs):
        feed = cls(**kwargs)
        return feed

class FeedEntry(object):
    """
    Represents an entry/article originating from the RSS/Atom feed.
    """

    def __init__(self, feed, name, link, description, date):
        self.feed = feed
        self.name = name
        self.link = link
        self.description = description
        self.date = date
