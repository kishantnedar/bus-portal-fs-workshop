from actions.booking.booking import BookingActions
from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from actions.bus.bus import BusActions
from util.date_utils import get_day_name

booking = Blueprint('book', __name__)


@booking.route('/search', methods=['GET'])
def search_bus():
    if not session.get("user"):
        return redirect(url_for('login'))
    else:
        if request.method == 'GET':
            start = request.args.get('from')
            destination = request.args.get('to')
            date = request.args.get('date')
            session['date'] = date
            day = get_day_name(session['date'])
            bus_list = BookingActions().get_user_request_buses(
                search={'from': start, 'to': destination, 'date': date})
            return render_template('user-request-buses.html', buses=bus_list, day=day)


@booking.route('/book/<schedule_id>')
def seat_book(schedule_id):
    if not session.get("user"):
        return redirect(url_for('login'))
    else:
        _schedule = BusActions().get_bus_schedule(schedule_id)
        _bus = BusActions().get_bus(_schedule['bus_number'])
        return render_template('seat-booking.html', schedule=_schedule, bus=_bus, book_date=session['date'])


@booking.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    if not session.get("user"):
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            user_id = session['user']
            bus_number = int(request.form['bus_id'])
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
            return render_template('booking-done.html', bus=BusActions().get_bus(bus_number), booking=booking)


@booking.route('/bookings')
def booking_list():
    if not session.get("user"):
        return redirect(url_for('login'))
    bookings = BookingActions().get_bookings(session['user'])
    return render_template('bookings-list.html', bookinglist=bookings)


@booking.route('/cancel')
def cancel_booking():
    if not session.get("user"):
        return redirect(url_for('login'))
    else:
        _user_id = session['user']
        _booking_id = request.args.get('booking_id')
        if _booking_id:
            BookingActions().booking_cancellation(booking_id=_booking_id, booked_by=_user_id)
            flash('Booking cancelled successfully', 'alert-danger')
            return redirect(url_for('book.booking_list', user_id=_user_id))
