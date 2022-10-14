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


@booking.route('/seat/<int:bus_no>')
def seat_book(bus_no):
    bus_details = get_selected_bus(bus_no)
    # print(bus_details)
    seat_count = int(bus_details['bus_capacity'] / 4)
    print(bus_details['bus_seats']['window_left']
          ['seats'][1]['seat_occupied'])
    return render_template('seat_booking.html', bus=bus_details, seat_count=seat_count)


@booking.route('/confirm-booking', methods=['GET', 'POST'])
def confirm_booking():
    if request.method == 'POST':
        # print(request.form['bus_number'])
        user_id = 102
        bus_number = request.form['bus_id']
        window_left = request.form.getlist('window_left_seats')
        window_right = request.form.getlist('window_right_seats')
        left = request.form.getlist('left_seats')
        right = request.form.getlist('right_seats')
        record = {'user_id': user_id, 'bus_number': bus_number, 'window_left': window_left,
                  'window_right': window_right, 'left': left, 'right': right}
        book_ticket(record)

        return redirect(url_for('index'))
