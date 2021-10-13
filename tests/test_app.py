# unit tests for app.py

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
    THEN check for '<p> elements' in the returned data: this indicates that the template has been filled with data from the db
    """
    res = client.get('/')
    assert b'<p>Title' in res.data
    assert b'<p>Cover' in res.data
    assert b'<p>Blurb' in res.data
    assert b'<p>Upvotes' in res.data
    assert b'<p>Affiliate' in res.data
    assert b'<p>Author' in res.data
    assert b'<p>Genre' in res.data


def test_get_books(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /get_books
    THEN check for status code 200
    """
    res = client.get('/get_books')
    assert res.status_code == 200


def test_get_books_content(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /get_books
    THEN check for '<p> elements' in the returned data: this indicates that the template has been filled with data from the db
    """
    res = client.get('/get_books')
    assert b'<p>Title' in res.data
    assert b'<p>Cover' in res.data
    assert b'<p>Blurb' in res.data
    assert b'<p>Upvotes' in res.data
    assert b'<p>Affiliate' in res.data
    assert b'<p>Author' in res.data
    assert b'<p>Genre' in res.data


def test_register(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /register
    THEN check for status code 200
    """
    res = client.get('/register')
    assert res.status_code == 200


def test_register_card_title(app, client):
    """
    GIVEN a running Flask app
    WHEN the client browses to /register
    THEN check the h5 element with class "card-title" and text "Register Your Account"
    """
    res = client.get('/register')
    assert b'<h5 class="card-title">Register Your Account' in res.data