import os
from dotenv import load_dotenv

load_dotenv()

# Получаем переменные окружения
BOT_TOKEN = os.getenv('BOT_TOKEN') or os.environ.get('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID') or int(os.environ.get('ADMIN_ID', '0')))

# Проверка наличия обязательных переменных
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен! Добавьте его в переменные Heroku")
if not ADMIN_ID:
    raise ValueError("ADMIN_ID не установлен! Добавьте его в переменные Heroku")
