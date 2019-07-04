from app import app


atomic_endpoint = {
    "name": "test request",
    "request": {
        "method": "GET",
        "header": [],
        "url": {
            "raw": "{{target_url}}test-employees",
            "host": ["{{target_url}}test-employees"],
        },
        "description": "This description can come from docs strings",
    },
    "response": [],
}


def format_endpoint(route, postman_request=atomic_endpoint):
    """Populates basic_endpoint dictionary with route metatdata.
    Returns a formatted postman request item."""

    name = route[1]
    description = route[0].__doc__
    url = "{{target_url}}" + name[1:]
    postman_request["name"] = name
    postman_request["request"]["url"]["raw"] = url
    postman_request["request"]["url"]["host"] = [url]
    postman_request["request"]["description"] = description
    return postman_request

