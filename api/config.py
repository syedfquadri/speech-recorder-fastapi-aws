import os
from dotenv import dotenv_values, load_dotenv,find_dotenv
load_dotenv(find_dotenv())
MONGO_ENDPOINT = os.environ.get("MONGO_ENDPOINT")
# MONGO_ENDPOINT = os.getenv('MONGO_ENDPOINT')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'AA_ASR')

LEN_AUDIO_URL = 1
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")