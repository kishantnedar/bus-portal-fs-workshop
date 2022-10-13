from flask import Blueprint, render_template, request, redirect, url_for
from actions.booking.booking import get_user_request_buses

booking = Blueprint('book', __name__)

@booking.route('/search', methods=['GET', 'POST'])
def search_bus():
    if request.method == 'POST':
        bus_list = get_user_request_buses(search=request.form)
        for bus in bus_list:
            print(bus.keys())
        return redirect(url_for('index'))


@booking.route('/seat/<int:bus_no>')
def seat_book(bus_no):
    print(bus_no)
    return render_template('seat_booking.html')
