LOGGER_FORMAT = "%(asctime)s %(levelname)s %(message)s"
LOGGER_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
START_IMAGE_URL = "https://disk.yandex.ru/i/UKnaymTb0Qo1DQ"

text_commands = {
    "start": "Привет! Этот бот создан для изучения **английского языка**\n\n"
             "Нажмите **/englishwords**, чтобы перейти к изучению\n\n**/commands** — команды бота",
    "commands": "команды бота:\n\n**/start** — начать общение с ботом\n**/englishwords** — список английских слов\n"
                "**/about** — информация о боте\n\nИзучайте английский вместе с ботом @english_edu_bot!",
    "about": "Телеграм бот для изучения английских слов.\n\n**/commands** — команды бота",
    "english_words": "Список слов, которые вы можете изучить:\n\nnouns:\n{}\n\nverbs:\n{}\n\n"
                     "Чтобы узнать перевод слова, отправьте мне английское слово из данного списка.\n\n"
                     "**/commands** — команды бота",
    "default": "{}, я не много вас не понял, возможно вы ввели слово, которого нет в моём словаре\n\n"
               "**/englishwords** — английские слова для изучения\n**/commands** — команды бота",
}

words = {
    "verbs": {
        "feel": "чувствовать",
        "eat": "кушать",
        "drink": "пить",
        "go": "идти",
        "have": "иметь",
        "do": "делать",
        "bring": "приносить",
        "breath": "дышать",
        "forget": "забывать",
        "put": "класть",
        "leave": "оставлять",
        "turn off": "выключать",
        "lead": "вести",
        "introduce": "представить",
        "disappear": "исчезать",
        "achieve": "достигать",
    },
    "nouns": {
        "city": "город",
        "country": "страна",
        "street": "улица",
        "rock": "скала",
        "mountain": "гора",
        "land": "земля",
        "insect": "насекомое",
        "union": "объединение",
        "leisure time": "досуг",
    },
}

dictionary = {
    "verbs": "глагол",
    "nouns": "существительное"
}
