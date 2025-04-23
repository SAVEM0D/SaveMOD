from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
import random
import asyncio
import sqlite3
from datetime import datetime
from emoji_config import AnimatedEmoji

router = Router()

# Основные команды
@router.message(Command("help"))
async def help_command(message: Message):
    help_text = f"""
<tg-emoji emoji-id="{AnimatedEmoji.PAPER}">📝</tg-emoji> <b><u>ДОСТУПНЫЕ КОМАНДЫ</u></b>

<tg-emoji emoji-id="{AnimatedEmoji.HEART}">✨</tg-emoji> <b>Основные</b>
✦ <code>.help</code> — это меню
✦ <code>.info @username</code> — метаданные аккаунта
✦ <code>.dox</code> — фейк-досье
✦ <code>.deanon</code> — фейк-деанон

<tg-emoji emoji-id="{AnimatedEmoji.HEART}">💖</tg-emoji> <b>Анимации</b>
✦ <code>.love</code> — магическая любовь
✦ <code>.love2</code> — любовь v2
✦ <code>.-7</code> — гуль 1000-7
✦ <code>/p текст</code> — анимация печати

<tg-emoji emoji-id="{AnimatedEmoji.BOMB}">⚡</tg-emoji> <b>Эксперименты</b>
✦ <code>.spam N текст</code> — спам
✦ <code>.crash</code> — краш Android
✦ <code>.crash2</code> — краш iOS
"""
    await message.reply(help_text, parse_mode="HTML")

# Анимационные команды
@router.message(Command("p"))
async def print_animation(message: Message):
    try:
        text = message.text.split(maxsplit=1)[1]
    except IndexError:
        text = "Пример текста для анимации"
    
    msg = await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.SCAN}'>⌨️</tg-emoji> "
        "<i>Подготовка печати...</i>",
        parse_mode="HTML"
    )
    await asyncio.sleep(0.5)
    
    for i in range(1, len(text)+1):
        await msg.edit_text(
            f"<tg-emoji emoji-id='{AnimatedEmoji.SCAN}'>⌨️</tg-emoji> "
            f"{text[:i]}_",
            parse_mode="HTML"
        )
        await asyncio.sleep(0.05)
    
    await msg.edit_text(
        f"<tg-emoji emoji-id='{AnimatedEmoji.PAPER}'>📜</tg-emoji> "
        f"<b>Результат:</b>\n{text}",
        parse_mode="HTML"
    )

@router.message(Command("love"))
async def love_command(message: Message):
    hearts = [
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[0]}'>💖</tg-emoji>",
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[1]}'>💘</tg-emoji>",
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[2]}'>💓</tg-emoji>"
    ]
    
    for _ in range(3):
        combo = random.sample(hearts, 3)
        await message.answer(" ".join(combo))
        await asyncio.sleep(0.3)
    
    await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[3]}'>💕</tg-emoji> "
        "I LOVE YOU "
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[3]}'>💕</tg-emoji>"
    )

@router.message(Command("love2"))
async def love2_command(message: Message):
    heart_frames = [
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[0]}'>💖</tg-emoji>",
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[0]}'>💖</tg-emoji>" * 2,
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[0]}'>💖</tg-emoji>" * 3,
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[0]}'>💖</tg-emoji>" * 4,
        f"<tg-emoji emoji-id='{AnimatedEmoji.HEARTS[0]}'>💖</tg-emoji>" * 5 + "\nI LOVE YOU"
    ]
    
    for frame in heart_frames:
        await message.answer(frame)
        await asyncio.sleep(0.4)

@router.message(Command("-7"))
async def minus7_command(message: Message):
    count = 1000
    msg = await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.CHAINS}'>⛓️</tg-emoji> "
        f"<code>「{count} ➖ 7 = {count-7}」</code>\n"
        f"<tg-emoji emoji-id='{AnimatedEmoji.BLOOD}'>🩸</tg-emoji> "
        "<i>Кошмар не уходит...</i>",
        parse_mode="HTML"
    )
    
    while count > 7:
        count -= 7
        await msg.edit_text(
            f"<tg-emoji emoji-id='{AnimatedEmoji.CHAINS}'>⛓️</tg-emoji> "
            f"<code>「{count+7} ➖ 7 = {count}」</code>\n"
            f"<tg-emoji emoji-id='{AnimatedEmoji.BLOOD}'>🩸</tg-emoji> "
            f"<tg-emoji emoji-id='{AnimatedEmoji.HEART}'>🤍</tg-emoji> "
            f"<code>{count}</code>",
            parse_mode="HTML"
        )
        await asyncio.sleep(0.3)
    
    await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.GHOST}'>💀</tg-emoji> "
        "<b>Ты гуль.</b>",
        parse_mode="HTML"
    )
    await asyncio.sleep(1)
    await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.SAD}'>😔</tg-emoji> "
        "<i>1000-7, я умер прости</i>",
        parse_mode="HTML"
    )

# Экспериментальные команды
@router.message(Command("spam"))
async def spam_command(message: Message):
    try:
        args = message.text.split(maxsplit=2)
        if len(args) < 3:
            return await message.reply(
                f"<tg-emoji emoji-id='{AnimatedEmoji.WARNING}'>⚠️</tg-emoji> "
                "<i>Формат: <code>.spam [число] [текст]</code></i>",
                parse_mode="HTML"
            )
        
        count = min(int(args[1]), 20)
        for _ in range(count):
            await message.answer(args[2])
            await asyncio.sleep(0.3)
    except ValueError:
        await message.reply(
            f"<tg-emoji emoji-id='{AnimatedEmoji.WARNING}'>⚠️</tg-emoji> "
            "<i>Укажите корректное число!</i>",
            parse_mode="HTML"
        )

@router.message(Command("crash"))
async def crash_command(message: Message):
    await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.BOMB}'>💥</tg-emoji> "
        "<b>Имитация краша для Android...</b>",
        parse_mode="HTML"
    )
    await asyncio.sleep(1)
    await message.answer("‍" * 400)

@router.message(Command("crash2"))
async def crash2_command(message: Message):
    await message.answer(
        f"<tg-emoji emoji-id='{AnimatedEmoji.BOMB}'>💣</tg-emoji> "
        "<b>Имитация краша v2...</b>",
        parse_mode="HTML"
    )
    await asyncio.sleep(1)
    await message.answer("▄︻デ══━一" * 50)

# Другие команды (info, deanon и т.д. из предыдущих примеров)
# ...