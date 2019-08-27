import os
from sanic_to_json import (
    atomic_request,
    collection_json,
    basic_JSON,
    get_blueprints,
    get_blueprint_docs,
    get_all_routes,
    get_blueprint_routes,
    get_route_name,
    get_app_route_methods,
    get_route_doc_string,
    get_url,
    format_request,
    populate_blueprint,
    add_non_blueprint_requests,
    generate_sanic_json,
    format_json_body,
    extract_ini_from_doc,
    load_config,
    format_headers,
    format_json_body,
)
from examples.app import app
import configparser


def test_atomic_request():
    assert set(atomic_request().keys()) == set(["name", "request", "response"])


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


def test_get_all_routes():
    """Returns all routes from Sanic app, excludes duplicates."""
    assert get_all_routes(app).items() <= app.router.routes_all.items()


def test_get_blueprints():
    assert get_blueprints(app) == app.blueprints


def test_get_blueprints_type():
    assert isinstance(get_blueprints(app), dict)


# get example app blueprints
blueprints = get_blueprints(app)
routes = get_all_routes(app)


def test_get_blueprint_routes():
    """Return a list of routes."""
    for blueprint in blueprints:
        assert get_blueprint_routes(blueprint, routes).items() <= routes.items()


def test_get_blueprint_docs():
    """Returns doc string for blueprint."""
    for blueprint in blueprints:
        assert (
            get_blueprint_docs(blueprints, blueprint) == blueprints[blueprint].__doc__
        )


# INI functions
test_doc = app.router.routes_all["/v1/a-prefix/endpoint-three"].handler.__doc__


def test_extract_ini_from_doc():
    """Extracts INI from doc strings."""

    assert extract_ini_from_doc(test_doc) == test_doc.rsplit("INI")[-1]


def test_load_config():
    test_ini = extract_ini_from_doc(test_doc)
    test_config = load_config(test_ini)
    assert isinstance(test_config, configparser.RawConfigParser)


def test_format_headers():
    test_ini = extract_ini_from_doc(test_doc)
    test_config = load_config(test_ini)
    assert format_headers(test_config) == [
        {"key": "Content-Type", "value": "application/json", "type": "text"},
        {"key": "x-amz-sns-message-type", "value": "Notification", "type": "text"},
    ]


def test_format_json_body():
    test_ini = extract_ini_from_doc(test_doc)
    test_config = load_config(test_ini)
    test_body = format_json_body(test_config)
    assert test_body == {
        "mode": "raw",
        "raw": '{"username": "{{username}}", "password": "{{password}}"}',
    }


def test_get_route_name():
    """Returns route name."""
    for route in routes:
        assert get_route_name(route) == route.split("/")[-1]


def test_get_app_route_methods():
    """Return route CRUD method (GET, POST, etc)."""
    for route in routes:
        assert get_app_route_methods(routes, route) == list(routes[route].methods)


def test_get_route_doc_string():
    """Returns doc string for embedded route functions."""
    for route in routes:
        for method in get_app_route_methods(routes, route):
            doc = get_route_doc_string(routes, route, method)
            assert isinstance(doc, str)


def test_get_url():
    """Adds base_url environment variable to url prefix."""
    route = "test"
    assert get_url(route) == "{{base_Url}}" + route


def test_format_request():
    """Confirms atomic_request is a subset of request."""
    for route in routes:
        for method in get_app_route_methods(routes, route):
            request = format_request(routes, route, method)
            assert atomic_request().keys() <= request.keys()


def test_populate_blueprint():
    """Confirm subset of collection."""
    collection = collection_json()
    test_collection = collection.copy()
    for blueprint in blueprints:
        test_collection = populate_blueprint(collection, blueprints, blueprint, routes)
    assert collection.keys() <= test_collection.keys()


def test_populate_non_blueprint():
    """Confirm subset of collection."""
    collection = collection_json()
    test_collection = collection.copy()
    test_collection = add_non_blueprint_requests(collection, routes)
    assert collection.keys() <= test_collection.keys()


def test_generate_sanic_json():
    """Test generation of json file. Deletes after test."""
    filename = "tests/pytest_collection.json"
    generate_sanic_json("Testing with pytest", app, filename=filename)
    assert os.path.exists(filename)
    os.remove(filename)
    assert not os.path.exists(filename)
