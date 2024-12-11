from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен
BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_TOKEN = os.getenv("AI_TOKEN")
# Проверяем, что токен загрузился
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not defined. Please check your .env file or environment variables.")
if AI_TOKEN is None:
    raise ValueError("AI_TOKEN is not defined. Please check your .env file or environment variables.")
