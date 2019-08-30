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
    body = {"username": "{{username}}", "password": "{{password}}"}

    [example.single]
    name = single query
    method = POST
    query = ?days=1&units=metric
    header = {"Content-Type": "application/json"}
    body = {"token": "POST token"}

    [example.multiple]
    name = multiple query
    method = POST
    query = ?days=3&units=metric&time=1400
    header = {"Content-Type": "application/json"}
    body = {"token": "token"}

    [example.another]
    name = another query
    method = POST
    query = ?days=1&units=metric
    header = {"Content-Type": "application/json"}
    body = {"token": "POST token"}
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


@bp1.route("/endpoint-three/<resource>/<subresource>", methods=["POST"])
async def post(request, resource, subresource):
    """Hello World.
    
    INI
    [request]
    header = {"Content-Type": "application/json"}
    body ={"token": "POST token"}

        
    [example.subpaths]
    name = adding paths
    method = POST
    header = {"Content-Type": "application/json"}
    body = {"username": "{{username}}", "password": "{{password}}"}
    """
    return json({resource: subresource})

