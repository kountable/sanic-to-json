import os
from sanic_to_json import (
    collection_json,
    atomic_request,
    basic_JSON,
    get_blueprints,
    get_blueprint_docs,
    get_blueprint_routes,
    get_blueprint_route_name,
    get_doc_string,
    get_route_method,
    get_url_prefix,
    add_blueprint_folders,
    format_blueprint_request,
    populate_blueprints,
    get_app_routes,
    get_app_route_name,
    get_app_route_url,
    get_app_route_methods,
    get_app_route_doc_string,
    format_app_request,
    add_app_requests,
)
from examples.app import app


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


def test_get_blueprints():
    assert get_blueprints(app) == app.blueprints


def test_get_blueprints_type():
    assert isinstance(get_blueprints(app), dict)


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


def test_get_doc_string():
    """Return doc string for function in blueprint route."""
    for blueprint in blueprints:
        for route in get_blueprint_routes(blueprints, blueprint):
            get_doc_string(route) == route[0].__doc__


def test_get_route_method():
    """Return route CRUD method."""
    for blueprint in blueprints:
        for route in get_blueprint_routes(blueprints, blueprint):
            get_route_method(route) == route[2][0]


def test_get_url_prefix():
    for blueprint in blueprints:
        get_url_prefix(blueprints, blueprint) == blueprints[
            blueprint
        ].version + blueprints[blueprint].url_prefix


def test_add_blueprint_folders():
    collection = collection_json()
    collection = add_blueprint_folders(collection, blueprints)
    assert set(blueprints.keys()) == set([item["name"] for item in collection["item"]])


def test_format_blueprint_request():
    for blueprint in blueprints:
        for route in get_blueprint_routes(blueprints, blueprint):
            assert (
                format_blueprint_request(blueprints, blueprint, route).keys()
                == atomic_request().keys()
            )


def test_populate_blueprints():
    collection = collection_json()
    collection = populate_blueprints(collection, blueprints)
    for folder, blueprint in zip(collection["item"], app.blueprints):
        assert len(folder["item"]) == len(app.blueprints[blueprint].routes)


# app routes
def test_get_app_routes():
    """Return routes in main app."""
    routes = {}
    for route in app.router.routes_names:
        if "." not in route:
            routes[route] = app.router.routes_names[route]
    assert routes == get_app_routes(app)


routes = get_app_routes(app)


def test_get_app_route_name():
    """Return app route name."""
    for route in routes:
        assert get_app_route_name(routes, route) == routes[route][0]


def test_get_app_route_url():
    """Return app route name."""
    for route in routes:
        assert get_app_route_url(routes, route) == routes[route][1].name


def test_get_app_route_methods():
    """Return CRUD methods for routes in main app."""
    for route in routes:
        assert set(get_app_route_methods(routes, route)) == set(
            routes[route][1].methods
        )


def test_get_app_route_doc_string():
    """Return CRUD methods for routes in main app."""
    for route in routes:
        for method in get_app_route_methods(routes, route):
            assert isinstance(get_app_route_doc_string(routes, route, method), str)


def test_format_app_request():
    """validate dicts have same keys."""
    for route in routes:
        for method in get_app_route_methods(routes, route):
            assert (
                format_app_request(routes, route, method).keys()
                == atomic_request().keys()
            )


def test_add_app_requests():
    collection = collection_json()
    collection = add_app_requests(collection, app)
    assert len(collection["item"]) == len(get_blueprints(app)) + len(routes)


# def test_generate_postman_json():
#    """Test generation of json file. Deletes after test."""
#    filename = "Test_collection.json"
#    generate_postman_json("Testing", app, filename=filename)
#    assert os.path.exists(filename)
#    os.remove(filename)
#    assert not os.path.exists(filename)
#

