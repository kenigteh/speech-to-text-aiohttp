from .exception import exception_middleware

MIDDLEWARES = [
    exception_middleware
]

__all__ = [
    'MIDDLEWARES'
]
