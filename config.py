import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.getenv("DATABASE_HOST")
database = os.getenv("DATABASE_NAME")
database_password = os.getenv("DATABASE_PASSWORD")
database_username = os.getenv("DATABASE_USER")
