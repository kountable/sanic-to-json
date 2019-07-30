from python_to_postman import generate_postman_json
from examples.app import app


generate_postman_json("Test_collection", app)
