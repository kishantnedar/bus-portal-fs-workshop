from actions.booking.booking import BookingActions
from flask import Blueprint, session, render_template, request
import datetime

booking = Blueprint('book', __name__)


@booking.route('/search', methods=['GET', 'POST'])
def search_bus():
    if request.method == 'POST':
        bus_list = BookingActions().get_user_request_buses(search=request.form)
        date = request.form['date']
        session['date'] = date
        day_name = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = day_name[datetime.datetime.strptime(date, '%Y-%m-%d').weekday()]
        return render_template('UserRequestbus.html', buses=bus_list, day=day)


@booking.route('/bus/<int:bus_no>')
def seat_book(bus_no):
    bus_details = BookingActions().get_selected_bus(bus_no)
    seat_count = int(bus_details['bus_capacity'] / 4)
    return render_template('seat_booking.html', bus=bus_details, seat_count=seat_count, book_date=session['date'])


@booking.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    if request.method == 'POST':
        user_id = 102
        bus_number = int(request.form['bus_id'])
        window_left = request.form.getlist('window_left_seats')
        window_right = request.form.getlist('window_right_seats')
        left = request.form.getlist('left_seats')
        right = request.form.getlist('right_seats')
        price = request.form['price']
        book_date = session['date']
        record = {'user_id': user_id, 'bus_number': bus_number, 'window_left': window_left,
                  'window_right': window_right, 'left': left, 'right': right, 'booked_date': book_date, 'booking_price': price}
        booking = BookingActions().book_ticket(record)
        session.pop('book_date', None)
        bus_details = BookingActions().get_selected_bus(bus_number)
        return render_template('booking_done.html', bus=bus_details, booking=booking)


@ booking.route('/bookings/<int:user_id>')
def booking_list(user_id):
    return render_template('BookingsList.html', bookinglist=BookingActions().get_bookings(user_id))
