from sanic import Blueprint
from sanic.response import json, text

bp1 = Blueprint("api_1", url_prefix="/a-prefix", version="v1")
bp1.__doc__ = "This is the doc string for blueprint1."


@bp1.route("/endpoint-one", methods=["GET"])
async def post(request):
    """Return text from request.
       
    JSON BODY
    --------
    { "token":"{{token}}" ,"project_id":"{{project_id}}" }
    """
    data = request.text
    return text(data)


@bp1.route("/endpoint-two", methods=["GET"])
async def post(request):
    """Return JSON from GET request."""
    data = request.text
    return json(data)


@bp1.route("/endpoint-two", methods=["POST"])
async def post(request):
    """Return JSON from POST request."""
    data = request.text
    return json(data)
