from sanic import Blueprint
from sanic.response import json, text

bp1 = Blueprint("api_1", url_prefix="/a-prefix", version="v1")
bp1.__doc__ = "This is the doc string for blueprint1."


@bp1.route("/endpoint-one", methods=["GET"])
async def post(request):
    """Return text from request.
       
    INI
    [header]
    Content-Type = application/json

    [body]
    username = {{username}}
    password = {{password}}
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
    """Return JSON from POST request.
    
    INI
    [header]
    {
        "key": "Content-Type",
        "value": "application/json",
        "type": "text"
    },
    {
        "key": "x-amz-sns-message-type",
        "value": "Notification",
        "type": "text"
    }
    """
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

    [example.one]
    name = "first example"
    headers = {} 
    body = {}
    params = {}

    [example.two]
    name = "asecond example"
    days = 1
    time = 60
    units = metric 

    """
    data = request.text
    return json(data)
