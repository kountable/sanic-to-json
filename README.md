<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
# python_to_postman
Generate Postman JSON file from python endpoints

Using the postman [schema](https://schema.getpostman.com/json/collection/v2.1.0/collection.json) we can build Postman Collections using python endpoints from Sanic or Flask. The script reads Sanic app. It searches for blueprints. The blueprints, through routes, provide docs strings data. The doc string data is used to populate a Postman formatted JSON file. The JSON file can be uploaded to Postman as a collection. 

- run `generate_postman_json("collection_name", app)` Formats the Postman collection with 'collection_name' and doc strings from Sanic app, e.g., `postman_collection.json` 

# How to document Sanic app and Blueprints
- As the example shows, the Sanic app should have a `.doc` attribute. This doc string will serve as the introduction to the API in Postman docs, e.g., `app.__doc__ = "This API does stuff."`

- Blueprints should also a doc string, this will serve as the description to each collection folder in Postman. Again see `examples` folder
`bp1.__doc__ = "This is the doc string for blueprint1."`

