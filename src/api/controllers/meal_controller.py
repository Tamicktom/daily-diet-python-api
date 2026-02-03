# Libraries imports
from flask import Blueprint, request, jsonify

# Local imports

meal_blueprint = Blueprint("meal", __name__, url_prefix="/meal")


@meal_blueprint.get("/")
def get_meals():
    print("get_meals")
    return jsonify({"message": "Hello, World!"}), 200


@meal_blueprint.post("/")
def create_meal():
    print("create_meal")
    return jsonify({"message": "Hello, World!"}), 200


@meal_blueprint.put("/<int:meal_id>")
def update_meal(meal_id: int):
    print("update_meal")
    return jsonify({"message": "Hello, World!"}), 200


@meal_blueprint.delete("/<int:meal_id>")
def delete_meal(meal_id: int):
    print("delete_meal")
    return jsonify({"message": "Hello, World!"}), 200
