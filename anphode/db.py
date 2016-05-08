from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    price = db.Column(db.String())
    ratings = db.Column(db.String())
    open_close = db.Column(db.String())

    def __init__(self, name, address, price, ratings, open_close):
        self.name = name
        self.address = address
        self.price = price
        self.ratings = ratings
        self.open_close = open_close

    def __repr__(self):
        return self.name
