from flask import Flask, render_template, redirect, request, session, url_for
import os
from controllers.admin import admin
from controllers.book import booking
from actions.booking.booking import BookingActions
from controllers.bus import bus

from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.secret_key = os.urandom(24)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(booking)
app.register_blueprint(bus)


@app.route('/')
def index():
    if not session.get("user"):
        return redirect(url_for('login'))
    else:
        start_locations = []
        destination_locations = []
        location_obj = BookingActions().get_locations()
        for each_location in location_obj:
            if each_location['start'] not in start_locations:
                start_locations.append(each_location['start'])
            if each_location['destination'] not in destination_locations:
                destination_locations.append(each_location['destination'])
        return render_template("index.html", start_locations=start_locations, destination_locations=destination_locations, user=session.get("user"))


@app.route('/about')
def about_us():
    return render_template('about.html')



@app.route('/login',  methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["user"] = request.form.get("user-pno")
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["user"] = None
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5007))
    app.run(debug=True, host='0.0.0.0', port=port)
