from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/admin/')
def index():
    try:
        busses = get_busses()
        return render_template('admin_page.html')
    except TemplateNotFound:
        return render_template('404.html'), 404
