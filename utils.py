import sqlite3
import os
from aiogram.types import Message
from datetime import datetime

async def setup_db():
    os.makedirs("media", exist_ok=True)
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS message_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            old_text TEXT,
            new_text TEXT,
            is_edited BOOLEAN DEFAULT 0,
            is_deleted BOOLEAN DEFAULT 0,
            media_path TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()

async def log_edited_message(message: Message):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO message_logs 
        (user_id, username, old_text, new_text, is_edited, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        message.from_user.id,
        message.from_user.username,
        "Предыдущий текст недоступен",  # В реальности нужно хранить историю
        message.text,
        1,
        datetime.now()
    ))
    conn.commit()
    conn.close()