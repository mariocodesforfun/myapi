
from flask import jsonify
from app.api import example_blueprint, main_blueprint

@example_blueprint.route("/health", methods=["GET"])
def health():

    message = {"message": "API is running, let's start the implementation."}

    return jsonify(message), 200

@example_blueprint.route("/", methods=["GET"])
def main():

    message = {"message": "Nothing to show here, but we're getting there"}

    return jsonify(message), 200

