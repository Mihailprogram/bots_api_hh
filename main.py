import telebot
from telebot import types
from pars import pars_hh
from pathlib import Path
import time
from hh import *


from doc import word


bot = telebot.TeleBot('5848488244:AAFhyaydtOyVoTODNP6R4MsBTSs-IpfZQOE')

but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
but.add("Вакансии","Что умеешь?",'Список вакансии xlsx')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет ты написал мне /start,',reply_markup=but)
file = False
@bot.message_handler(content_types=['photo', 'document'])
def handler_file(message):
    Path(f'files/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src =  file_info.file_path.replace('photos/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
                
        word()
        global file
        file = True
             
count = 0
k1=0
num = False
vakansis = False 
# dl_vak = True
masiv = []
mas_next = []
massiv_city = []
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text =="Next=>":
        # global k1
        # k1+=1
        global mas_next
        mas_next.append('next')
        # keyboard = types.InlineKeyboardMarkup()
        # b12 = types.InlineKeyboardButton(text="Вакансии  в Екб", callback_data="a1")
        # keyboard.add(b12)
        # bot.send_message(message.from_user.id, text='Нажмите ', reply_markup=keyboard) 
    if message.text == "Что умеешь?":
        bot.send_message(message.from_user.id, "Привет, я умею выдавать вакнсии по одной(для этого выбирете Вакансии) или сразу все exel файлом(Список вакансии xlsx).") 
    if message.text == "Вакансии":
        bot.send_message(message.from_user.id, "Напишите желаемую должность")
        global vakansis
        vakansis = True
        global dl_vak
        dl_vak = True
    
    if message.text!= "Вакансии" and vakansis==True:
        global masiv
        masiv.append(message.text)
        keyboard = types.InlineKeyboardMarkup()
        b12 = types.InlineKeyboardButton(text="Вакансии  в Екб", callback_data="a0")
        keyboard.add(b12)
        bot.send_message(message.from_user.id, text='Нажмите ', reply_markup=keyboard) 
        vakansis = False
        
    
    if message.text == "Список вакансии xlsx":
        bot.send_message(message.from_user.id, "Напиши название вакансии")
        global num
        num = True
    if message.text!='Список вакансии xlsx' and num==True:
        main_hh(message.text)
        doc = open('C:/Users/Химачи/Desktop/Курс/hh.xlsx','rb')
        bot.send_document(message.chat.id,doc)
        num = False
    if message.text=="На главную":
        dl_vak = False
        bot.send_message(message.chat.id,'Главная',reply_markup=but)

    

@bot.callback_query_handler(func=lambda call: True)
def boter(call):
    global count

    if call.data=='a0':
        # dl_vak = True
        for k in m_hh(masiv[-1])[1]:
            count+=1
            but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            but.add('')
            bot.send_message(call.message.chat.id, k,reply_markup=but)
            time.sleep(1)
            # z2=dl_vak
            # print(z2)
            print(dl_vak)
            z=k1
            if count==3:
                zaebal = False
                count = 0
                but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                but.add('Next=>','На главную')
                bot.send_message(call.message.chat.id,'Выбери,',reply_markup=but)
                time.sleep(2)
                while True:
                    global mas_next
                    if 'next' in mas_next:
                        print(mas_next)
                        mas_next = []
                        break
                    if dl_vak!=True:
                        flag = True
                        break
                if flag == True:
                    break

            
bot.polling()