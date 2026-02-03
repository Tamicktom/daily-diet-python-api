# Libraries imports
from flask import Blueprint, request, jsonify

# Local imports

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.get("/")
def get_users():
    print("get_users")
    return jsonify({"message": "Hello, World!"}), 200


@user_blueprint.post("/")
def create_user():
    print("create_user")
    return jsonify({"message": "Hello, World!"}), 200


@user_blueprint.put("/<int:user_id>")
def update_user(user_id: int):
    print("update_user")
    return jsonify({"message": "Hello, World!"}), 200


@user_blueprint.delete("/<int:user_id>")
def delete_user(user_id: int):
    print("delete_user")
    return jsonify({"message": "Hello, World!"}), 200
