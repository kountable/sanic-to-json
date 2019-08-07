from sanic_to_json import generate_json
from examples.app import app


generate_json(collection_name="Test API", app=app)
