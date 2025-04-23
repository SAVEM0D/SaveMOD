import os
from dotenv import load_dotenv

load_dotenv()  # Для локального тестирования

# Получаем переменные из окружения Heroku или .env файла
BOT_TOKEN = os.getenv('BOT_TOKEN') or os.environ.get('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID') or int(os.environ.get('ADMIN_ID', 0))

# Проверка обязательных переменных
if not BOT_TOKEN:
    raise ValueError("Не указан BOT_TOKEN! Добавьте его в переменные Heroku")
if not ADMIN_ID:
    raise ValueError("Не указан ADMIN_ID! Добавьте его в переменные Heroku")
