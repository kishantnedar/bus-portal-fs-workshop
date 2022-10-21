from app import app

def test_admin_index():
    response = app.test_client().get('/admin/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_add_bus():
    response = app.test_client().get('/admin/add-bus')
    assert response.status_code == 200
    assert b'Add' in response.data

def test_add_bus_data():
    response = app.test_client().post('/admin/add-bus', data={
        'bus_number': 50201,
        'bus_name': 'NAMAV TRAVELS',
        'seat_count': '10',
        'start_location': 'Vasco',
        'destination_location': 'Ponda',
        'bus_reg_number': 'GA09F1010',
        'normal_seat_price': '90',
        'window_seat_price': '100',
        'runs_on': ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'NAMAV TRAVELS' in response.data

def test_remove_bus():
    response = app.test_client().get('/admin/remove-bus', query_string={'bus_id': 50201}, follow_redirects=True)
    assert response.status_code == 200
    assert b'NAMAV TRAVELS' not in response.data