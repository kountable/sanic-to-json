<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
# sanic_to_postman
Generate Postman JSON file from python endpoints

Using the postman [schema](https://schema.getpostman.com/json/collection/v2.1.0/collection.json) we can build Postman Collections using python endpoints from Sanic (Flask apps need testing). The script reads Sanic app. It searches for blueprints. The blueprints, through routes, provide docs strings data. The doc string data is used to populate a Postman formatted JSON file. The JSON file can be uploaded to Postman as a collection. 

Once we have Postman formatted JSON we can create API documentation through the Postman [API](https://docs.api.getpostman.com/?version=latest#3190c896-4216-a0a3-aa38-a041d0c2eb72)

Unfortunately, there is not a streamlined method to retreive routes in blueprints and main app. Ok, there is, but if you reuse function names, (e.g., `aysnc def post(request)` ) then some of the route method retrieval methods don't work because routes get saved in a dictionary. And dictionaries can't have duplicate keys. 

- run `generate_postman_json("collection_name", app)` Formats the Postman collection with 'collection_name' and doc strings from Sanic app, e.g., `postman_collection.json` 

# How to document Sanic app and Blueprints
- As the example shows, the Sanic app should have a `.doc` attribute. This doc string will serve as the introduction to the API in Postman docs, e.g., `app.__doc__ = "This API does stuff."`

- Blueprints should also a doc string, this will serve as the description to each collection folder in Postman. Again see `examples` folder
`bp1.__doc__ = "This is the doc string for blueprint1."`

- In the main Sanic app routes should have different funcion names, multiple methods are ok. In contrast, Blueprints are allowed to repeat function names e.g., `aysnc def post(request)`

# To do 
- At the moment endpoints are assumed to accept raw JSON, as passed by the header option in `sanic_to_json.atomic_requests`  
```
"header": [
            {
                "key": "Content-Type",
                "name": "Content-Type",
                "value": "application/json",
                "type": "text",
            }
          ]
```
Arguments to the header key could be passed in the doc strings, but I'll leave that for a future endevaor. 

- Because Sanic routes are accessed through a dictionary, `app.router.routes_names`, the underlying function names need to be unique for each route, .i.e., async defining routes `/health` and `/test`. 


# Contributors

See the [GitHub contributor page](https://github.com/caheredia/python_to_postman/graphs/contributors)
