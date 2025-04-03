# API Blueprint registration
from flask import Blueprint

example_blueprint = Blueprint("mario_api", __name__)

main_blueprint = Blueprint("mario_api", __name__)

from app.api import routes