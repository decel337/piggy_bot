import telebot
from telebot import types

bot = telebot.TeleBot('5501768689:AAEI_E347nwJ-lLVgSSvGwtt_8pMpv6cZgw')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        markup_inline = types.InlineKeyboardMarkup()
        item_interesting_story = types.InlineKeyboardButton(text='Хочу увлекательную историю о нас',
                                                            callback_data='interesting_story')
        item_fairy = types.InlineKeyboardButton(text='Хочу сказку на ночь!',
                                                            callback_data='fairy')
        item_fairy = types.InlineKeyboardButton(text='Хочу сказку на ночь!',
                                                callback_data='fairy')
        item_sad = types.InlineKeyboardButton(text='Мне грустно(', callback_data='sad')
        item_happy = types.InlineKeyboardButton(text='Мне весело, хочу тебя послушать!', callback_data='happy')

        markup_inline.add(item_sad, item_happy)

        bot.send_message(message.chat.id, 'Хрюник, как твое настроение?', reply_markup=markup_inline)

@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == 'sad':
        audio = open(r'data/voice_26-06-2022_16-46-42.oga', 'rb')
        bot.send_voice(call.message.chat.id, audio)
        audio.close()
        bot.answer_callback_query(callback_query_id=call.id)


bot.polling(none_stop=True, interval=0)