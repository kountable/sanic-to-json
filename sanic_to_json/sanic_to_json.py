def get_all_routes(app):
    """Returns all routes from Sanic app, excludes duplicates."""
    all_routes = app.router.routes_all
    routes = {}
    for route in all_routes:
        if route[-1] != "/":
            routes[route] = all_routes[route]
    return routes


def get_route_name(route):
    """Returns route name."""
    name = route.split("/")[-1]
    return name


def get_app_route_methods(routes, route):
    """Return route CRUD method (GET, POST, etc)."""
    methods = list(routes[route].methods)
    return methods


def get_route_doc_string(routes, route, method):
    """Returns doc string for embedded route functions."""
    try:
        doc = routes[route][0].handlers[method].__doc__
    except AttributeError:
        doc = routes[route][0].__doc__
    return doc


def get_url(route, base_url="{{base_Url}}"):
    """Adds base_url environment variable to url prefix."""
    url = base_url + route
    return url


def format_request(routes, route, method, base_url="{{base_Url}}"):
    """Populates atomic_request dictionary with route metatdata.

    Returns a postman formatted dictionary request item."""
    request = atomic_request()
    doc = get_route_doc_string(routes, route, method)
    name = get_route_name(route)
    url = get_url(route, base_url=base_url)
    request["name"] = name
    request["request"]["method"] = method
    request["request"]["url"]["raw"] = url
    request["request"]["url"]["host"] = [url]
    request["request"]["description"] = doc
    # check doc strings for INI add extra keys
    if "INI" in doc:
        config_string = extract_ini_from_doc(doc)
        config = load_config(config_string)

        request = add_INI_data(doc, request, config)
        request["response"] = add_responses(request, config)
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
            example_request["originalRequest"]["url"]["raw"] += config[section]["query"]
            example_request["originalRequest"]["url"]["host"] = [
                example_request["originalRequest"]["url"]["raw"]
            ]

            response.append(example_request)
    return response


def populate_blueprint(
    api_json, blueprints, blueprint, routes, base_url="{{base_Url}}"
):
    """Populates endpoints for blueprint."""

    items = []
    for route in get_blueprint_routes(blueprint, routes):
        for method in get_app_route_methods(routes, route):
            items.append(format_request(routes, route, method, base_url=base_url))
    api_json["item"].append(
        {
            "name": blueprint,
            "description": get_blueprint_docs(blueprints, blueprint),
            "item": items,
        }
    )
    return api_json


def add_non_blueprint_requests(
    api_json, routes, base_url="{{base_Url}}", divider="JSON BODY\n    --------"
):
    """Add requests not added in populate_blueprints."""
    for route in routes:
        if "." not in routes[route].name:
            for method in get_app_route_methods(routes, route):
                request = format_request(routes, route, method, base_url=base_url)
                api_json["item"].append(request)
    return api_json


def save_as_json(collection_name, filename="postman_collection.json"):
    """Write dict to JSON file."""

    with open(filename, "w") as file:
        dump(collection_name, file, indent=4)


def generate_sanic_json(collection_name, app, filename="postman_collection.json"):
    """Generates json script from Sanic docs.

    Parameters
    ----------
    collection_name: str
        title of collection
    app: Sanic class
        Sanic app
    filename: str (optional)
        location of output file
    """
    # build basic json schema
    collection = basic_JSON(collection_name, app)

    # get routes and blueprints
    routes = get_all_routes(app)
    blueprints = get_blueprints(app)

    # populate blueprint requests
    for blueprint in blueprints:
        collection = populate_blueprint(collection, blueprints, blueprint, routes)

    # populate main app requests
    collection = add_non_blueprint_requests(collection, routes)

    # save dict to JSON file
    save_as_json(collection, filename=filename)

