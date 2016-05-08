from flask_restful import Resource
import db


class Restaurant(Resource):
    def get(self):
        restaurant = db.Restaurant.query.all()
        return restaurant

    def post(self, name, address, price, ratings, open_close):
        data = db.Restaurant(name, address, price, ratings, open_close)
        db.session.add(data)
        db.session.commit()
