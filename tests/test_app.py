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
    #expected = {'hello': 'world'}
    #assert expected == json.loads(res.get_data(as_text=True))
