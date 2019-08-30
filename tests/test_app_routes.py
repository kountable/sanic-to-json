from examples.app import app
from sanic_to_json.app_helpers import (
    get_all_routes,
    get_route_name,
    get_app_route_methods,
    get_url,
    get_route_doc_string,
    format_request,
)
from sanic_to_json.schema_helpers import atomic_request

routes = get_all_routes(app)


def test_get_all_routes():
    """Returns all routes from Sanic app, excludes duplicates."""
    assert get_all_routes(app).items() <= app.router.routes_all.items()


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
