import requests
from bs4 import BeautifulSoup
import telebot

# python heh.py

# 859071138:AAGbzXZ7cSfrQdUMxjaKBOA20VY7i_WgzbM
# https://api.telegram.org/bot859071138:AAGbzXZ7cSfrQdUMxjaKBOA20VY7i_WgzbM/getMe
bot = telebot.TeleBot('859071138:AAGbzXZ7cSfrQdUMxjaKBOA20VY7i_WgzbM');

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    }


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, 'Я бот который найдет тебе все что ты хочешь!(в пределах Google)')
    bot.send_message(message.chat.id, 'Введи команду /google ')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Чтобы начать гуглить введи команду: /google ')


def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q
    r = s.get(url, headers=headers_Get)
    soup = BeautifulSoup(r.text, "html.parser")
    output = []
    for search in soup.find_all('div', {'class':'r'}):
        url = search.find('a')["href"]
        result = url
        output.append(result)
    if len(output) < 10:
        url + '&start=10'
        for search in soup.find_all('div', {'class': 'r'}):
            while len(output) < 10:
                url = search.find('a')["href"]
                result = url
                output.append(result)
        return output
    else:
        return output



@bot.message_handler(commands=['google'])
def messageSearch(message):
    send = bot.send_message(message.chat.id, 'Введи запрос')
    bot.register_next_step_handler(send, heh)

def heh(message):
    for i in range(10):
        bot.send_message(message.chat.id, 'Сайт номер: ' + str(i+1))
        bot.send_message(message.chat.id, google(message.text)[i])
        i += 1

bot.polling(none_stop=True, interval=0)

