from sanic import Blueprint
from sanic.response import json, text

bp2 = Blueprint("bp2", url_prefix="/another-prefix", version="v1")
bp2.__doc__ = "This is the doc string for blueprint2."


@bp2.route("/endpoint-one", methods=["GET"])
async def post(request):
    """Return text from request."""
    data = request.text
    return text(data)


@bp2.route("/endpoint-two", methods=["GET"])
async def post(request):
    """Return JSON form request."""
    data = request.text
    return json(data)
