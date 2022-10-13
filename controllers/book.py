from flask import Blueprint, render_template, request, redirect, url_for
from actions.booking.booking import get_user_request_buses
import pandas as pd

booking = Blueprint('book', __name__)

@booking.route('/search', methods=['GET', 'POST'])
def search_bus():
    if request.method == 'POST':
        bus_list = get_user_request_buses(search=request.form)
        for bus in bus_list:
            print(bus['bus_name'])
        return redirect(url_for('index'))


