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

