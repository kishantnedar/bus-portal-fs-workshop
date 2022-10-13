from flask import Blueprint, render_template, request, redirect, url_for
from actions.booking.booking import

booking = Blueprint('book', __name__)


@booking.route('/seat', methods=['GET', 'POST'])
def seat_book():
    if request.method == 'POST':
        add_bus_action(bus=request.form)
        return redirect(url_for('index'))
    return render_template('admin/add-bus.html')
