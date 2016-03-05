from flask import Flask
from flask import request
from flask import render_template

from rooms import get_building

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/events")
def events():
    return render_template("index.html")


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
