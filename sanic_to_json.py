from json import load
from examples.app import app

collection_json = {
    "info": {
        "name": "Test_collection",
        "description": "Generic text used for documentation.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "item": [],
}

atomic_request = {
    "name": "test request",
    "request": {
        "method": "GET",
        "header": [],
        "url": {"raw": "{{target_url}}endpoint", "host": ["{{target_url}}endpoint"]},
        "description": "This description can come from docs strings",
    },
    "response": [],
}


def basic_JSON(collection_name, app, api_json=collection_json):
    """Formats the Postman collection with 'collection_name' and doc string from Sanic app.
    
    Returns JSON dictionary."""

    api_json["info"]["name"] = collection_name
    api_json["info"]["description"] = app.__doc__
    return api_json


def transfer_postman_id(api_json, existing_file=None):
    """Transfer postman_id from existing JSON file."""
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
    name = route[0].split("/")[-1]
    return name


collection = basic_JSON("Testing", app)
collection = transfer_postman_id(collection)


# blueprints = get_blueprint_docs("database_1", app)
blueprints = find_blueprints(app)
print(blueprints)
routes = get_blueprint_routes("api_1", app)
# test = get_route_name(routes[0])
# test = routes[0][1][0].handlers["GET"].__doc__
print(routes[0][0].__dir__())
