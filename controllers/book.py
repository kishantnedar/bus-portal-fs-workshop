from flask import Blueprint, render_template, request, redirect, url_for
from actions.booking.booking import get_user_request_buses
import pandas as pd

booking = Blueprint('book', __name__)

@booking.route('/search', methods=['GET', 'POST'])
def search_bus():
    if request.method == 'POST':
        bus_list = get_user_request_buses(search=request.form)
        date = request.form['date']
        day = pd.Timestamp(date).day_name()
        return render_template('UserRequestbus.html', buses = bus_list, day = day)


@booking.route('/seat/<int:bus_no>')
def seat_book(bus_no):
    print(bus_no)
    return render_template('seat_booking.html')
