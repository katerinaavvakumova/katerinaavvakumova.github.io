import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

print("Loaded API key:", api_key)
print("Loaded DB URL:", db_url)

# DO NOT hard-code secrets like this:
# api_key = "supersecret123"