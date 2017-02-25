from config import db

class DateMixin(db.Model):
    __abstract__ = True
    last_modified = db.Column(db.DateTime)

class Source(DateMixin):
    id = db.Column(db.Integer, primary_key = True)
    source = db.Column(db.String(50), unique = True)

    def __init__(self, source):
        self.source = source


class News(DateMixin):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    url = db.Column(db.String())
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    source = db.relationship('Source', backref=db.backref('source', lazy='dynamic'))
