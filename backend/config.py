from dotenv import load_dotenv
import os
load_dotenv(override=True)

db_url=os.getenv("DATABASE_URL")
secret_key=os.getenv("SECRET_KEY")
algorithm=os.getenv("ALGORITHM")
access_token_expire_time=60
