from app import app


def test_index():
    response = app.test_client().get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'About' in response.data


def test_search_bus():
    client = app.test_client()
    with client.session_transaction() as session:
        session['user'] = 9999999999
    response = client.get(
        '/search', query_string={'from': 'Margao', 'to': 'Panaji', 'date': '2022-10-31'})
    assert response.status_code == 200
    assert b'No buses available' in response.data


def test_seat_book_page():
    client = app.test_client()
    with client.session_transaction() as session:
        session['user'] = 9999999999
        session['date'] = '2022-10-31'
    response = client.get('/book/52491b52b02b405ca7e94e7c58fb925c')
    assert response.status_code == 200
    assert b'NAMAV TRAVELS' in response.data
    assert b'2022-10-31' in response.data


def test_booking_list():
    client = app.test_client()
    with client.session_transaction() as session:
        session['user'] = 9999999999
    response = client.get('/bookings')
    assert response.status_code == 200
    assert b'Booking ID' in response.data
