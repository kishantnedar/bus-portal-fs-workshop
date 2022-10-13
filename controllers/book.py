from flask import Blueprint, render_template, request, redirect, url_for
from actions.booking.booking import get_user_request_buses

booking = Blueprint('book', __name__)

@booking.route('/search', methods=['GET', 'POST'])
def seat_book():
    if request.method == 'POST':
        bus_list = get_user_request_buses(search=request.form)
        return render_template('display_buses.html', buses = bus_list)


