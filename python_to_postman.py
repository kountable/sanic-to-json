from json import load, loads, dump, dumps
from read_routes import format_endpoint
from app import app

# json dictionary has a simple file structure: name for folder, then
# then item: [namne, request:{method, header,url:  {raw, host} }]

api_json = {
    "info": {
        "name": "Test_collection",
        "description": "Generic text used for documentation.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "item": [],
}


api_json["info"]["description"] = app.__doc__

# print blueprints
blueprints = list(app.__dict__["blueprints"].keys())

# add folders from blueprints
for blueprint in blueprints:
    postman_item = {}
    postman_item["name"] = blueprint
    postman_item["item"] = []
    postman_item["description"] = app.blueprints[blueprint].__doc__
    for route in app.blueprints[blueprint].routes:
        postman_item["item"].append(format_endpoint(route))
    api_json["item"].append(postman_item)

# print(api_json)
with open("data_file.json", "w") as file:
    dump(api_json, file, indent=4)
