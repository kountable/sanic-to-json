from python_to_postman import collection_json, atomic_request

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
