import asyncio
from typing import AsyncGenerator

import aiohttp
from aiohttp import log


async def external_api(app) -> AsyncGenerator:
    """
    Создаёт клиентскую сессию с External API
    :param app:
    :return:
    """

    app['external_api'] = aiohttp.ClientSession(
        headers={
            'Content-Type': 'application/json',
        },
    )

    log.server_logger.info('External API session pool established')

    yield

    log.server_logger.info('Closing external API session pool')
    await asyncio.sleep(0.250)
    await app['external_api'].close()
