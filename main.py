import telebot
from telebot import types
from pars import pars_hh
from pathlib import Path


from doc import word


bot = telebot.TeleBot('5848488244:AAFhyaydtOyVoTODNP6R4MsBTSs-IpfZQOE')

but = telebot.types.ReplyKeyboardMarkup()
but.add("Вакансии","Что умеешь?",'Next=>','документ')



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
             

k1=0
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "Что умеешь?":
        bot.send_message(message.from_user.id, "Привет, я умею выдавать вакнсии.") 
    if message.text == "Вакансии":
        keyboard = types.InlineKeyboardMarkup()
        b12 = types.InlineKeyboardButton(text="Вакансии Python в Екб", callback_data="a0")
        keyboard.add(b12)
        # for i in range(len_mas()):
        #     b13 = types.InlineKeyboardButton(text=f"{i}", callback_data=f"a{i}")
        #     keyboard.add(b13)
        
        bot.send_message(message.from_user.id, text='Выберите номер страницы ', reply_markup=keyboard)
    if message.text =="Next=>":
        global k1
        k1+=1
    if message.text =="документ" and file==True:
        doc = open('C:/Users/Химачи/Desktop/Курс/BDZ.docx','rb')
        bot.send_document(message.chat.id, doc)



count = 0
@bot.callback_query_handler(func=lambda call: True)
def boter(call):
    global count
    if call.data=='a0':
        for k in pars_hh():
             
            count+=1
            bot.send_message(call.message.chat.id, k)
            z=k1
            if count==3 :
                count = 0
                while k1==z:
                    print("Перерыв!")
      
            
    
    
                

bot.polling()