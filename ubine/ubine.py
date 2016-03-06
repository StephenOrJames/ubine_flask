from datetime import datetime

from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sparkpost import SparkPost

from config import *
from rooms import get_building

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

sparky = SparkPost(SPARKPOST_API_KEY)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/events")
def events():
    events_list = __import__("events").Event.query.all()
    return render_template("events.html", events=events_list)


@app.route("/events/add", methods=["GET", "POST"])
def events_add():
    if request.method == "POST":
        time = datetime.strptime(request.form["time"], "%Y-%m-%dT%H:%M")
        event = __import__("events").Event(request.form["title"], request.form["description"], time)
        db.session.add(event)
        db.session.commit()
        sparky.transmissions.send(
            from_email=SPARKPOST_FROM_EMAIL,
            recipients=["stephenorjames@gmail.com"],
            subject="UBinE event: %s" % event.title,
            html="<html><body><p>%s</p><p>%s</p></body></html>" % (event.time, event.description)
        )
        return redirect("/events")
    return render_template("events_add.html")


@app.route("/events/subscribe", methods=["GET", "POST"])
def events_subscribe():
    if request.method == "POST" and not request.form["bad-bot"]:
        # Get current recipients
        recipients = sparky.recipient_lists.get(SPARKPOST_RECIPIENT_LIST_ID, show_recipients=True)["recipients"]
        # print(recipients)

        # Add new recipient
        recipients.append({"address": {"email": request.form["email"]}})
        # print(recipients)
        sparky.recipient_lists.update(SPARKPOST_RECIPIENT_LIST_ID, recipients=recipients)

        # Add email address
        return render_template("events_subscribe.html", success=True)
    return render_template("events_subscribe.html")


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


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
