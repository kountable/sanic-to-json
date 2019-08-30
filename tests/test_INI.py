from examples.app import app
from sanic_to_json.INI_helpers import (
    extract_ini_from_doc,
    load_config,
    format_headers,
    format_json_body,
)
import configparser

# INI functions
test_doc = app.router.routes_all["/v1/a-prefix/endpoint-one"].handler.__doc__


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
    assert format_headers(test_config["request"]) == [
        {
            "key": "Content-Type",
            "name": "Content-Type",
            "value": "application/json",
            "type": "text",
        },
        {
            "key": "x-amz-sns-message-type",
            "name": "x-amz-sns-message-type",
            "value": "Notification",
            "type": "text",
        },
    ]


def test_format_json_body():
    test_ini = extract_ini_from_doc(test_doc)
    test_config = load_config(test_ini)
    test_body = format_json_body(test_config["request"])
    assert test_body == {"mode": "raw", "raw": {}}
