import os

from examples.app import app
from sanic_to_json.generate_json import generate_sanic_json


def test_generate_sanic_json():
    """Test generation of json file. Deletes after test."""
    filename = "tests/pytest_collection.json"
    generate_sanic_json("Testing with pytest", app, filename=filename)
    assert os.path.exists(filename)
    os.remove(filename)
    assert not os.path.exists(filename)
