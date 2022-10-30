import random
from app import app


def test_admin_index():
    response = app.test_client().get('/admin/')
    assert response.status_code == 200
    assert b'Welcome' in response.data


def test_add_bus():
    response = app.test_client().get('/admin/add-bus')
    assert response.status_code == 200
    assert b'Add Bus' in response.data


def test_add_bus_data():
    response = app.test_client().post('/admin/add-bus', data={
        'bus_number': random.randint(10000, 99999),
        'bus_name': 'NAMAV TRAVELS',
        'seat_columns': '10',
        'start_location': 'Vasco',
        'destination_location': 'Ponda',
        'bus_reg_number': 'GA09F1010',
        'normal_seat_price': '90',
        'window_seat_price': '100',
        'runs_on': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'NAMAV TRAVELS' in response.data


def test_remove_bus():
    app.test_client().post('/admin/add-bus', data={
        'bus_number': 50203,
        'bus_name': 'Bose Travels',
        'seat_columns': '10',
        'start_location': 'Vasco',
        'destination_location': 'Ponda',
        'bus_reg_number': 'GA09F1010',
        'normal_seat_price': '90',
        'window_seat_price': '100',
        'runs_on': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    }, follow_redirects=True)
    response = app.test_client().get(
        '/admin/remove-bus', query_string={'bus_id': 50203}, follow_redirects=True)
    assert response.status_code == 200
    assert b'50203' not in response.data


def test_schedule_page():
    response = app.test_client().get('admin/schedule-bus?bus_number=50202')
    assert response.status_code == 200
    assert b'Schedule Bus' in response.data
