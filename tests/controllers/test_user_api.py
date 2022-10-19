from app import app

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'About' in response.data

def test_search_bus():
    response = app.test_client().post('/search', data={'from': 'Margao', 'to': 'Panaji', 'date': '2022-10-19'})
    assert response.status_code == 200
    assert b'GAC' in response.data

def test_seat_book():
    client = app.test_client()
    with client.session_transaction() as session:
        session['date'] = '2022-10-19'
    response = client.get('/bus/40021')
    assert response.status_code == 200
    assert b'GAC Travels' in response.data
    assert b'2022-10-19' in response.data

# def test_confirm_booking():
#     client = app.test_client()
#     with client.session_transaction() as session:
#         session['date'] = '2022-10-19'
#     response = client.post('/confirm-booking',
#     data={'bus_id': '40021', 'window_left_seats': ['1'], 'window_right_seats': [], 'left_seats': [], 'right_seats': [], 'price': '30'})
#     assert response.status_code == 200
#     assert b'A1' in response.data
#     assert b'30' in 

def test_booking_list():
    response = app.test_client().get('/bookings/102')
    assert response.status_code == 200
    assert b'Booking ID' in response.data
    assert b'A1' in response.data
