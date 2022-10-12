from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
from actions.admin.bus import add_bus as add_bus_action

admin = Blueprint('admin', __name__)


@admin.route('/add-bus', methods=['GET', 'POST'])
def add_bus():
    if request.method == 'POST':
        add_bus_action(bus=request.form)
        return redirect(url_for('index'))
    return render_template('admin/add-bus.html')
