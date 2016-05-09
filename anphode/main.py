from flask import Flask
from flask_restful import Api

from resources.restaurant import Restaurant
from db import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
    db.init_app(app)
    return app

app = create_app()
api = Api(app)
api.add_resource(Restaurant, '/restaurant/')


@app.route("/")
def listing():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
