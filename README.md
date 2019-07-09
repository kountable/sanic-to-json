# python_to_postman
Generate Postman JSON file from python endpoints

Using the postman [schema](https://schema.getpostman.com/json/collection/v2.1.0/collection.json) we can build Postman Collections using python endpoints from Sanic or Flask. The script reads Sanic app. It searches for blueprints. The blueprints, through routes, provide docs strings data. The doc string data is used to populate a Postman formatted JSON file. The JSON file can be uploaded to Postman as a collection. 

# requests is a list of items per blueprint

# Need to add option for postman ID