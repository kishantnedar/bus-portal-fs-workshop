from flask import Flask, request, render_template, redirect, url_for,render_template,jsonify
import os

from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = os.urandom(24)

mysql = MySQL(app)

#Enter here your database informations 
app.config["MYSQL_HOST"] = ""
app.config["MYSQL_USER"] = ""
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = ""
app.config["MYSQL_CURSORCLASS"] = ""

@app.route("/")
def index():
    return render_template("base.html")
@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "select word_eng from words where word_eng LIKE '{}%' order by word_eng".format(searchbox)#This is just example query , you should replace field names with yours
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)





@app.route('/seat/book')
def seat_book():
    return render_template('seat_booking.html')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5007))
  app.run(debug = True, host = '0.0.0.0', port = port)