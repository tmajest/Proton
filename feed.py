
class Feed(object):
    def __init__(self, name, feed_link, site_link):
        self.name = name
        self.feed_link = feed_link
        self.site_link = site_link

    @classmethod
    def create(cls, **kwargs):
        feed = cls(**kwargs)
        return feed

class FeedEntry(object):
    def __init__(self, feed, name, link, description, date):
        self.feed = feed
        self.name = name
        self.link = link
        self.description = description
        self.date = date
