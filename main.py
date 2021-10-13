import datetime

from flask import Flask, render_template, request, redirect, url_for
from api.api import store_time, fetch_times, store_name_in_db, get_all_names

app = Flask(__name__)

@app.route("/")
def root():
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now())

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)

    return render_template('index.html', times=times)

@app.route("/names")
def names():
    names = get_all_names()
    return render_template('names.html', names=names)

@app.route("/names/<name>", methods=["POST", "GET"])
def store_name(name):
    store_name_in_db(name, datetime.datetime.now())
    return redirect(url_for('names'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)