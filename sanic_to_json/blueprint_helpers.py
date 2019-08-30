def get_blueprints(app):
    """Returns blueprints dict."""
    return app.blueprints


def get_blueprint_routes(blueprint, routes):
    """Return routes related to a given blueprint."""
    blueprint_routes = {}
    for route in routes:
        bp_name = routes[route].name.split(".")[0]
        # match route to blueprint
        if blueprint == bp_name:
            blueprint_routes[route] = routes[route]
    return blueprint_routes


def get_blueprint_docs(blueprints, blueprint):
    """Returns doc string for blueprint."""
    doc_string = blueprints[blueprint].__doc__
    return doc_string
