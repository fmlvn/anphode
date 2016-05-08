from flask import Flask
from flask_restful import Api

from resources.restaurant import RestaurantAPI
import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'

api_ = Api(app)


@app.route("/")
def hello():
    return "Hello World!"


api_.add_resource(RestaurantAPI, '/restaurant/')
db.db.init_app(app)

if __name__ == "__main__":
    app.run()
