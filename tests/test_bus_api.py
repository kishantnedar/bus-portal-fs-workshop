from app import app


def test_get_bus():
    response = app.test_client().get('/bus/50201', follow_redirects=True)
    assert response.status_code == 200
    data = response.get_json()
    assert data['_id'] == 50201


def test_get_bus_not_found():
    response = app.test_client().get('/bus/50203', follow_redirects=True)
    assert response.status_code == 404
    data = response.get_json()
    assert data['message'] == 'No bus found'
