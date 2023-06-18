import telebot
from telebot import types
import datetime
import time
from hh import *
from api_super import get_prof,get_week_su
from token_1 import TOKEN
from api_rf import get_vak,get_week_rf




bot = telebot.TeleBot(TOKEN)

but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
but.add("Вакансии","Что умеешь?",'Список вакансии xlsx','Вакансии_SuperJob','Вакансии_РФ' )

sl_id = {}
sl_menu = {}
sl_iter = {}
sl_city = {}
sl_salary = {}
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

salary = False
salary1 = False
salary2 = False

week = False
week1 = False
week2 = False

week_vak = []
week_vak_rf = []
week_vak_su = []

#Дальше код для отправки каждый понедельник вакансий
def schedule_job(message):
    current_datetime = datetime.datetime.now()
    if current_datetime.weekday() == 4:  
        k = 0
        bot.send_message(message.chat.id, "Привет это рассылка от HH")
        vacancies = week_hh(week_vak[-1][0], week_vak[-1][1], week_vak[-1][2])
        for vacancy in vacancies:
            k += 1
            bot.send_message(message.chat.id, vacancy)
            if k < 20:
                break
        del week_vak[-1]
        
def schedule_job_su(message):
    current_datetime = datetime.datetime.now()
    if current_datetime.weekday() == 5:  
        k = 0
        bot.send_message(message.chat.id, "Привет это рассылка Superjob")
        vacancies = get_week_su(week_vak_su[-1][0], week_vak_su[-1][1], week_vak_su[-1][2])
        for vacancy in vacancies:
            k += 1
            bot.send_message(message.chat.id, vacancy)
            if k>20:
                break
        del week_vak_su[-1]

def schedule_job_rf(message):
    current_datetime = datetime.datetime.now()
    if current_datetime.weekday() == 5: 
        k = 0
        bot.send_message(message.chat.id, "Привет это рассылка от Работа России")
        vacancies = get_week_rf(week_vak_rf[-1][0], week_vak_rf[-1][1], week_vak_rf[-1][2])
        for vacancy in vacancies:
            k+=1
            bot.send_message(message.chat.id, vacancy)
            if k>20:
                break
        del week_vak_rf[-1]

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    global dl_vak, vakansis1, flag1, city1
    global sl_id, vakansis2, flag2, city2
    global sl_menu, salary, salary1, salary2
    global sl_iter, sl_salary
    global but, week, week1, week2, week_vak, week_vak_rf, week_vak_su
    global sl_city
    global masiv
    global city
    global vakansis
    global flag
    if len(week_vak) > 0:
        schedule_job(message)
    if len(week_vak_su) > 0:
        schedule_job_su(message)
    if len(week_vak_rf) > 0:
        schedule_job_rf(message)
    if message.text == "На главную":
        but = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        but.add("Вакансии", "Что умеешь?", 'Список вакансии xlsx', 'Вакансии_SuperJob','Вакансии_РФ')
        sl_menu[message.chat.id] = False
        sl_iter[message.chat.id] = 0
        city1 = False
        salary = False
        salary1 = False
        salary2 = False
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
        bot.send_message(message.from_user.id, "Напишите желаемую должность",
                         reply_markup=types.ReplyKeyboardRemove())        
        vakansis = True
    if message.text != "Вакансии" and vakansis == True:
        if message.text not in['Next=>','На главную', 'Вакансии', "Напишите_город", 'Вакании_SuperJob', 'Вакансии_РФ']: 
            sl_id[message.chat.id] = message.text
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
        bot.send_message(message.from_user.id, "Напишите_заработную_плату",
                         reply_markup=types.ReplyKeyboardRemove())
    if flag == True and message.text != sl_city[message.chat.id]:
        arr_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        check = True
        for i in message.text:
            if i not in arr_check:
                check = False
        if check == True: 
            sl_salary[message.chat.id] = int(message.text)
            masiv.append(message.text)
            flag = False
        if sl_salary.get(message.chat.id)!=None:
            week = True
            bot.send_message(message.from_user.id, "Хотите присылать раз в неделю?(Да/нет)",
                            reply_markup=types.ReplyKeyboardRemove())
        else:
            bot.send_message(message.from_user.id, "Можно писать только цифры",
                            reply_markup=types.ReplyKeyboardRemove())
    if week == True:
        if message.text == "Да":
            mas_week = [sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id]]
            week_vak.append(mas_week)
        if message.text == "Да" or message.text == "Нет":
            salary = True
            week = False
    if salary == True:
        bot.send_message(message.chat.id, "Информация обрабатывается,подождите..",
                         reply_markup=types.ReplyKeyboardRemove())
                
        dl_vak = True
        sl_menu[message.chat.id] = True

        city = False
        
        if sl_iter[message.chat.id] < len(m_hh(sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id])[1]) and len(m_hh(sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id])[1])>0:
            for k in m_hh(sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id])[1][sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
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
            salary = False

    # super job
    
    if message.text == "Вакансии_SuperJob":
        sl_iter[message.chat.id] = 0
        bot.send_message(message.from_user.id, "Напишите желаемую должность",
                         reply_markup=types.ReplyKeyboardRemove())        
        vakansis1 = True

    if message.text != "Вакансии_SuperJob" and vakansis1 == True:
        if message.text not in['Next=>','На главную', 'Вакансии', "Напишите_город", 'Вакании_SuperJob','Вакансии_РФ']: 
            sl_id[message.chat.id] = message.text
        vakansis1 = False
        print('это вакансии',sl_id)
        
        bot.send_message(message.from_user.id, "Напишите_город",
                         reply_markup=types.ReplyKeyboardRemove())
        if sl_id.get(message.chat.id)!=None:
            city1 = True
    if (message.text != sl_id.get(message.chat.id)  and city1 == True):
    
        if message.text not in['Next=>','На главную', 'Вакансии',"Напишите_город",'Вакансии_SuperJob','Вакансии_РФ']: 
            sl_city[message.chat.id] = message.text
        city1 = False
        if sl_city.get(message.chat.id)!=None:
            flag1 = True
        bot.send_message(message.from_user.id, "Напишите_заработную_плату",
                         reply_markup=types.ReplyKeyboardRemove())
    if flag1 == True and message.text != sl_city[message.chat.id]:
        arr_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        check = True
        for i in message.text:
            if i not in arr_check:
                check = False
        if check == True: 
            sl_salary[message.chat.id] = int(message.text)
            masiv.append(message.text)
            flag1 = False
        if sl_salary.get(message.chat.id)!=None:
            week1 = True
            bot.send_message(message.from_user.id, "Хотите присылать раз в неделю?(Да/нет)",
                            reply_markup=types.ReplyKeyboardRemove())
        else:
            bot.send_message(message.from_user.id, "Можно писать только цифры",
                            reply_markup=types.ReplyKeyboardRemove())
    if week1 == True:
        if message.text == "Да":
            mas_week = [sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id]]
            week_vak_su.append(mas_week)
        if message.text == "Да" or message.text == "Нет":
            salary1 = True
            week1 = False
    if salary1 == True:
        bot.send_message(message.chat.id, "Информация обрабатывается,подождите..",
                         reply_markup=types.ReplyKeyboardRemove())
                
        dl_vak = True
        sl_menu[message.chat.id] = True

        city1 = False
    
        if sl_iter[message.chat.id] < len(get_prof(sl_id[message.chat.id], sl_city[message.chat.id],sl_salary[message.chat.id])):
            for k in get_prof(sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id])[sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
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
            salary1 = False
        masiv = []
    # end

    # rf vak
    if message.text == "Вакансии_РФ":
        sl_iter[message.chat.id] = 0
        bot.send_message(message.from_user.id, "Напишите желаемую должность",
                         reply_markup=types.ReplyKeyboardRemove())        
        vakansis2 = True

    if message.text != "Вакансии_РФ" and vakansis2 == True:
        if message.text not in['Next=>','На главную', 'Вакансии', "Напишите_город", 'Вакании_SuperJob','Вакансии_РФ']: 
            sl_id[message.chat.id] = message.text
        vakansis2 = False
        print('это вакансии',sl_id)
        
        bot.send_message(message.from_user.id, "Напишите_регион",
                         reply_markup=types.ReplyKeyboardRemove())
        if sl_id.get(message.chat.id)!=None:
            city2 = True
    if (message.text != sl_id.get(message.chat.id)  and city2 == True):
    
        if message.text not in['Next=>','На главную', 'Вакансии',"Напишите_город",'Вакансии_SuperJob','Вакансии_РФ']: 
            sl_city[message.chat.id] = message.text
        city2 = False
        if sl_city.get(message.chat.id)!=None:
            flag2 = True
        bot.send_message(message.from_user.id, "Напишите_заработную_плату",
                         reply_markup=types.ReplyKeyboardRemove())
    if flag2 == True and message.text != sl_city[message.chat.id]:
        arr_check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        check = True
        for i in message.text:
            if i not in arr_check:
                check = False
        if check == True: 
            sl_salary[message.chat.id] = int(message.text)
            masiv.append(message.text)
            flag2 = False
        if sl_salary.get(message.chat.id)!=None:
            week2 = True
            bot.send_message(message.from_user.id, "Хотите присылать раз в неделю?(Да/нет)",
                            reply_markup=types.ReplyKeyboardRemove())
        else:
            bot.send_message(message.from_user.id, "Можно писать только цифры",
                            reply_markup=types.ReplyKeyboardRemove())
    if week2 == True:
        if message.text == "Да":
            mas_week = [sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id]]
            week_vak_rf.append(mas_week)
        if message.text == "Да" or message.text == "Нет":
            salary2 = True
            week2 = False
    if salary2 == True:
        bot.send_message(message.chat.id, "Информация обрабатывается,подождите..",
                         reply_markup=types.ReplyKeyboardRemove())
                
        dl_vak = True
        sl_menu[message.chat.id] = True

        city2 = False
    
        if sl_iter[message.chat.id] < len(get_vak(sl_id[message.chat.id], sl_city[message.chat.id],sl_salary[message.chat.id])):
            for k in get_vak(sl_id[message.chat.id], sl_city[message.chat.id], sl_salary[message.chat.id])[sl_iter[message.chat.id]:sl_iter[message.chat.id]+5]:
                
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
            salary2 = False
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

bot.polling()
