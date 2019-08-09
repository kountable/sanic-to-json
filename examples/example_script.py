from generate_json import generate_sanic_json
from examples.app import app


generate_sanic_json("Test API", app, filename="postman_collection.json")
