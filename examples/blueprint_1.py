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
    """Return JSON from POST request.
    
    [DEFAULT]
    ServerAliveInterval = 45
    Compression = yes
    CompressionLevel = 9
    ForwardX11 = yes
    home_dir = /kountable

    [bitbucket.org]
    User = hg, what does 
        do in a different line. 
    UPPER = test
    url = %(home_dir)s/endpoint

    [topsecret.server.com]
    Port = 50022
    ForwardX11 = no"""
    data = request.text
    return json(data)


@bp1.route("/endpoint-three", methods=["POST"])
async def post(request):
    """Hello World.
    And more text on the second line. 
    
    INI
    [header]
    Content-Type = application/json
    x-amz-sns-message-type = Notification

    [body]
    username = {{username}}
    password = {{password}}
    """
    data = request.text
    return json(data)
