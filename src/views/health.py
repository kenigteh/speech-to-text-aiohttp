from aiohttp import web


async def health_view(request) -> web.Response:
    http_client = request.app['external_api']
    response = await http_client.get('https://api.chucknorris.io/jokes/random')  # TODO: Не учитесь плохому коду
    json_response = await response.json()
    return web.json_response(json_response.get('value', 'Ошибока'))
