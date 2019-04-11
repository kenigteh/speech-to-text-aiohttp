from aiohttp import web


async def health_view(request) -> web.Response:
    return web.json_response(dict(status='ok'))
