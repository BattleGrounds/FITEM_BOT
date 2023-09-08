import telebot
from database import Database
from telebot import types
bot = telebot.TeleBot('6033810139:AAHy9yDjSH2j-0akVF9QPmnnxsWIXps1EjU')

db = Database()


@bot.message_handler(commands=["start", "help"])
def get_command_messages(message):
    if message.text[1:] == "start":
        bot.send_message(message.from_user.id, "Доступные команды:\n\tНайтиПоНазванию То что хотите найти...\n\tНайтиПоТексту То что хотите найти...")
    elif message.text[1:] == "start":
        bot.send_message(message.from_user.id, "Доступные команды:\n\tНайтиПоНазванию То что хотите найти...\n\tНайтиПоТексту То что хотите найти...")
    else:
        bot.send_message(message.from_user.id, "Я не знаю таких комманд(")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет! Чем могу помочь?")
    elif message.text[:16] == "НайтиПоНазванию ":
        kbd = types.InlineKeyboardMarkup()
        for article in db.findByName(message.text[17:]):
            k = types.InlineKeyboardButton(text=article[0], callback_data=article[0])
            kbd.add(k)
        bot.send_message(message.from_user.id, "Найдено: ", reply_markup=kbd)
    elif message.text[:14] == "НайтиПоТексту ":
        kbd = types.InlineKeyboardMarkup()
        for article in db.findByText(message.text[15:]):
            k = types.InlineKeyboardButton(text=article[0], callback_data=article[0])
            kbd.add(k)
        bot.send_message(message.from_user.id, "Найдено: ", reply_markup=kbd)
    else:
        bot.send_message(message.from_user.id, "Не понимаю тебя((!")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.send_message(call.message.chat.id, db.get_article(call.data)[1])



bot.infinity_polling()

