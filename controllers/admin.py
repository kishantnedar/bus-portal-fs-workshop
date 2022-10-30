from flask import Blueprint, render_template, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from actions.admin.bus import AdminActions
from actions.bus.bus import BusActions
from actions.booking.booking import BookingActions
from pymongo.errors import DuplicateKeyError
from util.date_utils import get_day_name

admin = Blueprint('admin', __name__)


@admin.route('/', methods=['GET'])
def index():
    try:
        return render_template('admin/index.html', buses=AdminActions().get_busses())
    except TemplateNotFound:
        return render_template('404.html'), 404


@admin.route('/add-bus', methods=['GET', 'POST'])
def add_bus():
    if request.method == 'POST':
        try:
            _bus = {'bus_number': request.form['bus_number'],
                    'bus_name': request.form['bus_name'],
                    'start_location': request.form['start_location'],
                    'destination_location': request.form['destination_location'],
                    'bus_reg_number': request.form['bus_reg_number'],
                    'normal_seat_price': request.form['normal_seat_price'],
                    'window_seat_price': request.form['window_seat_price'],
                    'runs_on': request.form.getlist('runs_on'),
                    'seat_columns': request.form['seat_columns']}
            AdminActions().add_bus(bus=_bus)
        except DuplicateKeyError as e:
            flash('Bus already exists', 'alert-danger')
            return redirect(url_for('admin.add_bus'))
        flash('Bus added successfully', 'alert-success')
        return redirect(url_for('admin.index'))
    return render_template('admin/add-bus.html')


@admin.route('/view-bus', methods=['GET'])
def view_bus():
    bus_id = int(request.args.get('bus_id'))
    if bus_id:
        bus_details = BusActions().get_bus(bus_id)
        _bus_schedules = BusActions().get_bus_schedules(bus_id)
        return render_template('admin/view-bus.html', bus=bus_details, bus_schedules=_bus_schedules)
    return redirect(url_for('admin.index'))


@admin.route('/view-scheduled-bus', methods=['GET', 'POST'])
def view_scheduled_bus():
    schedule_id = request.args.get('schedule_id')
    schedule = BusActions().get_bus_schedule(schedule_id)
    return render_template('admin/view-scheduled-bus.html', bus=schedule)


@admin.route('/remove-bus', methods=['GET'])
def remove_bus():
    bus_id = int(request.args.get('bus_id'))
    if bus_id:
        if BusActions().get_bus_schedules(int(bus_id)) is None:
            AdminActions().delete_bus(int(bus_id))
            flash('Bus removed', 'alert-success')
        else:
            flash('Unable to delete bus since it has bookings', 'alert-danger')
    return redirect(url_for('admin.index'))


@admin.route('/schedule-bus', methods=['GET', 'POST'])
def schedule_bus():
    if request.method == 'POST':
        schedule = request.form
        bus = BusActions().get_bus(int(schedule['bus_number']))
        if get_day_name(schedule['date']) not in bus['runs_on']:
            flash('Bus does not run on this day', 'alert-danger')
            return redirect(url_for('admin.schedule_bus'), bus=BusActions().get_bus(schedule['bus_id']))
        AdminActions().schedule_bus(schedule=request.form)
        flash('Bus scheduled', 'alert-success')
        return redirect(url_for('admin.index'))
    bus_number = int(request.args.get('bus_number'))
    if bus_number:
        return render_template('admin/schedule-bus.html', bus=BusActions().get_bus(bus_number))
    else:
        flash('Bus not found', 'alert-danger')
        return redirect(url_for('admin.index'))


@admin.route('/cancel-schedule', methods=['GET'])
def cancel_schedule():
    schedule_id = request.args.get('schedule_id')
    bus_number = request.args.get('bus_id')
    schedule_bookings = BookingActions().get_bookings_by_schedule(schedule_id)
    if schedule_bookings == None:
        BusActions().cancel_schedule(schedule_id)
        flash('Schedule cancelled', 'alert-success')
        return redirect(url_for('admin.view_bus', bus_id=bus_number))
    else:
        flash('Schedule contains bookings', 'alert-danger')
        return redirect(url_for('admin.view_bus', bus_id=bus_number))


@admin.route('/get-bus-details', methods=['GET'])
def get_bus_details():
    bus_id = int(request.args.get('bus_id'))
    if bus_id:
        return BusActions().get_bus(bus_num=bus_id)
    flash('Bus not found', 'alert-danger')
    return redirect(url_for('admin.index'))
