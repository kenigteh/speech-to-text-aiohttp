from typing import Callable, List

from .http_client import external_api

SERVICES: List[Callable] = [
    external_api
]

__all__ = [
    'external_api',
    'SERVICES'
]
