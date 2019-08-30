from sanic_to_json.schema_helpers import atomic_request, collection_json, basic_JSON
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
