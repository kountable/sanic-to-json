from blueprint_1 import bp1
from blueprint_2 import bp2
from sanic import Sanic


app = Sanic(__name__)
app.__doc__ = "A doc string for the API. Blueprints have their own doc strings."
app.blueprint([bp1, bp2])


@app.listener("before_server_start")
async def setup_db(app, loop):
    logger.debug("root before_server_start 'opening thrift transport'")
    transport.open()


@app.listener("after_server_stop")
async def close_db(app, loop):
    logger.debug("root after_server_start 'closing thrift transport'")
    transport.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=local_instance)
