from os import getenv
from dotenv import load_dotenv

load_dotenv()

credenciais = {
    'app_key': getenv('APP_KEY'),
    'app_secret': getenv('APP_SECRET')
}