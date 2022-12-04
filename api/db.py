from motor.motor_asyncio import AsyncIOMotorClient

from config import *

class Database:
	client: AsyncIOMotorClient = None

db = Database()

async def get_database() -> AsyncIOMotorClient:
	return db.client[MONGO_DB_NAME]

def get_db():
	return db.client[MONGO_DB_NAME]

async def connect_to_mongo():
	print('Connecting to database...')
	db.client = AsyncIOMotorClient(
                f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_ENDPOINT}/{MONGO_DB_NAME}?retryWrites=true&w=majority'
        )
	# db.client = AsyncIOMotorClient(
    #             f'mongodb://localhost:27017/AA_ASR'
    #     )

	print('Connected!')

async def close_mongo_connection():
	print('Disconnecting from database...')
	db.client.close()
	print('Disconnected!')
