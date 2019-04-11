import logging

from aiohttp import web

import settings
from middleware import MIDDLEWARES
from routes import setup_routes
from services import SERVICES


async def init():
    app = web.Application(middlewares=MIDDLEWARES)
    app.cleanup_ctx.extend(SERVICES)
    setup_routes(app)
    return app


logging.basicConfig(level=(logging.INFO if not settings.DEBUG else logging.DEBUG))

if __name__ == '__main__':
    web.run_app(init(), port=8085)
