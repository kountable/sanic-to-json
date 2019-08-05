from json import load
from examples.app import app


def collection_json():
    """Returns JSON skeleton for Postman schema."""
    collection_json = {
        "info": {
            "name": "Test_collection",
            "description": "Generic text used for documentation.",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        },
        "item": [],
    }
    return collection_json


def atomic_request():
    """Returns an atomic Postman request dictionary."""

    request = {
        "name": "test request",
        "request": {
            "method": "GET",
            "header": [],
            "url": {
                "raw": "{{target_url}}endpoint",
                "host": ["{{target_url}}endpoint"],
            },
            "description": "This description can come from docs strings",
        },
        "response": [],
    }
    return request


def basic_JSON(collection_name, app, api_json=collection_json()):
    """Formats the Postman collection with 'collection_name' and doc string from Sanic app.

    Returns JSON dictionary."""
    api_json["info"]["name"] = collection_name
    api_json["info"]["description"] = app.__doc__
    return api_json


def transfer_postman_id(api_json, existing_file=None):
    """Transfer postman_id from existing JSON file.

    This is only needed if you want to keep the same url."""
    try:
        with open(existing_file, "r") as file:
            data = load(file)
            api_json["info"]["_postman_id"] = data["info"]["_postman_id"]
    except TypeError:
        pass

    return api_json


def find_blueprints(app):
    """Returns a list of blueprints."""
    blueprints = app.blueprints.keys()
    return list(blueprints)


def get_blueprint_docs(blueprint, app):
    """Returns doc string for blueprint."""
    doc_string = app.blueprints[blueprint].__doc__
    return doc_string


def get_blueprint_routes(blueprint, app):
    """Return a list of routes."""
    routes = app.blueprints[blueprint].routes
    return routes


def get_route_name(route):
    """Returns route name."""
    name = route[1]
    return name


def get_doc_string(route):
    """Return doc string for function in route."""
    return route[0].__doc__


def get_route_method(route):
    """Return route CRUD method."""
    return route[2][0]


def get_url_prefix(blueprint):
    prefix = app.blueprints[blueprint].version + app.blueprints[blueprint].url_prefix
    return prefix


def get_app_routes(app):
    """Return routes in main app."""
    routes = {}
    for route in app.router.routes_names:
        if "." not in route:
            routes[route] = app.router.routes_names[route]
    return routes


collection = basic_JSON("Testing", app)
collection = transfer_postman_id(collection)


# blueprints = get_blueprint_docs("database_1", app)
blueprints = find_blueprints(app)
for blueprint in blueprints:
    print(get_url_prefix(blueprint))
    routes = get_blueprint_routes(blueprint, app)
    for route in routes:
        print(get_route_name(route))
        print(get_route_method(route))
        print(get_doc_string(route))


# test = routes[0][1][0].handlers["GET"].__doc__

app_routes = get_app_routes(app)
for endpoint in app_routes:
    print(app_routes[endpoint][1][0].handlers)
    for method in app_routes[endpoint][1][0].handlers:
        print(app_routes[endpoint][1][0].handlers[method].__doc__)
