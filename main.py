# Домашнее задание 9 Семинар
# Реализовать телеграмм бота, который может здороваться с пользователем по имени и складывать числа

# /hello
# /sum

# Задание дополнительное (Сдавать к семинару 10)
# Прикрутить к боту новые возможности (один пункт на выбор - все реализовывать не обязательно!):
# - игра в крестики-нолики
# - игра в конфеты
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# - сообщать пользователю фазу луны в зависимости от даты
# - сообщать пользователю, сколько дней осталось до Нового Года

# =============================================================================

# Решение:

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

'''====================================ОПЕРАЦИИ========================================='''

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(x+y)

'''=====================================ВАШ_БОТ========================================='''

app = ApplicationBuilder().token(">>>----->BOT_TOKEN<-----<<<").build()

'''=================================ВЫЗОВ_ОПЕРАЦИЙ======================================'''

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))

app.run_polling()
print("Start_bot")
# =============================================================================
