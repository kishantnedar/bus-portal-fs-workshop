import pandas as pd
from actions.booking.booking import (book_ticket, get_selected_bus,
                                     get_user_request_buses)
from flask import Blueprint, redirect, render_template, request, url_for

booking = Blueprint('book', __name__)


@booking.route('/search', methods=['GET', 'POST'])
def search_bus():
    if request.method == 'POST':
        bus_list = get_user_request_buses(search=request.form)
        date = request.form['date']
        day = pd.Timestamp(date).day_name()
        return render_template('UserRequestbus.html', buses=bus_list, day=day)


@booking.route('/seat/<int:bus_no>', methods = ['GET', 'POST'])
def seat_book(bus_no):
    bus_details = get_selected_bus(bus_no)
    seat_count = int(bus_details[0]['bus_capacity'] / 4)        
    return render_template('seat_booking.html', bus = bus_details[0], seat_count = seat_count)
