from sanic import Blueprint
from sanic.response import json, text

bp2 = Blueprint("api_2", url_prefix="/another-prefix", version="v1")
bp2.__doc__ = "This is the doc string for blueprint 2."


@bp2.route("/endpoint-four", methods=["GET"])
async def post(request):
    """Return JSON form request."""
    data = request.text
    return json(data)
