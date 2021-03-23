import telebot
import configure

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(content_types = ['text'])
def get_text(message):
    print(message.text)
    name = message.from_user.first_name

    if message.text.lower() == 'дай мне файл!':
        with open('file.txt', 'rb') as f:
            client.send_document(message.chat.id, data = f)


client.polling(none_stop = True, interval = 0)

