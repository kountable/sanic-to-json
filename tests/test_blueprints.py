from examples.app import app
from sanic_to_json.blueprint_helpers import (
    get_blueprints,
    get_blueprint_routes,
    get_blueprint_docs,
    populate_blueprint,
    add_non_blueprint_requests,
)
from sanic_to_json.app_helpers import get_all_routes
from sanic_to_json.schema_helpers import collection_json


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
