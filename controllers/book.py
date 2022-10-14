from flask import Blueprint, render_template, request, redirect, url_for, jsonify

booking = Blueprint('booking', __name__, template_folder='templates')


@booking.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form
        return redirect(url_for('search', start=search['from'], destination=search['to'], date=search['date']))
    return render_template('search.html')


@booking.route('/search/results', methods=['GET', 'POST'])
def search_results(search):
    return render_template('search_results.html', search=search)
