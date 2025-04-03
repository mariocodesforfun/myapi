
from flask import jsonify
from app.api import example_blueprint

@example_blueprint.route("/health", methods=["GET"])
def health():

    message = {"message": "API is running, let's start the implementation."}

    return jsonify(message), 200