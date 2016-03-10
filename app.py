from flask import Flask, redirect, request, render_template
from rooms import get_building

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/rooms")


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
        return render_template("rooms.html", quadrangle=quadrangle, number=number, building=building, floor=number//100)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
