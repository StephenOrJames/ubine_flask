from ubine import db


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


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ubitname = db.Column(db.String(8), unique=True)
#     # password = db.Column
