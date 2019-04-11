from aiohttp import web, log

from settings import DEBUG


@web.middleware
async def exception_middleware(request: web.Request, handler) -> web.Response:
    try:
        response: web.Response = await handler(request)
        return response
    except Exception as ex:
        if DEBUG:
            log.server_logger.error(ex, exc_info=True)
        return web.json_response(dict(message=str(ex), code='SERVER_ERROR'), status=500)
