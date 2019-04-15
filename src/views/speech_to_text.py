from aiohttp import web
from aiohttp.web_request import FileField
from integrations import google_stt
import jwt
from constants import public_key


class SpeechToTextView(web.View):
    async def check_req(self, data):
        try:
            encoded = data['key']
            jwt.decode(encoded, public_key, algorithms='RS256')
        except Exception as e:
            print(e)
            data = {"error": "Secret key is incorrect!"}
            return 400, data

        if 'audio_file' not in data:
            data = {"error": "File key not correctly transmitted."}
            return 400, data

        audio_file = data.get('audio_file')
        if not isinstance(audio_file, FileField):
            data = {"error": "You did not transfer the file."}
            return 404, data

        audio_type = audio_file.filename.split(".")[-1]
        if audio_type != 'flac':
            data = {"error": "The extension of your file is not .flac ."}
            return 406, data

        return 200, audio_file.file

    async def post(self):
        data = await self.request.post()
        status, data = await self.check_req(data)
        if status != 200:
            return web.json_response(data=data, status=status)

        audio_file = data
        try:
            audio_text = await google_stt.speech_to_text(audio_file)
            data = {"text": audio_text}
            return web.json_response(data=data, status=200)
        except Exception as e:
            data = {"error": str(e)}
            return web.json_response(data, status=502)
