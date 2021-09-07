import os

from sanic import Sanic, Request
from sanic import response
import sys


app = Sanic("media-app")


@app.get("/video/<id:int>/<hash:str>")
async def hello_world(request: Request, id, hash) -> response.HTTPResponse:
    return response.text(f"content ... {id}/{hash}")

if __name__ == '__main__':
    host = os.getenv('HOST') or sys.argv[1]
    app.run(host='0.0.0.0', port=host, debug=True)
