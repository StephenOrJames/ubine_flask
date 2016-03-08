from datetime import datetime
from app import db


TIME_FORMAT = "%Y-%m-%dT%H:%M"


def time_str_to_obj(string):
    return datetime.strptime(string, TIME_FORMAT)


def time_obj_to_str(obj):
    return datetime.strftime(obj, TIME_FORMAT)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    time = db.Column(db.DateTime)

    def __init__(self, title, description, time):
        self.title = title
        self.description = description
        self.time = time

    def __repr__(self):
        return "<Event %d: %s>" % (self.id, self.title)
