from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('seat_booking.html')

@app.route('/get/data')
def get_data():
    seat = [3, 6, 8]
    return render_template('seat_booking.html', seat = seat)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5007))
  app.run(debug = True, host = '0.0.0.0', port = port)