from app import app
from controllers.book import booking


def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'About' in response.data


def search_bus(start_location, destination_location, day):
    return app.test_client().post('/search', data=dict(start_location=start_location, destination_location=destination_location, day=day), follow_redirects=True)

def test_search_bus():
    response = search_bus('Vasco', 'Panaji', 'Tuesday')
    assert response.status_code == 200
    # assert b'bus' in response.data
