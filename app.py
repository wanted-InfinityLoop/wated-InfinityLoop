from flask import Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate

from company.models import db
from config import DB_URL

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

db.init_app(app)
db.app = app
db.create_all()
migrate = Migrate(app, db)


@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)