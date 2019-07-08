import requests
import telebot
from bs4 import BeautifulSoup

bot = telebot.TeleBot('859071138:AAGbzXZ7cSfrQdUMxjaKBOA20VY7i_WgzbM');
headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    }


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, you wrote me a command: /start')
    bot.send_message(message.chat.id, 'I ma a bot which find for you any query in Google search!')
    bot.send_message(message.chat.id, 'Enter a command: /google')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'For search enter a command: /google ')


@bot.message_handler(commands=['google'])
def message_search(message):
    send = bot.send_message(message.chat.id, 'Enter the query!')
    bot.register_next_step_handler(send, output_result)


def output_result(message):
    for i in range(10):
        bot.send_message(message.chat.id, 'Website number: ' + str(i+1))
        bot.send_message(message.chat.id, google(message.text)[i])
        i += 1


def google(query):
    query = '+'.join(query.split())
    url = 'https://www.google.com/search?q=' + query
    output = []
    output_save = ifLenSmaller10(url, output)
    if len(output_save) == 10:
        return output
    if len(output_save) < 10:
        url += '&start=10'
        return ifLenSmaller10(url, output_save)


def ifLenSmaller10(url, output):
    session = requests.Session()
    request = session.get(url, headers=headers_Get)
    soup = BeautifulSoup(request.text, "html.parser")
    for search in soup.find_all('div', {'class': 'r'}):
        url = search.find('a')["href"]
        output.append(url)
    return output


bot.polling(none_stop=True, interval=0)

