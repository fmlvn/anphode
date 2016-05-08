from flask_restful import Resource
import db


class RestaurantAPI(Resource):
    def get(self):
        restaurant = db.Restaurant.query()
        # restaurant = {}
        # restaurant['name'] = 'Pho tron, pho Lan Ong'
        # restaurant['address'] = '65 Lan Ong, Hoan Kiem, Ha Noi'
        # restaurant['price'] = '20.000 - 55.000'
        # restaurant['ratings'] = '5'
        # restaurant['open_close'] = '5:00 - 22:00'
        return restaurant

    def post(self, name, address, price, ratings, open_close):
        data = db.Restaurant(name, address, price, ratings, open_close)
        db.session.add(data)
        db.session.commit()
