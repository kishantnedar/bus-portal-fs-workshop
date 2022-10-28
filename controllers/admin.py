from flask import Blueprint, render_template, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from actions.admin.bus import AdminActions
from actions.booking.booking import BookingActions
from actions.bus.bus import BusActions
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
            AdminActions().add_bus(bus=request.form)
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


@admin.route('/remove-bus', methods=['GET'])
def remove_bus():
    bus_id = int(request.args.get('bus_id'))
    if bus_id:
        try:
            bus_schedules = BusActions().get_bus_schedules(bus_id)
            print(f"Bus contains bookings {len(bus_schedules)}")
            flash('Unable to delete bus since it has bookings', 'alert-danger')
        except ValueError:
            AdminActions().delete_bus(bus_id)
            print('Bus removed')
            flash('Bus removed', 'alert-success')
    return redirect(url_for('admin.index'))


@admin.route('/schedule-bus', methods=['GET', 'POST'])
def schedule_bus():
    if request.method == 'POST':
        schedule = request.form
        print(schedule)
        bus = BusActions().get_bus(int(schedule['bus_number']))
        if get_day_name(schedule['date']) not in bus['bus_runs_on']:
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


@admin.route('/get-bus-details', methods=['GET'])
def get_bus_details():
    bus_id = int(request.args.get('bus_id'))
    if bus_id:
        return BusActions().get_bus(bus_num=bus_id)
    flash('Bus not found', 'alert-danger')
    return redirect(url_for('admin.index'))
