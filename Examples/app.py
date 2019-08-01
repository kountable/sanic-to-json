from examples.blueprint_1 import bp1
from examples.blueprint_2 import bp2
from sanic import Sanic


app = Sanic(__name__)
app.__doc__ = "A doc string for the API. Blueprints have their own doc strings."
app.blueprint([bp1, bp2])


@app.listener("before_server_start")
async def setup_db(app, loop):
    pass


@app.listener("after_server_stop")
async def close_db(app, loop):
    pass


@app.route("/healthcheck", methods=["GET"])
async def health(request):
    """Return health status."""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
