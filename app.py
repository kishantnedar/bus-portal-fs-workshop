from flask import Flask, render_template
import os
from controllers.admin import admin
from controllers.book import booking

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(admin, url_prefix='/admin')

app.register_blueprint(booking, url_prefix='/book')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5007))
    app.run(debug=True, host='0.0.0.0', port=port)


