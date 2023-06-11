import telebot
import string
import random

from telebot import types

bot = telebot.TeleBot("6193282100:AAGTLLBgKDEeKCEodURBxnhUCGHC3CXc9GM")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("/password_easy")
item2 = types.KeyboardButton("/password_normal")
item3 = types.KeyboardButton("/password_hard")

markup.add(item1)
markup.add(item2)
markup.add(item3)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Добро пожаловать в генератор паролей', reply_markup=markup)

@bot.message_handler(commands=['password_easy'])

def genrate_password(message):
    characters = string.ascii_letters + string.digits
# Добавить спец симолы: + string.punctuation

# Generate random charecter
    password = "".join(random.choice(characters) for x in range(random.randint(6, 6)))

    # Keyboard
    bot.send_message(message.chat.id, f"{password}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == 'private':
        if message.text == 'password':
            bot.send_message(message.chat.id, str(random.randint(0.100)))

@bot.message_handler(commands=['password_normal'])

def genrate_passwordnormal(message):
    characters = string.ascii_letters + string.digits

# Generate random charecter
    passwordnormal = "".join(random.choice(characters) for x in range(random.randint(8, 9)))

    # Keyboard
    bot.send_message(message.chat.id, f"{passwordnormal}")

@bot.message_handler(commands=['password_hard'])

def genrate_passwordhard(message):
    characters = string.ascii_letters + string.digits + string.punctuation

# Generate random charecter
    passwordhard = "".join(random.choice(characters) for x in range(random.randint(9, 10)))

    # Keyboard
    bot.send_message(message.chat.id, f"{passwordhard}")

bot.polling()

