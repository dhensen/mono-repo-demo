from sanic import Sanic
from sanic.response import json
import os

app = Sanic("App Name")


@app.route("/api")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv('PORTAAL_BACKEND_PORT', 8000)))
