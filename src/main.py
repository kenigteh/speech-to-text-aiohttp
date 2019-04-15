import logging

from aiohttp import web

import settings
from middleware import MIDDLEWARES
from routes import setup_routes
from services import SERVICES


async def init_func():
    app = web.Application(middlewares=MIDDLEWARES)
    app.cleanup_ctx.extend(SERVICES)
    setup_routes(app)
    return app


logging.basicConfig(level=(logging.DEBUG if settings.DEBUG else logging.INFO))

if __name__ == '__main__':
    web.run_app(init_func(), port=8085)
