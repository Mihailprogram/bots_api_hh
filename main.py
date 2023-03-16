import telebot
from telebot import types
from pars import pars_hh
from pathlib import Path
import time
from hh import *
from token_1 import TOKEN



bot = telebot.TeleBot(TOKEN)

but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
but.add("Вакансии","Что умеешь?",'Список вакансии xlsx')

sl_id = {}
sl_menu = {}
sl_iter = {}
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет ты написал мне /start,',reply_markup=but)

# @bot.message_handler(content_types=['photo', 'document'])
# def handler_file(message):
#     Path(f'files/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
#     if message.content_type == 'photo':
#         file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#         src =  file_info.file_path.replace('photos/', '')
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
                
#         word()
#         global file
#         file = True
# next_iter = 0     
# count = 0
# k1=0
num = False
vakansis = False 
# dl_vak = True
masiv = []
# mas_next = []
# massiv_city = []


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    global dl_vak
    global sl_id
    global sl_menu
    global sl_iter
    if message.text == "На главную":
        but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        but.add("Вакансии","Что умеешь?",'Список вакансии xlsx')
        sl_menu[message.chat.id] = False
        sl_iter[message.chat.id] = 0
        dl_vak = False
        bot.send_message(message.chat.id,'Главная', reply_markup=but)

    if message.text == "Next=>":
        # global k1
        # k1+=1
        global next_iter
        sl_iter[message.chat.id] += 5
    
    if message.text == "Что умеешь?":
        sl_iter[message.chat.id] = 0
        bot.send_message(message.from_user.id, "Привет, я умею выдавать вакнсии по одной(для этого выбирете Вакансии) или сразу все exel файлом(Список вакансии xlsx).") 
    if message.text == "Вакансии":
        sl_iter[message.chat.id] = 0
        sl_id[message.chat.id] = 'Sl'
        bot.send_message(message.from_user.id, "Напишите желаемую должность")
        global vakansis
        vakansis = True
        # global dl_vak
        # dl_vak = True
    
    if (message.text!= "Вакансии" and vakansis==True) or sl_iter[message.chat.id]>0:
        global masiv
        
        dl_vak = True
        sl_menu[message.chat.id] = True
        if message.text not in['Next=>','На главную', 'Вакансии'] and message.text not in masiv: 
            sl_id[message.chat.id] = message.text
            masiv.append(message.text)

        vakansis = False
        if sl_iter[message.chat.id] < len(m_hh(sl_id[message.chat.id])[1]) and len(m_hh(sl_id[message.chat.id])[1])>0:
            for k in m_hh(sl_id[message.chat.id])[1][sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
                but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                but.add('')
                bot.send_message(message.chat.id, k, reply_markup=but)
                time.sleep(1)
                if sl_menu[message.chat.id] == False:
                    del sl_id[message.chat.id]
                    sl_iter[message.chat.id] = 0
                    break
            but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            but.add('Next=>', 'На главную')
            bot.send_message(message.chat.id, 'Выбери', reply_markup=but)

            if sl_menu[message.chat.id] == False:
                # del sl_id[message.chat.id]
                sl_iter[message.chat.id] = 0
        else:
            bot.send_message(message.chat.id, 'Этого нет')

    if message.text == "Список вакансии xlsx":
        bot.send_message(message.from_user.id, "Напиши название вакансии")
        global num
        num = True
    if message.text != 'Список вакансии xlsx' and num == True:
        main_hh(message.text)
        doc = open('C:/Users/Химачи/Desktop/Курс/hh.xlsx', 'rb')
        bot.send_document(message.chat.id,doc)
        num = False


bot.polling()
