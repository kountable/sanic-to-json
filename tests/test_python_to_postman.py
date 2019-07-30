from python_to_postman import collection_json, atomic_request, postman_JSON
from examples.app import app

"""Basic tests for python to postman script."""


def test_collection_items():
    """Assert the correct dicionary keys are present."""
    items = ["info", "item"]
    assert set(collection_json.keys()) == set(items)


def test_types():
    """Assert json templates are dicionaries."""
    json_templates = [collection_json, atomic_request]
    for template in json_templates:
        assert isinstance(template, dict)


def test_postman_JSON():
    """Checks 'collection_name' and doc string from Sanic app."""
    test_json = postman_JSON("test_collection", app)

    assert test_json["info"]["name"] == "test_collection"
    assert test_json["info"]["description"] == app.__doc__
