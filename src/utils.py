import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    token = os.getenv('WILDBERRIES_API_TOKEN')
    if not token:
        raise ValueError("API токен не найден. Проверьте файл .env")
    return token
