key = 'AIzaSyAPgaSnLgDd0tIP_YxfKXBf59fNQ-IKocA'
url = f"https://speech.googleapis.com/v1/speech:recognize?alt=json&key={key}"

REQ_DATA = {
    "encoding": "FLAC",
    "languageCode": "ru-RU"
}

with open("files/public_key.txt") as f:
    public_key = f.read()
