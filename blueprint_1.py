from sanic import Blueprint
from sanic.response import json, text

bp1 = Blueprint("bp1", url_prefix="/a-prefix", version="v1")
bp1.__doc__ = "This is the doc string for blueprint1."


@bp1.route("/endpoint-one", methods=["GET"])
async def post(request):
    """Return text from request."""
    data = request.text
    return text(data)


@bp1.route("/endpoint-two", methods=["GET"])
async def post(request):
    """Return JSON form request."""
    data = request.text
    return json(data)
