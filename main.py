import telebot
from telebot import types
import time
from hh import *
from api_super import get_prof
from token_1 import TOKEN
from api_rf import get_vak




bot = telebot.TeleBot(TOKEN)

but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
but.add("Вакансии","Что умеешь?",'Список вакансии xlsx','Вакансии_SuperJob','Вакансии_РФ' )

sl_id = {}
sl_menu = {}
sl_iter = {}
sl_city = {}
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет ты написал мне /start,',reply_markup=but)





num = False
vakansis = False
city = False
flag = False
masiv = []

vakansis1 = False
flag1 = False
city1 = False 

vakansis2 = False
flag2 = False
city2 = False 
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    global dl_vak, vakansis1, flag1, city1
    global sl_id, vakansis2, flag2, city2
    global sl_menu
    global sl_iter
    global but
    global sl_city
    global masiv
    global city
    global vakansis
    global flag

    if message.text == "На главную":
        but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        but.add("Вакансии", "Что умеешь?", 'Список вакансии xlsx', 'Вакансии_SuperJob','Вакансии_РФ')
        sl_menu[message.chat.id] = False
        sl_iter[message.chat.id] = 0
        city1 = False
        flag = False
        flag1 = False
        flag2 = False
        dl_vak = False
        bot.send_message(message.chat.id, 'Главная', reply_markup=but)

    if message.text == "Next=>":
        global next_iter
        sl_iter[message.chat.id] += 5

    if message.text == "Что умеешь?":
        sl_iter[message.chat.id] = 0
        bot.send_message(message.from_user.id, "Привет, я умею выдавать вакнсии по одной(для этого выбирете Вакансии) или сразу все exel файлом(Список вакансии xlsx).") 
    
    if message.text == "Вакансии":
        sl_iter[message.chat.id] = 0
        sl_id[message.chat.id] = 'Sl'
        bot.send_message(message.from_user.id, "Напишите желаемую должность",
                         reply_markup=types.ReplyKeyboardRemove())        
        vakansis = True

    if message.text != "Вакансии" and vakansis == True:
        if message.text not in['Next=>','На главную', 'Вакансии', "Напишите_город", 'Вакании_SuperJob', 'Вакансии_РФ'] and message.text not in masiv: 
            sl_id[message.chat.id] = message.text
            masiv.append(message.text)
        vakansis = False
        print('это вакансии',sl_id)
        
        bot.send_message(message.from_user.id, "Напишите_город",
                         reply_markup=types.ReplyKeyboardRemove())
        if sl_id.get(message.chat.id)!=None:
            city = True
    if (message.text != sl_id.get(message.chat.id)  and city == True):
    
        if message.text not in['Next=>','На главную', 'Вакансии',"Напишите_город", 'Вакансии_РФ'] and message.text not in masiv : 
            sl_city[message.chat.id] = message.text
            masiv.append(message.text)
        city = False
        if sl_city.get(message.chat.id)!=None:
            flag = True

    if flag == True:
        bot.send_message(message.chat.id, "Информация обрабатывается,подождите..",
                         reply_markup=types.ReplyKeyboardRemove())
                
        dl_vak = True
        sl_menu[message.chat.id] = True

        city = False
        
        if sl_iter[message.chat.id] < len(m_hh(sl_id[message.chat.id], sl_city[message.chat.id])[1]) and len(m_hh(sl_id[message.chat.id], sl_city[message.chat.id])[1])>0:
            for k in m_hh(sl_id[message.chat.id], sl_city[message.chat.id])[1][sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
                but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                but.add('')
                bot.send_message(message.chat.id, k, reply_markup=types.ReplyKeyboardRemove())
                time.sleep(1)
                if sl_menu[message.chat.id] == False:
                    del sl_id[message.chat.id]
                    sl_iter[message.chat.id] = 0
                    break
            but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            but.add('Next=>', 'На главную')
            bot.send_message(message.chat.id, 'Выбери', reply_markup=but)

            if sl_menu[message.chat.id] == False:
                sl_iter[message.chat.id] = 0
        else:
            bot.send_message(message.chat.id, 'Этого нет', reply_markup=but)
            flag = False

    # super job
    
    if message.text == "Вакансии_SuperJob":
        sl_iter[message.chat.id] = 0
        sl_id[message.chat.id] = 'Sl'
        bot.send_message(message.from_user.id, "Напишите желаемую должность",
                         reply_markup=types.ReplyKeyboardRemove())        
        vakansis1 = True

    if message.text != "Вакансии_SuperJob" and vakansis1 == True:
        if message.text not in['Next=>','На главную', 'Вакансии', "Напишите_город", 'Вакании_SuperJob','Вакансии_РФ'] and message.text not in masiv: 
            sl_id[message.chat.id] = message.text
            masiv.append(message.text)
        vakansis1 = False
        print('это вакансии',sl_id)
        
        bot.send_message(message.from_user.id, "Напишите_город",
                         reply_markup=types.ReplyKeyboardRemove())
        if sl_id.get(message.chat.id)!=None:
            city1 = True
    if (message.text != sl_id.get(message.chat.id)  and city1 == True):
    
        if message.text not in['Next=>','На главную', 'Вакансии',"Напишите_город",'Вакансии_SuperJob','Вакансии_РФ'] and message.text not in masiv : 
            sl_city[message.chat.id] = message.text
            masiv.append(message.text)
        city1 = False
        if sl_city.get(message.chat.id)!=None:
            flag1 = True

    if flag1 == True:
        bot.send_message(message.chat.id, "Информация обрабатывается,подождите..",
                         reply_markup=types.ReplyKeyboardRemove())
                
        dl_vak = True
        sl_menu[message.chat.id] = True

        city1 = False
    
        if sl_iter[message.chat.id] < len(get_prof(sl_id[message.chat.id], sl_city[message.chat.id])):
            for k in get_prof(sl_id[message.chat.id], sl_city[message.chat.id])[sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
                but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                but.add('')
                bot.send_message(message.chat.id, k, reply_markup=types.ReplyKeyboardRemove())
                time.sleep(1)
                if sl_menu[message.chat.id] == False:
                    del sl_id[message.chat.id]
                    sl_iter[message.chat.id] = 0
                    break
            but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            but.add('Next=>', 'На главную')
            bot.send_message(message.chat.id, 'Выбери', reply_markup=but)

            if sl_menu[message.chat.id] == False:
                sl_iter[message.chat.id] = 0
        else:
            bot.send_message(message.chat.id, 'Этого нет', reply_markup=but)
            flag1 = False
        masiv = []
    # end

    # rf vak
    if message.text == "Вакансии_РФ":
        sl_iter[message.chat.id] = 0
        sl_id[message.chat.id] = 'Sl'
        bot.send_message(message.from_user.id, "Напишите желаемую должность",
                         reply_markup=types.ReplyKeyboardRemove())        
        vakansis2 = True

    if message.text != "Вакансии_РФ" and vakansis2 == True:
        if message.text not in['Next=>','На главную', 'Вакансии', "Напишите_город", 'Вакании_SuperJob','Вакансии_РФ'] and message.text not in masiv: 
            sl_id[message.chat.id] = message.text
            masiv.append(message.text)
        vakansis2 = False
        print('это вакансии',sl_id)
        
        bot.send_message(message.from_user.id, "Напишите_регион",
                         reply_markup=types.ReplyKeyboardRemove())
        if sl_id.get(message.chat.id)!=None:
            city2 = True
    if (message.text != sl_id.get(message.chat.id)  and city2 == True):
    
        if message.text not in['Next=>','На главную', 'Вакансии',"Напишите_город",'Вакансии_SuperJob','Вакансии_РФ'] and message.text not in masiv : 
            sl_city[message.chat.id] = message.text
            masiv.append(message.text)
        city2 = False
        if sl_city.get(message.chat.id)!=None:
            flag2 = True

    if flag2 == True:
        bot.send_message(message.chat.id, "Информация обрабатывается,подождите..",
                         reply_markup=types.ReplyKeyboardRemove())
                
        dl_vak = True
        sl_menu[message.chat.id] = True

        city2 = False
    
        if sl_iter[message.chat.id] < len(get_vak(sl_id[message.chat.id], sl_city[message.chat.id])):
            for k in get_vak(sl_id[message.chat.id], sl_city[message.chat.id])[sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
                but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                but.add('')
                bot.send_message(message.chat.id, k, reply_markup=types.ReplyKeyboardRemove())
                time.sleep(1)
                if sl_menu[message.chat.id] == False:
                    del sl_id[message.chat.id]
                    sl_iter[message.chat.id] = 0
                    break
            but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            but.add('Next=>', 'На главную')
            bot.send_message(message.chat.id, 'Выбери', reply_markup=but)

            if sl_menu[message.chat.id] == False:
                sl_iter[message.chat.id] = 0
        else:
            bot.send_message(message.chat.id, 'Этого нет', reply_markup=but)
            flag2 = False
        masiv = []
    #end
    if message.text == "Список вакансии xlsx":
        bot.send_message(message.from_user.id, "Напиши название вакансии и город через запятую",
                         reply_markup=types.ReplyKeyboardRemove())
        global num
        num = True

    if message.text != 'Список вакансии xlsx' and num == True:
        xlm_hh = message.text.split(',') 
        main_hh(xlm_hh[0],xlm_hh[1])
        doc = open('C:/Users/Химачи/Desktop/Курс/hh.xlsx', 'rb')
        bot.send_document(message.chat.id, doc, reply_markup=but)
        num = False


# @bot.message_handler(commands=['check_channel'])
# def group(message):
#     channel_id = '1001036240821'
#     user_id = message.from_user.id
    
#     # Получаем информацию о канале
#     channel_info = bot.get_chat(channel_id)
#     print(channel_info)
    
    # Проверяем, есть ли пользователь в списке участников канала
    # if user_id in [member.user.id for member in bot.get_chat_members(channel_id)]:
    #     bot.send_message(message.chat.id, f'Пользователь {message.from_user.username} есть в канале {channel_info.title}')
    # else:
    #     bot.send_message(message.chat.id, f'Пользователь {message.from_user.username} отсутствует в канале {channel_info.title}')


bot.polling()
