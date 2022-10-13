from actions.admin.bus import add_bus


bus = {
    'bus_number': '123',
    'bus_name': 'Test',
    'seat_count': 10,
    'start_location': 'Test',
    'destination_location': 'Test',
    'bus_reg_number': 'Test',
    'normal_seat_price': 100,
    'window_seat_price': 200
}

add_bus(bus)
