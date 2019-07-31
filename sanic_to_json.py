from json import load

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


def transfer_postman_id(api_json, existing_file=None):
    """Transfer postman_id from existing JSON file."""
    try:
        with open(existing_file, "r") as file:
            data = load(file)
            api_json["info"]["_postman_id"] = data["info"]["_postman_id"]
    except TypeError:
        pass

    return api_json


def basic_JSON(collection_name, app, api_json=collection_json):
    """Returns skeleton JSON for Postman collection file.
    
    Collects 'collection_name' from argument and doc string from Sanic app.
    Returns JSON dictionary."""

    api_json["info"]["name"] = collection_name
    api_json["info"]["description"] = app.__doc__
    return api_json
