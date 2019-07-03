# python_to_postman
Generate Postman JSON file from python endpoints

Using the postman [schema](https://schema.getpostman.com/json/collection/v2.1.0/collection.json) we can build Postman Collections using python endpoints from Sanic or Flask. Note: endpoints need to be designated with `@`, for example `@app.route("example-route")`. 

