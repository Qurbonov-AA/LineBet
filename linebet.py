import telebot
from telebot import types
from mysql import connector
import json
import datetime
import os
import base64

from telebot.apihelper import send_message
bot = telebot.TeleBot("1778835566:AAGCqelAKbl7DBltGvpOT8pv-4_6lZezS9o", parse_mode="html")

lang = 'uz'
id_state = ''
pcode = ''
# main menu


def connect_to_base():
    mydb = connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="linebet"
    )
    return mydb

def upd_mydata(datas,my_id):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    if (datas == 'uzcard_upd'):
        sql = f"UPDATE users SET uzcard = '0' WHERE chat_id = '{my_id}'"
    elif (datas == '1xbet_upd'):
        sql = f"UPDATE users SET 1xbet_uz = 0 WHERE chat_id = '{my_id}'"
    elif (datas == 'linebet_upd'):
        sql = f"UPDATE users SET linebet_uz = 0 WHERE chat_id = '{my_id}'"
    elif (datas == 'melbet_upd'):
        sql = f"UPDATE users SET melbet_uz = 0 WHERE chat_id = '{my_id}'"
    mycursor.execute(sql)
    mydb.commit()

def secure_rand(len=8):
    token=os.urandom(len)
    return base64.b64encode(token)

def filter(text):
    text = text.lower()
    text = [c for c in text if c in '0123456789 -']
    text = "".join(text) # alfabit harflaridan boshqa simvollarni uchiradi
    return text

def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'qwertyuiopasdfghjklzxcvbnm1234567890 -']
    text = "".join(text) # alfabit harflaridan boshqa simvollarni uchiradi
    return text


def user_add(chatid):
    mydb = connect_to_base()
    global pcode
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE chat_id = "+str(chatid))
    myresult = mycursor.fetchall()
    promo = (secure_rand()).decode('ascii')
    
    if (len(myresult) == 0):
        pcode = filter_text(promo)
        sql = "INSERT INTO users (chat_id,promokod) VALUES ("+str(chatid)+",'"+str(promo)+"')"
        mycursor.execute(sql)
        mydb.commit()
def main_menu(message, lang):
    markup = types.ReplyKeyboardMarkup()
    if(lang == 'ru'):
        replenish = types.KeyboardButton("🔄Пополнить")
        withdraw = types.KeyboardButton("📤Вывести")
        instruction = types.KeyboardButton("📚 Инструкция")
        orderkiwi = types.KeyboardButton("🔖Идитификация")
        cashback = types.KeyboardButton("💸 Cashback")
        mycards = types.KeyboardButton("🔰Мои счета")
        kurs = types.KeyboardButton("📈Курс | 💰Резервы")
        myreplenish = types.KeyboardButton("Мои пополнения")
        callback = types.KeyboardButton("Обратная связь")
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        bot.send_message(message.chat.id,"Главное меню", reply_markup=markup)
    elif(lang == 'uz'):
        replenish = types.KeyboardButton("🔄Hisobni toldirish")
        withdraw = types.KeyboardButton("📤Pul chiqarish")
        instruction = types.KeyboardButton("📚Qo'llanma")
        orderkiwi = types.KeyboardButton("🔖Identifikatsiya")
        cashback = types.KeyboardButton("💸 Cashback")
        mycards = types.KeyboardButton("🔰Hamyonlar")
        kurs = types.KeyboardButton("📈Kurs | 💰Zahira")
        myreplenish = types.KeyboardButton("Tulovlar tarixi")
        callback = types.KeyboardButton("Aloqa")
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        bot.send_message(message.chat.id,"Bosh menu", reply_markup=markup)

def get_menu(call, lang):
    markup = types.ReplyKeyboardMarkup()
    if(lang == 'ru'):
        replenish = types.KeyboardButton("🔄Пополнить")
        withdraw = types.KeyboardButton("📤Вывести")
        instruction = types.KeyboardButton("📚 Инструкция")
        orderkiwi = types.KeyboardButton("🔖Идитификация")
        cashback = types.KeyboardButton("💸 Cashback")
        mycards = types.KeyboardButton("🔰Мои счета")
        kurs = types.KeyboardButton("📈Курс | 💰Резервы")
        myreplenish = types.KeyboardButton("Мои пополнения")
        callback = types.KeyboardButton("Обратная связь")
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        bot.send_message(call.from_user.id,"Главное меню", reply_markup=markup)
    elif(lang == 'uz'):
        replenish = types.KeyboardButton("🔄Hisobni toldirish")
        withdraw = types.KeyboardButton("📤Pul chiqarish")
        instruction = types.KeyboardButton("📚Qo'llanma")
        orderkiwi = types.KeyboardButton("🔖Identifikatsiya")
        cashback = types.KeyboardButton("💸 Cashback")
        mycards = types.KeyboardButton("🔰Hamyonlar")
        kurs = types.KeyboardButton("📈Kurs | 💰Zahira")
        myreplenish = types.KeyboardButton("Tulovlar tarixi")
        callback = types.KeyboardButton("Aloqa")
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        bot.send_message(call.from_user.id,"Bosh menu", reply_markup=markup)

# replenish


def get_replenish(message, lang):
    markup = types.ReplyKeyboardMarkup()
    xbet_uz = types.KeyboardButton(
        "1XBET UZS")
    xbet_ru = types.KeyboardButton(
        "MelBet UZS")
    linebet_uz = types.KeyboardButton(
        "LineBet UZS")    
    
    if (lang == 'ru'):
        main       = types.KeyboardButton("Главная меню")
        markup.row(xbet_uz, xbet_ru, linebet_uz)
        markup.row(main)
        bot.send_message(
        message.chat.id, "Выберите валюту пополнения.", reply_markup=markup)
    if (lang == 'uz'):
        main       = types.KeyboardButton("Asosiy menu")
        markup.row(xbet_uz, xbet_ru, linebet_uz)
        markup.row(main)
        bot.send_message(
        message.chat.id, "To'ldirilayotgan valyuta turini tanlang.", reply_markup=markup)



def get_instruction(message, lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if (lang == 'ru'):
        instruction_out = types.InlineKeyboardButton(
            "❓ Как вывести", callback_data='instruction_out')
        instruction_in = types.InlineKeyboardButton(
            "⁉️ Как пополнить счет", callback_data='instruction_in')
        main_menu = types.InlineKeyboardButton(
            "🔙Главное меню", callback_data='main_menu')
        markup.add(instruction_out, instruction_in, main_menu)
        bot.send_message(message.chat.id, "Выберите вопрос.",
                         reply_markup=markup)
    if (lang == 'uz'):
        instruction_out = types.InlineKeyboardButton(
            "❓ Pul chiqarish qanday kerak", callback_data='instruction_out')
        instruction_in = types.InlineKeyboardButton(
            "⁉️ Hisobni qanday to'ldirish kerak", callback_data='instruction_in')
        main_menu = types.InlineKeyboardButton(
            "🔙Bosh menu", callback_data='main_menu')
        markup.add(instruction_out, instruction_in, main_menu)
        bot.send_message(message.chat.id, "Savolni tanlang.",
                         reply_markup=markup)


def get_userinfo(message, lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if (lang == 'ru'):
        user_card = types.InlineKeyboardButton(
            "➕UZCARD", callback_data='user_uzcard')
        card_upd  = types.InlineKeyboardButton("↪",callback_data = 'uzcard_upd')
        user_uzxbet = types.InlineKeyboardButton(
            "➕1XBET UZS", callback_data='user_1xuzb')
        uzxbet_upd  = types.InlineKeyboardButton("↪",callback_data = '1xbet_upd')
        user_uzline = types.InlineKeyboardButton(
            "➕LINEBET UZS", callback_data='user_lineuzb')
        linebet_upd  = types.InlineKeyboardButton("↪",callback_data = 'linebet_upd')
        user_uzmelbet = types.InlineKeyboardButton(
            "➕MELBET UZS", callback_data='user_melbetuzb')
        melbet_upd  = types.InlineKeyboardButton("↪",callback_data = 'melbet_upd')
        markup.add(user_card, card_upd, user_uzxbet, uzxbet_upd, user_uzline, linebet_upd, user_uzmelbet,melbet_upd)
        bot.send_message(message.chat.id, "🗂Ваши Кошельки:",   reply_markup=markup)
    if (lang == 'uz'):
        user_card = types.InlineKeyboardButton(
            "➕UZCARD", callback_data='user_uzcard')
        card_upd  = types.InlineKeyboardButton("↪",callback_data = 'uzcard_upd')
        user_uzxbet = types.InlineKeyboardButton(
            "➕1XBET UZS", callback_data='user_1xuzb')
        uzxbet_upd  = types.InlineKeyboardButton("↪",callback_data = '1xbet_upd')
        user_uzline = types.InlineKeyboardButton(
            "➕LINEBET UZS", callback_data='user_lineuzb')
        linebet_upd  = types.InlineKeyboardButton("↪",callback_data = 'linebet_upd')
        user_uzmelbet = types.InlineKeyboardButton(
            "➕MELBET UZS", callback_data='user_melbetuzb')
        melbet_upd  = types.InlineKeyboardButton("↪",callback_data = 'melbet_upd')
        markup.add(user_card, card_upd, user_uzxbet, uzxbet_upd, user_uzline, linebet_upd, user_uzmelbet,melbet_upd)
        bot.send_message(
            message.chat.id, "🗂Sizning hisoblaringiz:", reply_markup=markup)


def get_kursinfo(message, lang):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM kurs ")
    myresult = mycursor.fetchall()
    for item in myresult:
        if (lang == 'ru'):
            if (int(item[11]) == 0):
                bot.send_message(message.chat.id, "📉Курс пополнения")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)
            else:
                bot.send_message(message.chat.id, "📉Курс вывода")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)

        if (lang == 'uz'):
            if (int(item[11]) == 0):
                bot.send_message(message.chat.id, "📉Toldirish kursi")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)
            else:
                bot.send_message(message.chat.id, "📉Chiqarish kursi")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)


def get_frontend(message):
    global lang
    mydb = connect_to_base()
    if(message.content_type == 'photo'):
        user = message.from_user.id
        photo_data = message.json["photo"][-1]["file_id"]
        file_info = bot.get_file(photo_data)
        downloaded_file = bot.download_file(file_info.file_path)
        sql = "INSERT INTO imgs (file_id,user_id,status) VALUES (%s,%s,%s)"
        val = (photo_data, user, 'front')
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        with open("img/f"+str(message.chat.id)+".jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        if(lang == 'uz'):
            bot.send_message(
                message.chat.id, "passportni propiska tarafini junating")
        else:
            bot.send_message(message.chat.id, "Отправьте фото от прописки")
        bot.register_next_step_handler(message, get_backend)


def get_backend(message):
    global lang
    mydb =connect_to_base()
    if(message.content_type == 'photo'):
        user = message.from_user.id
        photo_data = message.json["photo"][0]["file_id"]
        file_info = bot.get_file(photo_data)
        downloaded_file = bot.download_file(file_info.file_path)
        sql = "INSERT INTO imgs (file_id,user_id,status) VALUES (%s,%s,%s)"
        val = (photo_data, user, 'backend')
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        with open("img/b"+str(message.chat.id)+".jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        if(lang == 'uz'):
            bot.send_message(
                message.chat.id, "Sizni surovingiz qabul qilindi!")
        else:
            bot.send_message(message.chat.id, "Ваша заявка принято!")

 

def add_mycard(message):
    mycard = filter(message.text)
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"UPDATE users SET uzcard = '{mycard}' WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    mydb.commit()
    bot.send_message(message.chat.id,"UZCARD registratsiyadan muvofaqiyatli utdi!")
        
def add_linebet(message):
    linebet = filter(message.text)
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"UPDATE users SET linebet_uz = '{linebet}' WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    mydb.commit()
    bot.send_message(message.chat.id,"LineBet registratsiyadan muvofaqiyatli utdi!")

def add_1xbet(message):
    xbet = filter(message.text)
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"UPDATE users SET 1xbet_uz = {xbet} WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    mydb.commit()
    bot.send_message(message.chat.id,"1XBET registratsiyadan muvofaqiyatli utdi!")

def add_melbet(message):
    xbet = filter(message.text)
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"UPDATE users SET melbet_uz = {xbet} WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    mydb.commit()
    bot.send_message(message.chat.id,"MelBet registratsiyadan muvofaqiyatli utdi!")


def send_notif(items):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"SELECT p.*,u.linebet_uz,u.promokod,u.1xbet_uz,u.melbet_uz FROM pays p, users u  WHERE  u.chat_id = p.client_id and p.status = 'new' and p.client_id = {items[1]}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        bot.send_message(items[1],f"Karta raqami - {x[1]} \n Summasi - {x[3]} \n murojat yuborilgan sana - {x[4]} \n  Tulov qilinadigan hamyon - {x[6]} ")

    mycursor = mydb.cursor()
    sql = f"SELECT * FROM users WHERE admin = 'admin' "
    mycursor.execute(sql)
    myadmin = mycursor.fetchone()
    for x in myresult:
        bot.send_message(myadmin[1],f"Karta raqami - {x[1]} \n Summasi - {x[3]} \n murojat yuborilgan sana - {x[4]} \n Tulov qilinadigan hamyon - {x[6]}, \n Linebet id - {x[7]} \n 1Xbet id - {x[9]} \n Melbet id - {x[10]} \n promokod user - {x[8]}  ") 
    
def notif_list(user_id):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM pays  p  WHERE p.status = 'new' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    markup = types.InlineKeyboardMarkup(row_width=1)
    for item in myresult:
        markup.add(types.InlineKeyboardButton(f"{item[1]} summa - {item[3]} \n  turi - {item[6]} ", callback_data=item[0]))
    bot.send_message(user_id, "Tulov qilinishi kerak bulgan active tulovlar!", reply_markup=markup)

def answer_notif(call):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"UPDATE pays p SET p.status = 'old'  WHERE  p.status = 'new' and p.client_id = {items[1]}"
    mycursor.execute(sql)
    mydb.commit()


def payment(message):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql =f"SELECT * FROM users WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    mycard = mycursor.fetchone()
    dates = datetime.datetime.now()
    if (int(message.text) < 5000):
        bot.send_message(message.chat.id,f"Sizni hisobni tuldirish haqidagi murojatingiz bekor qilindi ! \n summa : {message.text}  \n  minimal summa 5000 \n tip: {id_state}")
    else:    
        sql = "INSERT INTO pays (client_card,client_id,name,dates,price) VALUES (%s, %s, %s, %s, %s)"
        val = (str(mycard[2]), str(mycard[1]),id_state,dates.strftime("%Y-%m-%d %H:%M:%S"),message.text)
        mycursor.execute(sql, val)
        mydb.commit()
        bot.send_message(message.chat.id,f"Sizni hisobni tuldirish haqidagi murojatingiz qabul qilindi!\n summa : {message.text} \n  tip: {id_state}")
        bot.send_message(message.chat.id,"Quyidagi karta raqamiga tashlab bering  UZCARD 8600140435703799")
        send_notif(mycard)

def get_user(pcode):
    mydb = connect_to_base()    
    mycursor = mydb.cursor()
    sql = f"SELECT  * FROM  users WHERE promokod = '{pcode}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for item in myresult:
        return item[1]
    

    
def user_id_upd(message):
    mydb = connect_to_base()
    global lang
    global id_state
    mycursor = mydb.cursor()
    sql = f"SELECT  * FROM  users WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for item in myresult:
        
        if (len(item[2]) == 1):
            bot.send_message(message.chat.id,f"Sizning UZCARD karta raqamingizni kiritmagansiz iltimos kiriting!")
            bot.register_next_step_handler(message,add_mycard)
        elif (item[3] == 0) and (id_state == "LineBet UZS"):
            bot.send_message(message.chat.id,f"Sizning LineBet id ingiz ro'yxatga olinmagan!")
            id_state = ''
            bot.register_next_step_handler(message,add_linebet)
        elif (id_state == "1XBET UZS") and (item[5] == 0):
            bot.send_message(message.chat.id,f"Sizning 1XBET id ingiz ro'yxatga olinmagan!")
            id_state = ''
            bot.register_next_step_handler(message,add_1xbet)
        elif (id_state == "MelBet UZS") and (item[7] == 0):
            bot.send_message(message.chat.id,f"Sizning MelBet id ingiz ro'yxatga olinmagan!")
            id_state = ''
            bot.register_next_step_handler(message,add_melbet)
        elif (id_state == "LineBet UZS") and (item[3] > 0):
            bot.send_message(message.chat.id,f"LineBet ni tuldirish uchun summani kiriting!")
            bot.register_next_step_handler(message,payment)
        elif (id_state == "MelBet UZS") and (item[5] > 0):
            bot.send_message(message.chat.id,f"MelBet ni tuldirish uchun summani kiriting!")
            bot.register_next_step_handler(message,payment)
        elif (id_state == "1XBET UZS") and (item[7] > 0):
            bot.send_message(message.chat.id,f"1XBET ni tuldirish uchun summani kiriting!")
            bot.register_next_step_handler(message,payment)
        


def push_promo(message):
    mydb = connect_to_base()
    promo = message.text
    user_id = get_user(promo)
    mycursor = mydb.cursor()
    sql = f"UPDATE users SET  link = 'https://t.me/LinrBet_Bot?start={message.text}' WHERE chat_id = '{user_id}'"    
    mycursor.execute(sql)
    mydb.commit()
    mycursor = mydb.cursor()
    dates = datetime.datetime.now()
    sql = "INSERT INTO users_promo (user_id, client_id,dates) VALUES (%s, %s, %s)"
    val = (str(user_id), str(message.from_user.id),dates.strftime("%Y-%m-%d %H:%M:%S"))
    mycursor.execute(sql, val)
    mydb.commit()

def get_my_cash(state,id):
    mydb = connect_to_base()
    global lang
    mycursor = mydb.cursor()
    sql = f"SELECT  * FROM  users WHERE chat_id = {id}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for item in myresult:
        if (state == "user_uzcard"):
            bot.send_message(id,f"Sizning uz card {item[2]} nomeringigz!")
        if (state == "user_1xuzb"):
            bot.send_message(id,f"Sizning 1XBET id {item[5]} nomeringiz")
        if (state == "user_lineuzb"):
            bot.send_message(id,f"Sizning LineBet id {item[3]} nomeringiz")
        if (state == "user_melbetuzb"):
            bot.send_message(id,f"Sizning MelBet id {item[7]} nomeringiz")

def get_cashback(message,lang):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM users where chat_id = {message.chat.id}")
    myresult = mycursor.fetchall()
    for x in myresult:
        if(len(x[6]) < 8):
            bot.send_message(message.chat.id,"qaysi sillka orqali kirdingiz ! Promo code ni kiriting")
            bot.register_next_step_handler(message,push_promo)
        else:
            bot.send_message(message.chat.id,f"Sizni promo codingiz! - {x[6]}")
    
    
    

@bot.message_handler(commands=['start', 'help','pays'])
def send_welcome(message):
    global pcode
    if (message.text == '/start'):
        user_add(message.from_user.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        ru = types.InlineKeyboardButton("🇷🇺Руский", callback_data='ru')
        uz = types.InlineKeyboardButton("🇺🇿Ўзбек тили", callback_data='uz')
        #promo = types.InlineKeyboardButton("Промокод", url="https://t.me/LinrBet_Bot?start="+pcode)
        markup.add(ru, uz)
        bot.send_message(message.chat.id, "<em>Выберите язык интерфейса💬</em>")
        bot.send_message(message.chat.id, '<em>Interfeys tilini tanlang</em>', reply_markup=markup)
    elif (message.text == '/pays'):
        norif = [] 
        notif_list(message.chat.id)
        
    
    

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global lang
    if call.data == 'ru':
        lang = 'ru'
        get_menu(call, lang)
    elif call.data == 'uz':
        lang = 'uz'
        get_menu(call, lang)
    elif (call.data == "user_uzcard") or (call.data =="user_1xuzb") or (call.data == "user_lineuzb") or (call.data == "user_melbetuzb"):
        get_my_cash(call.data,call.from_user.id)
    elif (call.data == 'uzcard_upd') or (call.data =='1xbet_upd') or (call.data == 'linebet_upd') or (call.data == 'melbet_upd'):
        upd_mydata(call.data,call.from_user.id)
    else:
        global mydb    
        mycursor = mydb.cursor()
        sql = f"UPDATE pays SET status = 'old' WHERE id = {call.data}"
        mycursor.execute(sql)
        mydb.commit()        
        bot.send_message(call.from_user.id, 'tulov haqida malumot uzgartirildi ')
        notif_list(call.from_user.id)



@bot.message_handler(content_types=['text'])
def get_text(message):
    global lang
    global id_state 
    if (message.text == "🔄Пополнить") or (message.text == "🔄Hisobni toldirish"):
        get_replenish(message, lang)
    if (message.text == "📚Qo'llanma") or (message.text == "📚 Инструкция"):
        get_instruction(message, lang)
    if (message.text == "🔰Hamyonlar") or (message.text == "🔰Мои счета"):
        get_userinfo(message, lang)
    if (message.text == "📈Kurs | 💰Zahira") or (message.text == "📈Курс | 💰Резервы"):
        get_kursinfo(message, lang)
    if (message.text == '🔖Identifikatsiya') or (message.text == "🔖Идитификация"):
        if (lang == 'ru'):
            bot.send_message(
                message.chat.id, "Добавте паспортные данные в виде рисунка!")
        else:
            bot.send_message(
                message.chat.id, "Passport ma'lumotlaringizni rasm kurinishida junating!")

        bot.register_next_step_handler(message, get_frontend)
    if (message.text == "💸 Cashback"):
        get_cashback(message,lang)
    if (message.text == "1XBET UZS") or (message.text == "MelBet UZS") or (message.text == "LineBet UZS"):
        if (message.text == "1XBET UZS"):
            id_state = "1XBET UZS"
        elif(message.text == "MelBet UZS"):
            id_state = "MelBet UZS"
        elif(message.text == "LineBet UZS"):
            id_state = "LineBet UZS"
        if (lang == "uz"):
            bot.send_message(message.chat.id,"1XBET, MELBET, LineBet dagi id nomeringizni kiriting! ")            
        else:
            bot.send_message(message.chat.id,"Напишите ид из 1XBET, MELBET, LineBet а!")
        bot.register_next_step_handler(message,user_id_upd)
    if (message.text == 'Asosiy menu') or (message.text == 'Главная меню'):
        main_menu(message,lang)
        

#bot.remove_webhook()

bot.polling()

