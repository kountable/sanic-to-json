from sanic import Blueprint
from sanic.response import json, text

bp1 = Blueprint("api_1", url_prefix="/a-prefix", version="v1")
bp1.__doc__ = "This is the doc string for blueprint 1."


@bp1.route("/endpoint-one", methods=["GET"])
async def post(request):
    """Return text from request.
       
    INI
    [request]
    header = {"Content-Type": "application/json","x-amz-sns-message-type": "Notification"}
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


@bp1.route("/endpoint-three/<resource>", methods=["POST"])
async def post(request, resource):
    """resource endpoint with subresource.
    
    INI
    [request]
    header = {"Content-Type": "application/json"}
    body ={"token": "POST token"}
    """
    return json({resource})


@bp1.route("/endpoint-three/<resource>/<subresource>", methods=["POST"])
async def post(request, resource, subresource):
    """resource endpoint with subresource.
    
    INI
    [request]
    header = {"Content-Type": "application/json"}
    body ={"token": "POST token"}

    """
    return json({resource: subresource})

