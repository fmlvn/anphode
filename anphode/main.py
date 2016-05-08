from flask import Flask
from flask_restful import Api

import api
import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

api_ = Api(app)


@app.route("/")
def hello():
    return "Hello World!"


api_.add_resource(api.RestaurantAPI, '/cuahang/')
db.db.init_app(app)

if __name__ == "__main__":
    app.run()
