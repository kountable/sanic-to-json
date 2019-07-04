from read_routes import generate_postman_json
from app import app


generate_postman_json("Test_collection", app)
