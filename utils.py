import asyncio
import os
import subprocess


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


async def main(urls, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    tasks = [download_audio_url(url, output_path) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    urls = [
        'https://www.youtube.com/watch?v=your_video_id1',
        'https://www.youtube.com/watch?v=your_video_id2',
    ]
    output_path = 'downloads'
    asyncio.run(main(urls, output_path))
