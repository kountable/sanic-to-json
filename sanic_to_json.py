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


def find_blueprints(app):
    """Returns a list of blueprints."""
    blueprints = app.blueprints.keys()
    return list(blueprints)


def get_blueprint_docs(blueprint, app):
    """Returns doc string for blueprint."""
    doc_string = app.blueprints[blueprint].__doc__
    return doc_string


def get_blueprint_routes(blueprints, app):
    """Return a list of routes."""
    routes = []
    for blueprint in blueprints:
        for route_name in app.router.routes_names:
            if blueprint in route_name:
                routes.append(app.router.routes_names[route_name])
    return routes


def get_route_name(route):
    """Returns route name."""


collection = basic_JSON("Testing", app)
collection = transfer_postman_id(collection)


# blueprints = get_blueprint_docs("database_1", app)
blueprints = find_blueprints(app)
routes = get_blueprint_routes(blueprints, app)
test = routes[1]
# test = routes[0][1][0].handlers["GET"].__doc__
print(test)
