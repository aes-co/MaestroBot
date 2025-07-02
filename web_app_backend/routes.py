from flask import Blueprint

bp = Blueprint("routes", __name__)

@bp.route("/status")
def status():
    return {"status": "ok"}