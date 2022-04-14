import telebot
import logging
from check_environs import *
from data import *


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(filename="bot.log")],
    datefmt="%Y-%m-%d %H:%M:%S"
)


bot = telebot.TeleBot(BOT_TOKEN, parse_mode='html')

logging.info(f'bot {BOT_NAME} started')


@bot.message_handler(commands='start')
def answer_start(message):
    bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/UKnaymTb0Qo1DQ', text_commands["start"])
    logging.info(f'START {message.from_user.username} {message.from_user.first_name}')


@bot.message_handler(commands='commands')
def answer_commands(message):
    bot.send_message(message.chat.id, text_commands["commands"])
    logging.info(f'COMMANDS {message.from_user.username} {message.from_user.first_name}')


@bot.message_handler(commands='about')
def answer_about(message):
    bot.send_message(message.chat.id, text_commands["about"])
    logging.info(f'ABOUT {message.from_user.username} {message.from_user.first_name}')


@bot.message_handler(commands='help')
def answer_help(message):
    bot.send_message(message.chat.id, text_commands["help"].format(ADMIN))
    logging.info(f'HELP {message.from_user.username} {message.from_user.first_name}')


@bot.message_handler(commands='englishwords')
def answer_english_words(message):
    nouns = '\n'.join([f'🔻 {noun}' for noun in words['nouns']])
    verbs = '\n'.join([f'🔻 {verb}' for verb in words['verbs']])

    bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/7WG0dU2SrJkdnA',
                   text_commands["english_words"].format(nouns, verbs))
    logging.info(f'ENGLISH WORDS {message.from_user.username} {message.from_user.first_name}')


@bot.message_handler(func=lambda x: True)
def answer_to_all_messages(message):
    translated_message = ''
    for part_of_speech in words:
        for word in words[part_of_speech]:
            if message.text.lower() == word:
                translated_message = f'{dictionary[part_of_speech].title()}: {message.text.lower()}\n' \
                       f'Перевод: {words[part_of_speech][word]}\n\n' \
                       f'Отправьте /englishwords, чтобы посмотреть список слов'
                bot.send_message(message.chat.id, translated_message)
                logging.info(f'TRANSLATED {message.from_user.username} {message.from_user.first_name} {message.text}')
                break
    if not translated_message:
        logging.info(f'RECV {message.from_user.username} {message.from_user.first_name} {message.text}')
        bot.send_message(message.chat.id, text_commands["answer_to_all_messages"].format(message.chat.first_name))


bot.polling(none_stop=True)

logging.error(f'bot {BOT_NAME} finished')
