from flaskr.app import db


class Post(db.Model):

    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

    def __repr__(self):
        return '<title {}>'.format(self.body)
