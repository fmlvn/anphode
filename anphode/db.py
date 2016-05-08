from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    price = db.Column(db.String())
    ratings = db.Column(db.String())
    open_close = db.Column(db.String())

    def __init__(self, id, name, address, price, ratings, open_close):
        self.id = id
        self.name = name
        self.address = address
        self.price = price
        self.ratings = ratings
        self.open_close = open_close

    def __repr__(self):
        restaurant = {}
        restaurant['id'] = self.id
        restaurant['name'] = self.name
        restaurant['address'] = self.address
        restaurant['price'] = self.price
        restaurant['ratings'] = self.ratings
        restaurant['open_close'] = self.open_close
        return str(restaurant)