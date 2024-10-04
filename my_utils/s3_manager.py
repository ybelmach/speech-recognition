import asyncio
import os.path
import uuid
from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from config import SECRET_S3_KEY, PUBLIC_S3_KEY
import my_utils.utils as utils


class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client('s3', **self.config, verify=False) as client:
            yield client

    async def upload_file(self, file_path: str):
        if os.path.exists(file_path):
            async with self.get_client() as client:
                with open(file_path, 'rb') as file:
                    await client.put_object(Bucket=self.bucket_name, Key=file_path, Body=file)
            print(f"[INFO] Successfully uploaded {file_path}")
        else:
            raise Exception(f"[ERROR] File {file_path} wasn't upload")
        if os.path.exists(file_path):
            os.remove(file_path)
        return file_path


async def s3_save(url: str, **kwargs):
    s3_client = S3Client(
        access_key=PUBLIC_S3_KEY,
        secret_key=SECRET_S3_KEY,
        endpoint_url='https://s3.ru-1.storage.selcloud.ru',
        bucket_name='speech-recognition-videos',
    )

    mode = kwargs.get('mode')
    if mode:
        if mode == 'video':
            file_path = 'v_' + str(uuid.uuid4()).split('-')[0]
            await utils.download_audio_url(url=url, output_path=file_path)
            file_path += '.mp3'
            return await s3_client.upload_file(file_path=file_path)
        if mode == 'text':
            return await s3_client.upload_file(file_path=url)
        if mode == 'audio':
            file_path = 'a_' + str(uuid.uuid4()).split('-')[0] + '.mp3'
            return await s3_client.upload_file(file_path=file_path)
    else:
        raise ValueError("Unknown mode")
