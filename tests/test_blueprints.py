from examples.app import app
from sanic_to_json.blueprint_helpers import (
    get_blueprints,
    get_blueprint_routes,
    get_blueprint_docs,
)
from sanic_to_json.app_helpers import get_all_routes


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
