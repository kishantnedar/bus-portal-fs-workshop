from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/seat/book')
def seat_book():
    return render_template('seat_booking.html', seat = [3, 6, 8])


@app.route('/admin/index')
def admin_index():
    return render_template('admin_page.html')

@app.route('/save/bus-deatils', methods = ['GET', 'POST'])
def save_bus_details():
    if request.method == 'POST':
        bus_name = request.form['bus_name']
        bus_no = request.form['bus_no']
        bus_reg_no = request.form['bus_reg_no']
        normal_seat_price = request.form['normal_seat_price']
        window_seat_price = request.form['window_seat_price']
        no_of_seats = request.form['no_of_seats']
        start_location = request.form['start_location']
        destination_location = request.form['destination_location']
    return redirect(url_for('admin_index'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5007))
    app.run(debug=True, host='0.0.0.0', port=port)
