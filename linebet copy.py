import telebot
from telebot import types
from mysql import connector
import json
import datetime
import os
import base64
from LineBet.conf import Database
from conf import bot
from telebot.apihelper import send_message


lang = 'uz'
id_state = ''
pcode = ''
# main menu
gmessage = {}
my_mysql = Database()

# def connect_to_base():
#     mydb = connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="linebet"
#     )
#     return mydb

# def upd_mydata(datas,my_id):
#     global gmessage
#     mydb = my_mysql.Connect()
#     mycursor = mydb.cursor()
#     if (datas == 'uzcard_upd'):
#         sql = f"UPDATE users SET uzcard = '0' WHERE chat_id = '{my_id}'"
#         bot.send_message(my_id,"Sizning carta raqamingiz uchirildi!")
#         #bot.register_next_step_handler(gmessage, add_mycard)
#     elif (datas == '1xbet_upd'):
#         sql = f"UPDATE users SET 1xbet_uz = 0 WHERE chat_id = '{my_id}'"
#         bot.send_message(my_id,"Sizning 1xbet id ingiz uchirildi!")
#         #bot.register_next_step_handler(gmessage, add_1xbet)
#     elif (datas == 'linebet_upd'):
#         sql = f"UPDATE users SET linebet_uz = 0 WHERE chat_id = '{my_id}'"
#         bot.send_message(my_id,"Sizning linebet id ingiz uchirildi!")
#         #bot.register_next_step_handler(gmessage, add_linebet)
#     elif (datas == 'melbet_upd'):
#         sql = f"UPDATE users SET melbet_uz = 0 WHERE chat_id = '{my_id}'"
#         bot.send_message(my_id,"Sizning melbet id ingiz uchirildi!")
#         #bot.register_next_step_handler(gmessage, add_melbet)
#     mycursor.execute(sql)
#     mydb.commit()
    

def secure_rand(len=8):
    token=os.urandom(len)
    return base64.b64encode(token)


def filter(text):
    text = text.lower()
    text = [c for c in text if c in '0123456789 -']
    text = "".join(text) # alfabit harflaridan boshqa simvollarni uchiradi
    if (len(text) > 3):
        return int(text)
    else:
        return 0

def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'qwertyuiopasdfghjklzxcvbnm1234567890 -']
    text = "".join(text) # alfabit harflaridan boshqa simvollarni uchiradi
    return text


def user_add(chatid):
    mydb = my_mysql.Connect()
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
        replenish = types.KeyboardButton("??????????????????????")
        withdraw = types.KeyboardButton("??????????????????")
        instruction = types.KeyboardButton("???? ????????????????????")
        orderkiwi = types.KeyboardButton("????????????????????????????")
        cashback = types.KeyboardButton("???? Cashback")
        mycards = types.KeyboardButton("?????????? ??????????")
        kurs = types.KeyboardButton("???????????? | ??????????????????")
        myreplenish = types.KeyboardButton("?????? ????????????????????")
        callback = types.KeyboardButton("???????????????? ??????????")
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        bot.send_message(message.chat.id,"?????????????? ????????", reply_markup=markup)
    elif(lang == 'uz'):
        replenish = types.KeyboardButton("????Hisobni toldirish")
        withdraw = types.KeyboardButton("????Pul chiqarish")
        instruction = types.KeyboardButton("????Qo'llanma")
        orderkiwi = types.KeyboardButton("????Identifikatsiya")
        cashback = types.KeyboardButton("???? Cashback")
        mycards = types.KeyboardButton("????Hamyonlar")
        kurs = types.KeyboardButton("????Kurs | ????Zahira")
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
        replenish = types.KeyboardButton("??????????????????????")
        withdraw = types.KeyboardButton("??????????????????")
        instruction = types.KeyboardButton("???? ????????????????????")
        orderkiwi = types.KeyboardButton("????????????????????????????")
        cashback = types.KeyboardButton("???? Cashback")
        mycards = types.KeyboardButton("?????????? ??????????")
        kurs = types.KeyboardButton("???????????? | ??????????????????")
        myreplenish = types.KeyboardButton("?????? ????????????????????")
        callback = types.KeyboardButton("???????????????? ??????????")
        
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        markup.row(send_contact)
        bot.send_message(call.from_user.id,"?????????????? ????????", reply_markup=markup)
    elif(lang == 'uz'):
        replenish = types.KeyboardButton("????Hisobni toldirish")
        withdraw = types.KeyboardButton("????Pul chiqarish")
        instruction = types.KeyboardButton("????Qo'llanma")
        orderkiwi = types.KeyboardButton("????Identifikatsiya")
        cashback = types.KeyboardButton("???? Cashback")
        mycards = types.KeyboardButton("????Hamyonlar")
        kurs = types.KeyboardButton("????Kurs | ????Zahira")
        myreplenish = types.KeyboardButton("Tulovlar tarixi")
        callback = types.KeyboardButton("Aloqa")
        send_contact = types.KeyboardButton("Meni nomerim", request_contact=True)
        markup.row(replenish)
        markup.row(withdraw, instruction)
        markup.row(orderkiwi, cashback)
        markup.row(mycards, kurs)
        markup.row(myreplenish, callback)
        markup.row(send_contact)
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
        main       = types.KeyboardButton("?????????????? ????????")
        markup.row(xbet_uz, xbet_ru, linebet_uz)
        markup.row(main)
        bot.send_message(
        message.chat.id, "???????????????? ?????? ????????????????????.", reply_markup=markup)
    if (lang == 'uz'):
        main       = types.KeyboardButton("Asosiy menu")
        markup.row(xbet_uz, xbet_ru, linebet_uz)
        markup.row(main)
        bot.send_message(
        message.chat.id, "To'ldirilayotgan hamyon turini tanlang.", reply_markup=markup)



def get_instruction(message, lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if (lang == 'ru'):
        instruction_out = types.InlineKeyboardButton(
            "??? ?????? ??????????????", callback_data='instruction_out')
        instruction_in = types.InlineKeyboardButton(
            "?????? ?????? ?????????????????? ????????", callback_data='instruction_in')
        main_menu = types.InlineKeyboardButton(
            "?????????????????? ????????", callback_data='main_menu')
        markup.add(instruction_out, instruction_in, main_menu)
        bot.send_message(message.chat.id, "???????????????? ????????????.",
                         reply_markup=markup)
    if (lang == 'uz'):
        instruction_out = types.InlineKeyboardButton(
            "??? Pul chiqarish qanday kerak", callback_data='instruction_out')
        instruction_in = types.InlineKeyboardButton(
            "?????? Hisobni qanday to'ldirish kerak", callback_data='instruction_in')
        main_menu = types.InlineKeyboardButton(
            "????Bosh menu", callback_data='main_menu')
        markup.add(instruction_out, instruction_in, main_menu)
        bot.send_message(message.chat.id, "Savolni tanlang.",
                         reply_markup=markup)


def get_userinfo(message, lang):
    global gmessage
    markup = types.InlineKeyboardMarkup(row_width=2)    
    gmessage = message
    if (lang == 'ru'):
        user_card = types.InlineKeyboardButton(
            "???UZCARD", callback_data='user_uzcard')
        card_upd  = types.InlineKeyboardButton("???",callback_data = 'uzcard_upd')
        user_uzxbet = types.InlineKeyboardButton(
            "???1XBET UZS", callback_data='user_1xuzb')
        uzxbet_upd  = types.InlineKeyboardButton("???",callback_data = '1xbet_upd')
        user_uzline = types.InlineKeyboardButton(
            "???LINEBET UZS", callback_data='user_lineuzb')
        linebet_upd  = types.InlineKeyboardButton("???",callback_data = 'linebet_upd')
        user_uzmelbet = types.InlineKeyboardButton(
            "???MELBET UZS", callback_data='user_melbetuzb')
        melbet_upd  = types.InlineKeyboardButton("???",callback_data = 'melbet_upd')
        markup.add(user_card, card_upd, user_uzxbet, uzxbet_upd, user_uzline, linebet_upd, user_uzmelbet,melbet_upd)
        bot.send_message(message.chat.id, "???????????? ????????????????:",   reply_markup=markup)
    if (lang == 'uz'):
        user_card = types.InlineKeyboardButton(
            "???UZCARD", callback_data='user_uzcard')
        card_upd  = types.InlineKeyboardButton("???",callback_data = 'uzcard_upd')
        user_uzxbet = types.InlineKeyboardButton(
            "???1XBET UZS", callback_data='user_1xuzb')
        uzxbet_upd  = types.InlineKeyboardButton("???",callback_data = '1xbet_upd')
        user_uzline = types.InlineKeyboardButton(
            "???LINEBET UZS", callback_data='user_lineuzb')
        linebet_upd  = types.InlineKeyboardButton("???",callback_data = 'linebet_upd')
        user_uzmelbet = types.InlineKeyboardButton(
            "???MELBET UZS", callback_data='user_melbetuzb')
        melbet_upd  = types.InlineKeyboardButton("???",callback_data = 'melbet_upd')
        markup.add(user_card, card_upd, user_uzxbet, uzxbet_upd, user_uzline, linebet_upd, user_uzmelbet,melbet_upd)
        bot.send_message(
            message.chat.id, "????Sizning hisoblaringiz:", reply_markup=markup)


def get_kursinfo(message, lang):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM kurs ")
    myresult = mycursor.fetchall()
    for item in myresult:
        if (lang == 'ru'):
            if (int(item[11]) == 0):
                bot.send_message(message.chat.id, "???????????? ????????????????????")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)
            else:
                bot.send_message(message.chat.id, "???????????? ????????????")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)

        if (lang == 'uz'):
            if (int(item[11]) == 0):
                bot.send_message(message.chat.id, "????Toldirish kursi")
                msg = "1XBET UZS = "+item[1]+"\n1XBET USD = "+item[3]+"\n1XBET RUB ="+item[2]+"\nLINEBET UZS ="+item[4]+"\nLINEBET RUB = " + \
                    item[5]+"\nLINEBET USD = "+item[6]+"\nMELBET UZS ="+item[7] + \
                    "\nMELBET RUB =" + \
                    item[8]+"\nMELBET USD ="+item[9]+"\nQIWI = "+item[10]
                bot.send_message(message.chat.id, msg)
            else:
                bot.send_message(message.chat.id, "????Chiqarish kursi")
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
            bot.send_message(message.chat.id, "?????????????????? ???????? ???? ????????????????")
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
            bot.send_message(message.chat.id, "???????? ???????????? ??????????????!")

 

def add_mycard(message):
    mycard = filter(message.text)
    if (mycard < 1000000000000000):
        bot.send_message(message.chat.id, "Karta raqamini tekshirib tering 16 raqam bo'lishi kerak!" )
        
    else:
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
    if message.text != "LineBet UZS" or message.text != "1XBET UZS" or message.text != "MelBet UZS":
        get_replenish(message,lang)
    else:
        if (linebet == 0):
            bot.send_message(message.chat.id,"LineBet id ingizda sonlar bo'lishi kerak! \n Iltimos LineBet id ni qaytadan tering! Faqat sonlar bulishi kerak")
            bot.register_next_step_handler(message, add_linebet)
        else:
            sql = f"UPDATE users SET linebet_uz = '{linebet}' WHERE chat_id = {message.from_user.id}"
            mycursor.execute(sql)
            mydb.commit()
            bot.send_message(message.chat.id,"LineBet registratsiyadan muvofaqiyatli utdi!")
        

def add_1xbet(message):
    xbet = filter(message.text)
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    if message.text == "LineBet UZS" or message.text == "1XBET UZS" or message.text == "MelBet UZS":        
        get_replenish(message,lang)
    else:
        if (xbet == 0):
            bot.send_message(message.chat.id,"1XBET id ingizda sonlar ham bo'lishi kerak! \n Iltimos 1XBET id ni qaytadan tering! Faqat sonlar bulishi kerak")
            bot.register_next_step_handler(message, add_1xbet)
        else:
            sql = f"UPDATE users SET 1xbet_uz = {xbet} WHERE chat_id = {message.from_user.id}"
            mycursor.execute(sql)
            mydb.commit()
            bot.send_message(message.chat.id,"1XBET registratsiyadan muvofaqiyatli utdi!")
        

def add_melbet(message):
    xbet = filter(message.text)
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    if message.text != "LineBet UZS" or message.text != "1XBET UZS" or message.text != "MelBet UZS":        
        get_replenish(message,lang)
    else:
        if (xbet == 0):
            bot.send_message(message.chat.id,"MelBet id ingizda sonlar bo'lishi kerak! \n Iltimos MelBet id ni qaytadan tering! Faqat sonlar bulishi kerak")
            bot.register_next_step_handler(message, add_melbet)
        else:
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


def notif_push_list(user_id):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM outpays  p  WHERE p.status = 'new' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    markup = types.InlineKeyboardMarkup(row_width=1)
    for item in myresult:
        markup.add(types.InlineKeyboardButton(f"sizning cartangiz -{item[2]}  \n ariza sanasi -{item[3]} \n  turi - {item[4]} ", callback_data='push'+str(item[0])))
    bot.send_message(user_id, "Pul chiqarilishi kerak bulgan active arizalar!", reply_markup=markup)


def answer_notif(call):
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql = f"UPDATE pays p SET p.status = 'old'  WHERE  p.status = 'new' and p.client_id = {items[1]}"
    mycursor.execute(sql)
    mydb.commit()


def payment(message):
    global id_state
    mydb = connect_to_base()
    mycursor = mydb.cursor()
    sql =f"SELECT * FROM users WHERE chat_id = {message.from_user.id}"
    mycursor.execute(sql)
    mycard = mycursor.fetchone()
    dates = datetime.datetime.now()
    if (message.text == 'Asosiy menu') or (message.text == '?????????????? ????????'):
        main_menu(message,lang)        
    elif filter(message.text) <= 5000 and (message.text == "1XBET UZS" or message.text == "LineBet UZS" or message.text == "MelBet UZS"):
        bot.send_message(message.chat.id,f"Sizni hisobni tuldirish haqidagi murojatingiz bekor qilindi !   \n  minimal summa 5000 \n tip: {id_state} ")
        bot.send_message(message.chat.id, "To'lov summasini kiriting!")
        if (message.text == "1XBET UZS"):            
            id_state = "1XBET UZS"            
        elif (message.text == "LineBet UZS"):            
            id_state = "LineBet UZS"            
        elif (message.text == "MelBet UZS" ):            
            id_state = "MelBet UZS"
        bot.register_next_step_handler(message,payment)
            
        
    else:    
        sql = "INSERT INTO pays (client_card,client_id,name,dates,price) VALUES (%s, %s, %s, %s, %s)"
        val = (str(mycard[2]), str(mycard[1]),id_state,dates.strftime("%Y-%m-%d %H:%M:%S"),message.text)
        mycursor.execute(sql, val)
        mydb.commit()
        
        mydb = connect_to_base()
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM pays  p  WHERE p.status = 'new' and  client_card = {mycard[2]} and client_id = {mycard[1]} order by id desc LIMIT 1 "
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        markup = types.InlineKeyboardMarkup(row_width=1)
        for item in myresult:
            if(id_state == '1XBET UZS'):
                bot.send_message(message.chat.id,f"Sizni hisobni tuldirish haqidagi murojatingiz qabul qilindi! \n summa : {filter(message.text)} tip: {id_state} \n uzcard : {mycard[2]} \n  1XBET - {mycard[5]}")
            elif(id_state == 'MelBet UZS'):
                bot.send_message(message.chat.id,f"Sizni hisobni tuldirish haqidagi murojatingiz qabul qilindi! \n summa : {filter(message.text)} tip: {id_state} \n uzcard : {mycard[2]} \n  MelBEt - {mycard[7]}")
            elif (id_state == 'LineBet UZS'):
                bot.send_message(message.chat.id,f"Sizni hisobni tuldirish haqidagi murojatingiz qabul qilindi! \n summa : {filter(message.text)} tip: {id_state} \n uzcard : {mycard[2]} \n  LineBet - {mycard[3]}")    
            markup.add(types.InlineKeyboardButton("tashladim???", callback_data='s'+str(item[0])))
            markup.add(types.InlineKeyboardButton("bekor qilish???", callback_data='d'+str(item[0])))
            bot.send_message(message.chat.id,f"Pastroqda ko'rsatilgan to'lov summasini PAYME, Click, Apelsin, Zoomrad, Paynet to'lov tizimlaridan biri orqali \n \n  8600140435703799 - hisob raqamiga o'tkazing; \n \n To'lov summasi: {filter(message.text)} UZS To'lov o'tgach ??tashladim????? tugmasini bosing.\n  Sizning buyurtmangiz operator tomonidan ish vaqtida 1 daqiqadan 30 daqiqagacha vaqt ichida ko'rib chiqiladi.",reply_markup=markup)
        


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
        elif (item[3] == 0) and (message.text == "LineBet UZS"):
            bot.send_message(message.chat.id,f"Sizning LineBet id ingiz ro'yxatga olinmagan!")
            id_state = ''
            bot.register_next_step_handler(message,add_linebet)
        elif (message.text == "1XBET UZS") and (item[5] == 0):
            bot.send_message(message.chat.id,f"Sizning 1XBET id ingiz ro'yxatga olinmagan!")
            id_state = ''
            bot.register_next_step_handler(message,add_1xbet)
        elif (message.text == "MelBet UZS") and (item[7] == 0):
            bot.send_message(message.chat.id,f"Sizning MelBet id ingiz ro'yxatga olinmagan!")
            id_state = ''
            bot.register_next_step_handler(message,add_melbet)
        
     
            
                
        


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
    global gmessage
    mycursor = mydb.cursor()
    sql = f"SELECT  * FROM  users WHERE chat_id = {id}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for item in myresult:
        if (state == "user_uzcard"):
            if(len(item[2]) > 1):
                bot.send_message(id,f"Sizning uz card {item[2]} nomeringigz!")
            else:
                bot.send_message(id,f"Sizni karta raqamingiz ruyxatdan o'tmagan!")
                bot.register_next_step_handler(gmessage,add_mycard)
                
        if (state == "user_1xuzb"):
            if (item[5] > 1000):
                bot.send_message(id,f"Sizning 1XBET id {item[5]} nomeringiz")
            else:
                bot.send_message(id,f"Sizni 1XBET id  raqamingiz ruyxatdan o'tmagan!")
                bot.register_next_step_handler(gmessage,add_1xbet)
        if (state == "user_lineuzb"):
            if (item[3] > 1000):
                bot.send_message(id,f"Sizning LineBet id {item[3]} nomeringiz")
            else:
                bot.send_message(id,f"Sizni LineBet id  raqamingiz ruyxatdan o'tmagan!")
                bot.register_next_step_handler(gmessage,add_linebet)
        if (state == "user_melbetuzb"):
            if (item[7] > 1000):
                bot.send_message(id,f"Sizning MelBet id {item[7]} nomeringiz")
            else:
                bot.send_message(id,f"Sizni MelBet id  raqamingiz ruyxatdan o'tmagan!")
                bot.register_next_step_handler(gmessage,add_melbet)

def get_my_push(state,id):
    mydb = connect_to_base()
    global lang
    user_card = ""
    dates = datetime.datetime.now()
    mycursor = mydb.cursor()
    sql = f"SELECT  * FROM  users WHERE chat_id = {id}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for item in myresult:
        if (state == "push_1xuzb"):
            bot.send_message(id,f" Sizni uzcard ingiz {item[2]} \n 1xbet tizimidagi id ingiz- {item[5]}")
        elif (state == "push_lineuzb"):
            bot.send_message(id,f" Sizni uzcard ingiz {item[2]} \n linebet  tizimidagi id ingiz- {item[3]}")
        elif (state == "push_melbetuzb"):
            bot.send_message(id,f" Sizni uzcard ingiz {item[2]} \n melbet  tizimidagi id ingiz- {item[7]}")
        user_card = item[2]
    mycursor = mydb.cursor()
    sql = "INSERT INTO outpays (user_id, user_card, dates, types) VALUES (%s, %s, %s, %s)"
    val = (id, user_card, dates.strftime("%Y-%m-%d %H:%M:%S"),state)
    mycursor.execute(sql, val)
    mydb.commit()
    bot.send_message(id, "Sizni pulni chiqarish haqidagi arizangiz qabul qilindi!")



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
    
def push_many(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if (lang == 'ru'):
        #card_upd  = types.InlineKeyboardButton("???",callback_data = 'uzcard_upd')
        user_uzxbet = types.InlineKeyboardButton(
            "????1XBET UZS", callback_data='push_1xuzb')
        #uzxbet_upd  = types.InlineKeyboardButton("???",callback_data = '1xbet_upd')
        user_uzline = types.InlineKeyboardButton(
            "????LINEBET UZS", callback_data='')
        #linebet_upd  = types.InlineKeyboardButton("???",callback_data = 'linebet_upd')
        user_uzmelbet = types.InlineKeyboardButton(
            "????MELBET UZS", callback_data='push_melbetuzb')
        #melbet_upd  = types.InlineKeyboardButton("???",callback_data = 'melbet_upd')
        markup.add(user_uzxbet, user_uzline, user_uzmelbet)
        bot.send_message(message.chat.id, "???????????? ????????????????:",   reply_markup=markup)
    if (lang == 'uz'):
        #card_upd  = types.InlineKeyboardButton("???",callback_data = 'uzcard_upd')
        user_uzxbet = types.InlineKeyboardButton(
            "????1XBET UZS", callback_data='push_1xuzb')
        #uzxbet_upd  = types.InlineKeyboardButton("???",callback_data = '1xbet_upd')
        user_uzline = types.InlineKeyboardButton(
            "????LINEBET UZS", callback_data='push_lineuzb')
        #linebet_upd  = types.InlineKeyboardButton("???",callback_data = 'linebet_upd')
        user_uzmelbet = types.InlineKeyboardButton(
            "????MELBET UZS", callback_data='push_melbetuzb')
        #melbet_upd  = types.InlineKeyboardButton("???",callback_data = 'melbet_upd')
        markup.add(user_uzxbet, user_uzline, user_uzmelbet)
        bot.send_message(
            message.chat.id, "????Sizning hisoblaringiz:", reply_markup=markup)

    

@bot.message_handler(commands=['start', 'help','pays','push'])
def send_welcome(message):
    global pcode
    if (message.text == '/start'):
        user_add(message.from_user.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        ru = types.InlineKeyboardButton("????????????????????", callback_data='ru')
        uz = types.InlineKeyboardButton("?????????????????? ????????", callback_data='uz')
        #promo = types.InlineKeyboardButton("????????????????", url="https://t.me/LinrBet_Bot?start="+pcode)
        markup.add(ru, uz)
        bot.send_message(message.chat.id, "<em>???????????????? ???????? ????????????????????????</em>")
        bot.send_message(message.chat.id, '<em>Interfeys tilini tanlang</em>', reply_markup=markup)
    elif (message.text == '/pays'):
        norif = [] 
        notif_list(message.chat.id)
    elif (message.text == '/push'):
        notif_push_list(message.chat.id)

        
    
    

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
        my_mysql.upd_mydata(call.data,call.from_user.id)
    elif (call.data == "push_uzcard") or (call.data == "push_1xuzb") or (call.data == "push_lineuzb") or (call.data == "push_melbetuzb"):
        get_my_push(call.data,call.from_user.id)    
    elif (call.data[0] == 'd' or call.data[0] == 's'):
        if (call.data[0] == 's'):
            mid = int(call.data[1::])
            mydb = connect_to_base()    
            mycursor = mydb.cursor()
            sql = f"UPDATE pays SET status = 'suc' WHERE id = {mid}"
            mycursor.execute(sql)
            mydb.commit()
            mygettype = mydb.cursor()
            sql = f"select * from pays where id = {mid}"
            mygettype.execute(sql)
            myresult = mygettype.fetchone()
            if(myresult[6] == "LineBet UZS"):
                sql = f"SELECt p.*, (select linebet_uz from users where chat_id = {mid}) from pays as p WHERE p.status = 'suc' and p.id = {mid}"
            elif(myresult[6] == "1XBET UZS"):
                sql = f"SELECt p.*, (select 1xbet_uz from users where chat_id = {mid}) from pays as p WHERE p.status = 'suc' and p.id = {mid}"
            elif (myresult[6] == "MelBet UZS"):
                sql = f"SELECt p.*, (select melbet_uz from users where chat_id = {mid}) from pays as p WHERE p.status = 'suc' and p.id = {mid}"
            mycursor = mydb.cursor()   
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            mystr = f"??????Sizning buyurtmangiz tekshirish uchun yuborildi:  \n ????{myresult[0]} \n ????{myresult[1]}  \n ??????{myresult[6]} \n ????berish: {myresult[3]} UZS   \n ????olish: {myresult[3]} UZS \n  ????????UZCARD:  8600140435703799 \n ????????{myresult[6]}: {myresult[7]} \n ????Sana: {myresult[4]} \n Almashuv ish vaqtida 1 daqiqadan 30 daqiqagacha vaqt ichida ko'rib chiqiladi.\n ??????Operator to'lov chekini so'rashi mumkin"
            bot.send_message(myresult[2],mystr)  
            
        elif(call.data[0] == 'd'):
            mid = int(call.data[1::])
            mydb = connect_to_base()    
            mycursor = mydb.cursor()
            sql = f"UPDATE pays SET status = 'del' WHERE id = {mid}"
            mycursor.execute(sql)
            mydb.commit()
            bot.send_message(call.from_user.id, "Sizning hisobni to'ldirish bo'yicha murojatingiz bekor qilindi")
            get_menu(call,lang)
    else:
        
        mydb = connect_to_base()    
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
    

    if (message.text == "??????????????????????") or (message.text == "????Hisobni toldirish"):
        get_replenish(message, lang)
    elif (message.text == "????Qo'llanma") or (message.text == "???? ????????????????????"):
        get_instruction(message, lang)
    elif (message.text == "????Hamyonlar") or (message.text == "?????????? ??????????"):
        get_userinfo(message, lang)
    elif (message.text == "????Kurs | ????Zahira") or (message.text == "???????????? | ??????????????????"):
        get_kursinfo(message, lang)
    elif (message.text == '????Identifikatsiya') or (message.text == "????????????????????????????"):
        if (lang == 'ru'):
            bot.send_message(
                message.chat.id, "?????????????? ???????????????????? ???????????? ?? ???????? ??????????????!")
        else:
            bot.send_message(
                message.chat.id, "Passport ma'lumotlaringizni rasm kurinishida junating!")

        bot.register_next_step_handler(message, get_frontend)
    elif (message.text == "???? Cashback"):
        get_cashback(message,lang)
    elif (message.text == "??????????????????") or (message.text == "????Pul chiqarish"""):  
        push_many(message)
    elif (message.text == "1XBET UZS"):
        id_state = "1XBET UZS"
        mydb = connect_to_base()
        mycursor = mydb.cursor()
        sql = f"SELECT  * FROM  users WHERE chat_id = {message.from_user.id}"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for item in myresult:
            if (len(item[2]) < 16):
                bot.send_message(message.chat.id,f"Sizning UZCARD karta raqamingizni kiritmagansiz iltimos kiriting!")
                bot.register_next_step_handler(message,add_mycard)
            elif (item[5] <= 1):
                bot.send_message(message.chat.id,f"Sizning 1XBET id ingiz ro'yxatga olinmagan!")            
                bot.register_next_step_handler(message,add_1xbet)
            else:
                bot.send_message(message.chat.id, "To'lov summasini kiriting!")
                bot.register_next_step_handler(message,payment)
    elif(message.text == "MelBet UZS"):
        id_state = "MelBet UZS"
        mydb = connect_to_base()
        mycursor = mydb.cursor()
        sql = f"SELECT  * FROM  users WHERE chat_id = {message.from_user.id}"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for item in myresult:
            if (len(item[2]) < 16):
                bot.send_message(message.chat.id,f"Sizning UZCARD karta raqamingizni kiritmagansiz iltimos kiriting!")
                bot.register_next_step_handler(message,add_mycard)
            elif (item[7] <= 1):
                bot.send_message(message.chat.id,f"Sizning MelBet id ingiz ro'yxatga olinmagan!")            
                bot.register_next_step_handler(message,add_melbet)
            else:
                bot.send_message(message.chat.id, "To'lov summasini kiriting!")
                bot.register_next_step_handler(message,payment)   
    elif(message.text == "LineBet UZS"):
        id_state = "LineBet UZS"
        mydb = connect_to_base()
        mycursor = mydb.cursor()
        sql = f"SELECT  * FROM  users WHERE chat_id = {message.from_user.id}"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for item in myresult:
            if (len(item[2]) < 16):
                bot.send_message(message.chat.id,f"Sizning UZCARD karta raqamingizni kiritmagansiz iltimos kiriting!")
                bot.register_next_step_handler(message,add_mycard)
            elif(item[3] <= 1):
                bot.send_message(message.chat.id,f"Sizning LineBet id ingiz ro'yxatga olinmagan!")
                bot.register_next_step_handler(message,add_linebet)
            else:
                bot.send_message(message.chat.id, "To'lov summasini kiriting!")
                bot.register_next_step_handler(message,payment)
    elif (message.text == 'Asosiy menu') or (message.text == '?????????????? ????????'):
        main_menu(message,lang)
    else:
        print(message.text)
    #if (lang == "uz"):
    #    bot.send_message(message.chat.id,"1XBET, MELBET, LineBet dagi id nomeringizni kiriting! ")            
    #else:
    #    bot.send_message(message.chat.id,"???????????????? ???? ???? 1XBET, MELBET, LineBet ??!")
    
@bot.message_handler(content_types=['contact'])
def handle_get_contact(message):
    if message.contact is not None: #???????? ???????????????????? ???????????? <strong>contact</strong> ???? ?????????? ????????
        phone = message.contact.phone_number
        user_id = message.contact.user_id
        mydb = connect_to_base()
        mycursor = mydb.cursor()
        mycursor.execute(f"UPDATE users SET number = '{phone}' where chat_id = {user_id}")
        mydb.commit()
        bot.send_message(user_id,"Sizni telefon raqamingiz ruyxatga olindi!")



bot.polling()