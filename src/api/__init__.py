from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://mysql:mysql@localhost:3306/mysql"
)


@app.route("/hello", methods=["GET"])
def hello():
    """Return a hello world message."""
    return {"message": "Hello, World!"}, 200


if __name__ == "__main__":
    app.run(debug=True)
