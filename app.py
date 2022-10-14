from flask import Flask, render_template
import os
from controllers.admin import admin
from controllers.book import booking
from actions.booking.booking import get_locations

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(admin, url_prefix='/admin')

app.register_blueprint(booking, url_prefix='/book')

@app.route('/')
def index():
    start_locations = []
    destination_locations = []
    location_obj = get_locations()
    for each_location in location_obj:
        if each_location['bus_start'] not in start_locations:
            start_locations.append(each_location['bus_start'])
        if each_location['bus_destination'] not in destination_locations:
            destination_locations.append(each_location['bus_destination'])
    return render_template("index.html", start_locations = start_locations, destination_locations = destination_locations)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5007))
    app.run(debug=True, host='0.0.0.0', port=port)


