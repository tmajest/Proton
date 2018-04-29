from flask import request
from datetime import datetime
from dateutil import tz, parser

def parse_int_query(query_name):
    """
    Try to fetch and parse the query parameter as an int. 
    Return None if unsuccessful.
    """
    try:
        return int(request.args.get(query_name))
    except ValueError:
        return 0
    except TypeError:
        return 0


def get_time_str(date):
    """
    Gets a string that represents how long it has been.
    E.g. 1 hour ago, 3 months ago, etc. 
    """

    localized_now = datetime.now(tz.tzutc())

    seconds = int((localized_now - date).total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    months = days // 30
    years = months // 12

    # Get largest unit of time for the time string. If it is more than 1 year old, use
    # years. If it is less than one year but more than 1 month old, use months. Etc.
    time_str = ''
    if years > 0:
        unit = 'year' if years == 1 else 'years'
        return "{0} {1} ago".format(years, unit)
    elif months > 0:
        unit = 'month' if months == 1 else 'months'
        return "{0} {1} ago".format(months, unit)
    elif days > 0:
        unit = 'day' if days == 1 else 'days'
        return "{0} {1} ago".format(days, unit)
    elif hours > 0:
        unit = 'hour' if hours == 1 else 'hours'
        return "{0} {1} ago".format(hours, unit)
    else:
        unit = 'minute' if minutes == 1 else 'minutes'
        return "{0} {1} ago".format(minutes, unit)
