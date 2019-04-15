import views
from aiohttp import web


def setup_routes(app):
    app.add_routes(
        [
            web.view("/upload_audio", views.SpeechToTextView)
        ]
    )
