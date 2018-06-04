from flaskr.app import db


class Contact(db.Model):

    __tablename__ = "contact"

    contact_id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return '<last_name {}>'.format(self.body)
