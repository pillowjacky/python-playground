from .services import meowService
from flask import Blueprint

bp = Blueprint("cat", __name__, url_prefix="/cat")


@bp.route("/")
def index():
    return "Cat!"


@bp.route("/meow")
def meowRoute():
    return meowService()
