from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from rooms import get_building

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/ubine"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/events")
def events():
    events = __import__("events").Event.query.all()
    return render_template("events.html", events=events)


@app.route("/rooms")
def rooms():
    quadrangle = request.args.get("quadrangle")
    number = request.args.get("number")
    try:
        number = int(number)
    except (TypeError, ValueError):
        return render_template("rooms.html")
    else:
        building = get_building(quadrangle, number)
        return render_template("rooms.html", quadrangle=quadrangle, number=number, building=building)

if __name__ == "__main__":
    app.run(debug=True)
