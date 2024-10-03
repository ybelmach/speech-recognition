import asyncio

import whisper
from utils import download_audio_url
from s3_manager import s3_save


async def main():
    url1 = 'https://www.youtube.com/watch?v=LHyDqNEllyM&ab_channel=%D0%98%D0%B3%D0%BE%D1%80%D1%8C%D0%91%D0%B0%D0%B1%D0%BA%D0%BE'

    url2 = 'https://3ea85f17-b7fc-41a3-9241-61e9dfe83dcd.selstorage.ru/' + await s3_save(url=url1)
    model = whisper.load_model("turbo")
    result = model.transcribe(url2)
    print(result['text'])


if __name__ == '__main__':
    asyncio.run(main())
