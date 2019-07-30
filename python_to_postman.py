from json import dump, load

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


def postman_JSON(collection_name, app, api_json=collection_json):
    """Formats the Postman collection with 'collection_name' and doc string from Sanic app.
    
    Returns JSON dictionary."""

    api_json["info"]["name"] = collection_name
    api_json["info"]["description"] = app.__doc__
    return api_json


def blueprint_items(api_json, app):
    """Converts each blueprint into a dictionary with a name, item =[], and description.

    These dictionaries become Postman folders. The "item" dict will contain the endpoins
    for each blueprint.

    Returns a list of dictionary items."""

    blueprints = list(app.__dict__["blueprints"].keys())
    for blueprint in blueprints:
        postman_folder = {}
        postman_folder["name"] = blueprint
        postman_folder["item"] = []
        postman_folder["description"] = app.blueprints[blueprint].__doc__
        api_json["item"].append(postman_folder)
    return api_json


def populate_blueprint_requests(api_json, app):
    """Populates the requests for each blueprint.
    
    Returns the items list with 'item' key popluated with requests."""
    for blueprint_dict in api_json["item"]:
        for route in app.blueprints[blueprint_dict["name"]].routes:
            blueprint_dict["item"].append(format_endpoint(route))
    return api_json


def format_endpoint(route, postman_request=atomic_request.copy()):
    """Populates atomic_request dictionary with route metatdata.

    Assumes route is a list of route items, e.g, function, url, methods

    Returns a postman formatted dictionary request item."""

    name = route[1]
    description = route[0].__doc__
    url = "{{target_url}}" + name[1:]
    postman_request = {}
    postman_request["name"] = name
    postman_request["request"] = {}
    postman_request["request"]["url"] = {}
    postman_request["request"]["url"]["raw"] = url
    postman_request["request"]["url"]["host"] = [url]
    postman_request["request"]["description"] = description
    return postman_request


def transfer_postman_id(api_json, existing_file=None):
    """Transfer postman_id from existing JSON file."""
    try:
        with open(existing_file, "r") as file:
            data = load(file)
            api_json["info"]["_postman_id"] = data["info"]["_postman_id"]
    except TypeError:
        pass

    return api_json


def generate_postman_json(
    collection_name, app, filename="postman_collection.json", existing_file=None
):
    """Write a JSON file to Postman schema specifications."""

    # new json dictionary
    api_collection = postman_JSON(collection_name, app=app)

    # transfer old postman id
    api_collection = transfer_postman_id(api_collection, existing_file=None)

    # generate a list of items
    api_collection = blueprint_items(api_collection, app)

    # poulate blueprints with endpoints
    api_collection = populate_blueprint_requests(api_collection, app)

    with open(filename, "w") as file:
        dump(api_collection, file, indent=4)
