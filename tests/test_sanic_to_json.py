import os
from sanic_to_json import (
    collection_json,
    atomic_request,
    basic_JSON,
    get_blueprints,
    get_blueprint_docs,
    get_blueprint_routes,
    get_blueprint_route_name,
)
from examples.app import app


def test_collection_json():
    """Assert the correct dicionary keys are present."""
    items = ["info", "item"]
    assert set(collection_json().keys()) == set(items)


def test_types():
    """Assert json templates are dicionaries."""
    json_templates = [collection_json(), atomic_request()]
    for template in json_templates:
        assert isinstance(template, dict)


def test_basic_JSON():
    """Checks 'collection_name' and doc string from Sanic app."""
    collection_name = "test_collection"
    test_json = basic_JSON(collection_name, app)

    assert test_json["info"]["name"] == collection_name
    assert test_json["info"]["description"] == app.__doc__


def test_get_blueprints():
    assert get_blueprints(app) == app.blueprints


# get example app blueprints
blueprints = get_blueprints(app)


def test_get_blueprint_docs():
    """Returns doc string for blueprint."""
    for blueprint in blueprints:
        assert (
            get_blueprint_docs(blueprints, blueprint) == blueprints[blueprint].__doc__
        )


def test_get_blueprint_routes():
    """Return a list of routes."""
    for blueprint in blueprints:
        assert (
            get_blueprint_routes(blueprints, blueprint) == blueprints[blueprint].routes
        )


def test_get_blueprint_route_name():
    """Returns route name."""
    for blueprint in blueprints:
        for route in get_blueprint_routes(blueprints, blueprint):
            get_blueprint_route_name(route) == route[1]


#
# def test_populte_requests():
#    """References endpoints in examples/blueprint_1 and examples/blueprint_2."""
#    api_collection = postman_JSON("Testing", app=app)
#    # generate a list of items
#    api_collection = blueprint_items(api_collection, app)
#    # poulate blueprints with endpoints
#    api_collection = populate_blueprint_requests(api_collection, app)
#
#    json_items = [
#        api_collection["item"][0]["item"][0]["name"],
#        api_collection["item"][0]["item"][1]["name"],
#        api_collection["item"][1]["item"][0]["name"],
#        api_collection["item"][1]["item"][1]["name"],
#        api_collection["item"][0]["item"][0]["request"]["description"],
#        api_collection["item"][0]["item"][1]["request"]["description"],
#        api_collection["item"][1]["item"][0]["request"]["description"],
#        api_collection["item"][1]["item"][1]["request"]["description"],
#    ]
#
#    blueprint_strings = [
#        "/endpoint-one",
#        "/endpoint-two",
#        "/endpoint-three",
#        "/endpoint-four",
#        "Return text from request.",
#        "Return JSON form request.",
#        "Return text from request.",
#        "Return JSON form request.",
#    ]
#
#    for dict_item, str_item in zip(json_items, blueprint_strings):
#        assert dict_item == str_item
#
#
# def test_format_endpoint():
#    """Tests the first endpoint in examples/blueprint for formatting."""
#    route = app.blueprints["bp1"].routes[0]
#    test = format_endpoint(route)
#
#    formatted_endpoint = {
#        "name": "/endpoint-one",
#        "request": {
#            "url": {
#                "raw": "{{target_url}}endpoint-one",
#                "host": ["{{target_url}}endpoint-one"],
#            },
#            "description": "Return text from request.",
#        },
#    }
#    assert test == formatted_endpoint
#
#
# def test_generate_postman_json():
#    """Test generation of json file. Deletes after test."""
#    filename = "Test_collection.json"
#    generate_postman_json("Testing", app, filename=filename)
#    assert os.path.exists(filename)
#    os.remove(filename)
#    assert not os.path.exists(filename)
#
#
# def test_transfer_postman_id():
#    """Transfer postman_id from existing JSON file."""
#
#    api_collection = postman_JSON("Testing", app=app)
#
#    api_collection = transfer_postman_id(api_collection, existing_file=None)
#    assert "_postman_id" not in api_collection["info"].keys()
#
#    api_collection = transfer_postman_id(
#        api_collection, existing_file="examples/test.json"
#    )
#    assert "_postman_id" in api_collection["info"].keys()
#