import telebot

bot = telebot.TeleBot('5217047384:AAFlJ1mQ30ET7u8GE2MqXG4A_FNx5JIZkUQ')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    username = message.from_user.username
    msg = f'Кто здесь, {username}'
    bot.send_message(message.from_user.id, msg)

bot.polling()
