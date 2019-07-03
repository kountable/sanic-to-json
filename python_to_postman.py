from json import load, loads, dump, dumps

# json dictionary has a simple file structure: name for folder, then
# then item: [namne, request:{method, header,url:  {raw, host} }]

api_json = {
    "info": {
        "_postman_id": "8ca65fb5-6ed0-427f-83f8-e626582748ce",
        "name": "Test_collection",
        "description": "Generic text used for documentation.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "item": [],
}

basic_endpoint = {
    "name": "test request",
    "request": {
        "method": "GET",
        "header": [],
        "url": {"raw": "{{url}}test-employees", "host": ["{{url}}test-employees"]},
        "description": "This description can come from docs strings",
    },
    "response": [],
}

api_json["item"].append(basic_endpoint)
new_endpoint = basic_endpoint.copy()
new_endpoint["name"] = "copied endpoint"
api_json["item"].append(new_endpoint)
# print(api_json)
with open("data_file.json", "w") as file:
    dump(api_json, file, indent=4)
