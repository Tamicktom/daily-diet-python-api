# Libraries imports
from flask import Flask

# Local imports
from api.env import config
from api.database import db
from api.controllers.meal_controller import meal_blueprint

app = Flask(__name__)

app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL

db.init_app(app)
app.register_blueprint(meal_blueprint)


@app.route("/hello", methods=["GET"])
def hello():
    """Return a hello world message."""
    return {"message": "Hello, World!"}, 200


if __name__ == "__main__":
    app.run(debug=True)
