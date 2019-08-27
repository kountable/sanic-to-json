from sanic import Blueprint
from sanic.response import json, text

bp1 = Blueprint("api_1", url_prefix="/a-prefix", version="v1")
bp1.__doc__ = "This is the doc string for blueprint1."


@bp1.route("/endpoint-one", methods=["GET"])
async def post(request):
    """Return text from request.
       
    INI
    [header]
    header = {"Content-Typ e": "application/json","x-amz-sns-message-type": "Notification"}

    [example.one]
    name = "day query"
    method = "GET"
    query = ?days=1
    header = {"Content-Typ e": "application/json"}
    body = {"token": "1234"}
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


@bp1.route("/endpoint-three", methods=["POST"])
async def post(request):
    """Hello World.
    And more text on the second line. 
    
    INI
  
    [header]
    header = {"Content-Type": "application/json", "x-amz-sns-message-type": "Notification"}
    header2 = {"token":"{{token}}"}
    
    [body]
    body = {"username": "{{username}}", "password": "{{password}}"}
    more_body = {"token": "1234"}



    """
    data = request.text
    return json(data)

