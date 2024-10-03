from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

PUBLIC_S3_KEY = os.getenv("PUBLIC_S3_KEY")
SECRET_S3_KEY = os.getenv("SECRET_S3_KEY")
