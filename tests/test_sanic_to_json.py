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
