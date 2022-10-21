from actions.admin.bus import AdminActions


class TestActions:
    def test_add_bus(self):
        admin_actions = AdminActions()
        bus = {
            'bus_number': 'KBS-1234',
            'bus_name': 'KBS',
            'seat_count': '10',
            'start_location': 'Kathmandu',
            'destination_location': 'Pokhara',
            'bus_reg_number': 'KBS-1234',
            'normal_seat_price': '1000',
            'window_seat_price': '2000',
            'runs_on': ['Monday', 'Tuesday']
        }
        admin_actions.add_bus(bus)
        assert admin_actions.get_busses() == [bus]

    def test_get_busses(self):
        admin_actions = AdminActions()
        assert admin_actions.get_busses() == []

    def test_delete_bus(self):
        admin_actions = AdminActions()
        bus = {
            'bus_number': 'KBS-1234',
            'bus_name': 'KBS',
            'seat_count': '10',
            'start_location': 'Kathmandu',
            'destination_location': 'Pokhara',
            'bus_reg_number': 'KBS-1234',
            'normal_seat_price': '1000',
            'window_seat_price': '2000',
            'runs_on': ['Monday', 'Tuesday']
        }
        admin_actions.add_bus(bus)
        admin_actions.delete_bus('KBS-1234')
        assert admin_actions.get_busses() == []
