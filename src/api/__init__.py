from flask import Flask

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    """Return a hello world message."""
    return {"message": "Hello, World!"}, 200
