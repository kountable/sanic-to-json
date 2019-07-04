from json import dump

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
        "url": {
            "raw": "{{target_url}}test-employees",
            "host": ["{{target_url}}test-employees"],
        },
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


def blueprint_items(app):
    """Converts each blueprint into a dictionary with a name, items =[], and description.

    These dictionaries become Postman folders.
    Returns a lists of dictionary items."""

    items = []
    blueprints = list(app.__dict__["blueprints"].keys())
    for blueprint in blueprints:
        postman_item = {}
        postman_item["name"] = blueprint
        postman_item["item"] = []
        postman_item["description"] = app.blueprints[blueprint].__doc__
        items.append(postman_item)
    return items


def populate_requests(items, app):
    """Populates the requests for each blueprint.
    
    Returns the items list with 'item' key popluated with requests."""

    for blueprint in items:
        for route in app.blueprints[blueprint["name"]].routes:
            blueprint["item"].append(format_endpoint(route).copy())
    return items


def format_endpoint(route, postman_request=atomic_request):
    """Populates atomic_request dictionary with route metatdata.
    Returns a postman formatted dictionary request item."""

    name = route[1]
    description = route[0].__doc__
    url = "{{target_url}}" + name[1:]
    postman_request["name"] = name
    postman_request["request"]["url"]["raw"] = url
    postman_request["request"]["url"]["host"] = [url]
    postman_request["request"]["description"] = description
    return postman_request


def generate_postman_json(collection_name, app, filename="postman_collection.json"):
    """Saves a JSON file to Postman schema specifications."""

    # instantiate new collection
    api_collection = postman_JSON(collection_name, app=app)

    # generate a list of items
    items = blueprint_items(app)

    # populate items with requests
    items = populate_requests(items, app)

    api_collection["item"] = items

    with open(filename, "w") as file:
        dump(api_collection, file, indent=4)
