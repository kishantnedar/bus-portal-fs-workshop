from flask import Blueprint, render_template, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from actions.admin.bus import add_bus as add_bus_action, get_busses, delete_bus
from pymongo.errors import DuplicateKeyError

admin = Blueprint('admin', __name__)


@admin.route('/', methods=['GET'])
def index():
    try:
        return render_template('admin/index.html', buses=get_busses())
    except TemplateNotFound:
        return render_template('404.html'), 404


@admin.route('/add-bus', methods=['GET', 'POST'])
def add_bus():
    if request.method == 'POST':
        try:
            add_bus_action(bus=request.form)
        except DuplicateKeyError as e:
            flash('Bus already exists')
            return redirect(url_for('admin.add_bus'))
        return redirect(url_for('admin.index'))
    return render_template('admin/add-bus.html')


@admin.route('/remove-bus', methods=['GET'])
def remove_bus():
    bus_id = int(request.args.get('bus_id'))
    if bus_id:
        delete_bus(bus_id)
        print('bus removed')
        flash('Bus removed')
        return redirect(url_for('admin.index'))
    return redirect(url_for('admin.index'))
