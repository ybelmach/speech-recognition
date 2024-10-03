import asyncio
import whisper

from my_utils.s3_manager import s3_save


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
    file_url = 'https://3ea85f17-b7fc-41a3-9241-61e9dfe83dcd.selstorage.ru/' + await s3_save(url=video_url)
    model = whisper.load_model("turbo")
    result = model.transcribe(file_url)
    result_text = result['text']
    return result_text


if __name__ == '__main__':
    pass
