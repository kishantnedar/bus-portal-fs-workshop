from flask import Flask, render_template
import os
from controllers.admin import admin
from controllers.book import booking
from actions.booking.booking import BookingActions
from controllers.bus import bus

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(booking)
app.register_blueprint(bus)


@app.route('/')
def index():
    start_locations = []
    destination_locations = []
    location_obj = BookingActions().get_locations()
    for each_location in location_obj:
        if each_location['start'] not in start_locations:
            start_locations.append(each_location['start'])
        if each_location['destination'] not in destination_locations:
            destination_locations.append(each_location['destination'])
    return render_template("index.html", start_locations=start_locations, destination_locations=destination_locations)


@app.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5007))
    app.run(debug=True, host='0.0.0.0', port=port)
