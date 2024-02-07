import telebot 
from config import Token_Tg

Bot = telebot.TeleBot(Token_Tg)

@Bot.message_handler(commands={"start"}):