import base64
import aiohttp
import constants

REQ_DATA = constants.REQ_DATA


async def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content).decode("ascii")


async def create_rec(audio_content):
    data = {
        'config': {
            'encoding': REQ_DATA["encoding"],
            'languageCode': REQ_DATA["languageCode"]
        },
        'audio': {
            'content': audio_content
        }
    }
    return data


async def send_req(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=constants.url,
                                json=data,
                                params={"key": constants.key}) as resp:
            return await resp.json()


async def speech_to_text(audio_file):
    data = await encode_audio(audio_file)
    req_data = await create_rec(data)
    ans = await send_req(req_data)
    if 'error' in ans:
        raise Exception(ans['error']['message'])
    return ans['results'][0]['alternatives'][0]['transcript']
