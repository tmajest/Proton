from proton.utils import parse_int_query, get_time_str, get_datetime_now

import pytest

@pytest.mark.parametrize(
    ('query', 'expected'), (
        ('/?val=123', 123),
        ('/', 0),
        ('/?val=abc', 0)))
def test_parse_int_query(app, query, expected):
    """
    Test that we can correctly parse an int query parameter.
    """
    with app.test_request_context(query):
        val = parse_int_query('val')
        assert val == expected
