from actions.booking.booking import BookingActions
from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from actions.bus.bus import BusActions
from util.date_utils import get_day_name

booking = Blueprint('book', __name__)


@booking.route('/search', methods=['GET', 'POST'])
def search_bus():
    if request.method == 'POST':
        date = request.form['date']
        session['date'] = date
        print(session['date'])
        day = get_day_name(session['date'])
        print(day)
        bus_list = BookingActions().get_user_request_buses(search=request.form)
        return render_template('user-request-buses.html', buses=bus_list, day=day)


@booking.route('/book/<schedule_id>')
def seat_book(schedule_id):
    schedule = BookingActions().get_selected_schedule(schedule_id)
    return render_template('seat_booking.html', bus=schedule, book_date=session['date'])


@booking.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    if request.method == 'POST':
        user_id = 102
        bus_number = request.form['bus_id']
        schedule_id = request.form['schedule_id']
        window_left = request.form.getlist('window_left_seats')
        window_right = request.form.getlist('window_right_seats')
        left = request.form.getlist('left_seats')
        right = request.form.getlist('right_seats')
        price = request.form['price']
        book_date = session['date']
        record = {'user_id': user_id, 'bus_number': bus_number, 'schedule_id': schedule_id, 'window_left': window_left,
                  'window_right': window_right, 'left': left, 'right': right, 'booked_date': book_date, 'booking_price': price}
        booking = BookingActions().book_ticket(record)
        session.pop('book_date', None)
        bus_details = BusActions().get_bus(bus_number)
        return render_template('booking_done.html', bus=bus_details, booking=booking)


@booking.route('/bookings/<int:user_id>')
def booking_list(user_id):
    return render_template('BookingsList.html', bookinglist=BookingActions().get_bookings(user_id))


@booking.route('/cancel')
def cancel_booking():
    _user_id = 102
    booking_id = request.args.get('booking_id')
    if booking_id:
        cancelled_booking = BookingActions().booking_cancellation(
            booking_id=booking_id, booked_by=_user_id)
        print(cancelled_booking)
        flash('Booking cancelled successfully', 'alert-danger')
        return redirect(url_for('book.booking_list', user_id=_user_id))
    return redirect(url_for('book.booking_list', user_id=_user_id))
