from flask import Flask, request, render_template, redirect, url_for,render_template,jsonify
import os

from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "select word_eng from words where word_eng LIKE '{}%' order by word_eng".format(searchbox)#This is just example query , you should replace field names with yours
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)


@app.route('/book/seat', methods = ['GET', 'POST'])
def seat_book():
    return render_template('seat_booking.html', seat = [3, 6, 8])

# Admin Section
@app.route('/admin/index')
def admin_index():
    return render_template('admin_index.html')

@app.route('/admin/add/bus', methods = ['GET', 'POST'])
def add_bus():
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
    return render_template('admin_add_bus.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5007))
    app.run(debug=True, host='0.0.0.0', port=port)
