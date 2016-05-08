from flask_restful import Resource
import db


class RestaurantAPI(Resource):
    def get(self):
        restaurant = db.Restaurant.query()
        return restaurant

    def post(self, name, address, price, ratings, open_close):
        data = db.Restaurant(name, address, price, ratings, open_close)
        db.session.add(data)
        db.session.commit()
