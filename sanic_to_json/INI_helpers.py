import configparser
from json import dumps


def extract_ini_from_doc(doc):
    """Extracts INI from doc strings."""
    return doc.rsplit("INI")[-1]


def load_config(ini_string):
    """Load config parse from string."""
    # Override lower case key conversion
    config = configparser.RawConfigParser()
    config.optionxform = lambda option: option
    config.read_string(ini_string)
    return config


def format_headers(config_section):
    """Returns a list of formatted header dictionaries."""
    request_header = []
    try:
        header_items = eval(config_section["header"])
        for key in header_items:
            header = {
                "key": key,
                "name": key,
                "value": header_items[key],
                "type": "text",
            }
            request_header.append(header)
    except KeyError:
        pass
    return request_header


def format_json_body(config_section):
    """formats JSON body from config as raw JSON."""
    body = {}
    body["mode"] = "raw"
    body["raw"] = {}
    try:
        body_dict = eval(config_section["body"])
        for key in body_dict:
            body["raw"][key] = body_dict[key]
        body["raw"] = dumps(body["raw"])
    except KeyError:
        pass
    return body


def add_INI_data(doc, request, config):
    """adds INI elements to atomic request. Returns altered request."""
    body = format_json_body(config["request"])
    request["request"]["body"] = body

    head = format_headers(config["request"])
    request["request"]["header"] = head

    request["protocolProfileBehavior"] = {"disableBodyPruning": True}
    return request


def add_responses(request, config):
    """Response is a list of dictionary requests."""
    response = []
    for section in config.sections():
        example_request = {}
        example_request["originalRequest"] = {}
        if "example" in section:
            example_request["name"] = config[section]["name"]
            example_request["originalRequest"]["method"] = config[section]["method"]
            example_request["originalRequest"]["header"] = format_headers(
                config[section]
            )
            example_request["originalRequest"]["body"] = format_json_body(
                config[section]
            )
            example_request["originalRequest"]["url"] = request["request"]["url"].copy()
            if "query" in config[section].keys():
                example_request["originalRequest"]["url"]["raw"] += config[section][
                    "query"
                ]
            example_request["originalRequest"]["url"]["host"] = [
                example_request["originalRequest"]["url"]["raw"]
            ]

            response.append(example_request)
    return response
