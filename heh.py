import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot('859071138:AAGbzXZ7cSfrQdUMxjaKBOA20VY7i_WgzbM');

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    }


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, you wrote me a command: /start')
    bot.send_message(message.chat.id, 'I ma a bot which find for you any query in Google search!')
    bot.send_message(message.chat.id, 'Enter a command: /google')


@bot.message_handler(commands = ['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'For search enter a command: /google ')


def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q
    r = s.get(url, headers = headers_Get)
    soup = BeautifulSoup(r.text, "html.parser")
    output = []
    for search in soup.find_all('div', {'class':'r'}):
        url = search.find('a')["href"]
        result = url
        output.append(result)
    if len(output) < 10:
        url = 'https://www.google.com/search?q=' + q
        ifLen10(url, output)
        return output
    else:
        return output


def ifLen10(url, output):
    url += '&start=10'
    s = requests.Session()
    r = s.get(url, headers=headers_Get)
    soup = BeautifulSoup(r.text, "html.parser")
    for search in soup.find_all('div', {'class': 'r'}):
        url = search.find('a')["href"]
        result = url
        if len(output) < 10:
            output.append(result)
    return output


@bot.message_handler(commands=['google'])
def messageSearch(message):
    send = bot.send_message(message.chat.id, 'Enter the query!')
    bot.register_next_step_handler(send, heh)


def heh(message):
    for i in range(10):
        bot.send_message(message.chat.id, 'Website number: ' + str(i+1))
        bot.send_message(message.chat.id, google(message.text)[i])
        i += 1

bot.polling(none_stop=True, interval=0)

