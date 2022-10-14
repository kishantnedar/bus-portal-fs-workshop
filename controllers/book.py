from flask import Blueprint, render_template, request, redirect, url_for
from actions.booking.booking import get_user_request_buses, get_selected_bus
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
    bus_details = get_selected_bus(bus_no)
    seat_count = int(bus_details[0]['bus_capacity'] / 4)
    print(bus_details[0]['bus_seats']['window_left']['seats'][1]['seat_occupied'])
    return render_template('seat_booking.html', bus = bus_details[0], seat_count = seat_count)


@booking.route('/booked/<int:bus_no>',methods=['GET', 'POST'])
def booked(bus_no):
    if request.method == 'POST':

        bus_details = get_selected_bus(bus_no)
        return render_template('booking_done.html',bus = bus_details[0])

@booking.route('/booked', methods=['GET', 'POST'])
def return_to_homepage():
    if request.method == 'POST':
        return render_template('index.html')
    