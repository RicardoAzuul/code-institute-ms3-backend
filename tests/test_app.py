# unit tests for app.py

#import json


def test_index(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /
    THEN check for status code 200
    """
    res = client.get('/')
    assert res.status_code == 200


def test_index_content(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /
    THEN check for 'Shining' in the returned data
    """
    res = client.get('/')
    assert b'<p>Title' in res.data
    assert b'<p>Cover' in res.data
    assert b'<p>Blurb' in res.data



def test_get_books(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /get_books
    THEN check for status code 200
    """
    res = client.get('/get_books')
    assert res.status_code == 200