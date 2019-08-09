from json import dump


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
            "header": [
                {
                    "key": "Content-Type",
                    "name": "Content-Type",
                    "value": "application/json",
                    "type": "text",
                }
            ],
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


def get_all_routes(app):
    """Returns all routes from Sanic app.
    
    Exclue duplicates."""
    all_routes = app.router.routes_all
    routes = {}
    for route in all_routes:
        if route[-1] != "/":
            routes[route] = all_routes[route]
    return routes


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


def get_route_name(route):
    """Returns route name."""
    name = route.split("/")[-1]
    return name


def get_app_route_methods(routes, route):
    """Return route CRUD method (GET, POST, etc)."""
    methods = list(routes[route].methods)
    return methods


def get_route_doc_string(routes, route, method):
    """Returns doc string for embedded route functions."""
    try:
        doc = routes[route][0].handlers[method].__doc__
    except AttributeError:
        doc = routes[route][0].__doc__
    return doc


def get_url(route, base_url="{{base_Url}}"):
    """Adds base_url environment variable to url prefix."""
    url = base_url + route
    return url


def format_request(routes, route, method, base_url="{{base_Url}}"):
    """Populates atomic_request dictionary with route metatdata.

    Returns a postman formatted dictionary request item."""
    request = atomic_request()
    request["name"] = get_route_name(route)
    request["request"]["method"] = method
    request["request"]["url"]["raw"] = get_url(route, base_url=base_url)
    request["request"]["url"]["host"] = [request["request"]["url"]["raw"]]
    request["request"]["description"] = get_route_doc_string(routes, route, method)
    return request


# ______________________________________


# build the json from blueprints
def add_blueprint_folders(api_json, blueprints):
    """Converts each blueprint into a dictionary with a name, item =[], and description.

    These dictionaries become Postman folders. The "item" dict will contain the endpoins
    for each blueprint.

    Returns a list of dictionary items."""
    for blueprint in blueprints:
        postman_folder = {}
        postman_folder["name"] = blueprint
        postman_folder["item"] = []
        postman_folder["description"] = get_blueprint_docs(blueprints, blueprint)
        api_json["item"].append(postman_folder)
    return api_json


def populate_blueprints(api_json, blueprints):
    """Populates endpoints for each blueprint folder."""
    for blueprint in blueprints:
        items = []
        for route in get_blueprint_routes(blueprints, blueprint):
            items.append(format_blueprint_request(blueprints, blueprint, route))
        api_json["item"].append(
            {
                "name": blueprint,
                "description": get_blueprint_docs(blueprints, blueprint),
                "item": items,
            }
        )

    return api_json


def add_app_requests(api_json, app):
    """Add requests defined in main to api JSON dict."""
    routes = get_app_routes(app)
    for route in routes:
        methods = get_app_route_methods(routes, route)
        for method in methods:
            request = format_app_request(routes, route, method)
            api_json["item"].append(request)
    return api_json


# export JSON
def save_as_json(collection_name, filename="postman_collection.json"):
    """Write dict to JSON file."""

    with open(filename, "w") as file:
        dump(collection_name, file, indent=4)


def generate_json(
    collection_name, app, filename="postman_collection.json", existing_file=None
):
    """Generates json script from Sanic docs.

    Parameters
    ----------
    collection_name: str
        title of collection
    app: Sanic class
        Sanic app
    filename: str (optional)
        location of output file
    existing_file: str (optional)
        location of existing file, used to copy previous postman_id key
    """
    # build basic json schema
    collection = basic_JSON(collection_name, app)
    # populate blueprint requests
    collection = populate_blueprints(collection, app)
    # populate main app requests
    add_app_requests(collection, app)
    # save dict to JSON file
    save_as_json(collection)

