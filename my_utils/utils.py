import asyncio
import uuid

import whisper

from my_utils.s3_manager import s3_save
from config import DOMAIN


async def download_audio_url(url, output_path):
    print(f"Downloading video from {url}...")
    command = [
        'yt-dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '-o', output_path,
        url
    ]
    process = await asyncio.create_subprocess_exec(*command)
    await process.wait()
    print(f"Downloaded: {url}")


async def start_llm(video_url: str):
    file_name = await s3_save(url=video_url, mode='video')
    file_url = DOMAIN + file_name
    model = whisper.load_model("turbo")
    result = model.transcribe(file_url)
    result_text = result['text']
    text_file_url = await create_txt_file(result_text)
    return result_text, text_file_url


async def create_txt_file(text: str):
    url = 't_' + str(uuid.uuid4()).split('-')[0] + '.txt'
    with open(url, 'w') as file:
        file.write(text)
    file_name = await s3_save(url=url, mode='text')
    file_url = DOMAIN + file_name
    return file_url


if __name__ == '__main__':
    pass
