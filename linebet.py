import telebot
from telebot import types
from mysql import connector
bot = telebot.TeleBot(
    "1778835566:AAGCqelAKbl7DBltGvpOT8pv-4_6lZezS9o", parse_mode="html")

lang = ''
# main menu

mydb = connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="linebet"
)


def user_add(chatid, mydb):

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE chat_id = "+str(chatid))
    myresult = mycursor.fetchall()
    if (len(myresult) == 0):
        sql = "INSERT INTO users (chat_id) VALUES ("+str(chatid)+")"
        mycursor.execute(sql)
        mydb.commit()


def get_menu(call, lang):
    markup = types.ReplyKeyboardMarkup()
    if(lang == 'ru'):
        replenish = types.KeyboardButton("🔄Пополнить")
        withdraw = types.KeyboardButton("Вывести")
        instruction = types.KeyboardButton("📚 Инструкция")
        orderkiwi = types.KeyboardButton("🔖Идитификация")
        cashback = types.KeyboardButton("Cashback")
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
        withdraw = types.KeyboardButton("chiqarish")
        instruction = types.KeyboardButton("📚Qo'llanma")
        orderkiwi = types.KeyboardButton("🔖Identifikatsiya")
        cashback = types.KeyboardButton("Cashback")
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
    markup = types.InlineKeyboardMarkup(row_width=2)
    xbet_uz = types.InlineKeyboardButton(
        "1XBET UZS", callback_data='replenish_1xbet')
    xbet_ru = types.InlineKeyboardButton(
        "MelBet UZS", callback_data='replenish_melbet')
    linebet_uz = types.InlineKeyboardButton(
        "LineBet UZS", callback_data='replanish_linebet')
    markup.add(xbet_uz, xbet_ru, linebet_uz)
    if (lang == 'ru'):
        bot.send_message(
            message.chat.id, "Выберите валюту пополнения.", reply_markup=markup)
    if (lang == 'uz'):
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
    markup = types.InlineKeyboardMarkup(row_width=3)
    if (lang == 'ru'):
        user_card = types.InlineKeyboardButton(
            "➕UZCARD", callback_data='user_uzcard')
        user_uzxbet = types.InlineKeyboardButton(
            "➕1XBET UZS", callback_data='user_1xuzb')
        user_uzline = types.InlineKeyboardButton(
            "➕LINEBET UZS", callback_data='user_lineuzb')
        user_uzmelbet = types.InlineKeyboardButton(
            "➕MELBET UZS", callback_data='user_melbetuzb')
        markup.add(user_card, user_uzxbet, user_uzline, user_uzmelbet)
        bot.send_message(message.chat.id, "🗂Ваши Кошельки:",
                         reply_markup=markup)
    if (lang == 'uz'):
        user_card = types.InlineKeyboardButton(
            "➕UZCARD", callback_data='user_uzcard')
        user_uzxbet = types.InlineKeyboardButton(
            "➕1XBET UZS", callback_data='user_1xuzb')
        user_uzline = types.InlineKeyboardButton(
            "➕LINEBET UZS", callback_data='user_lineuzb')
        user_uzmelbet = types.InlineKeyboardButton(
            "➕MELBET UZS", callback_data='user_melbetuzb')
        markup.add(user_card, user_uzxbet, user_uzline, user_uzmelbet)
        bot.send_message(
            message.chat.id, "🗂Sizning hisoblaringiz:", reply_markup=markup)


def get_kursinfo(message, lang, mydb):
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
    global mydb
    # print(message)
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
    global mydb
    print(message)
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


def user_id_upd(call):
    global mydb
    global lang
    #mycursor = mydb.cursor()
    #sql = "UPDATE users SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    #mycursor.execute(sql)
    #mydb.commit()
    print(call)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    ru = types.InlineKeyboardButton("🇷🇺Руский", callback_data='ru')
    uz = types.InlineKeyboardButton("🇺🇿Ўзбек тили", callback_data='uz')
    markup.add(ru, uz)
    bot.send_message(message.chat.id, "<em>Выберите язык интерфейса💬</em>")
    bot.send_message(message.chat.id, '<em>Interfeys tilini tanlang</em>', reply_markup=markup)
    user_add(message.from_user.id, mydb)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global lang
    if call.data == 'ru':
        lang = 'ru'
        get_menu(call, lang)
    elif call.data == 'uz':
        lang = 'uz'
        get_menu(call, lang)
    elif call.data  == 'replenish_1xbet':
        if (lang == 'uz'):
            bot.send_message(call.from_user.id,"1XBET dagi id nomeringizni kiriting! ")            
        else:
            bot.send_message(call.from_user.id,"Напишите ид из 1XBET а!")            
    elif call.data == 'replenish_melbet':
        if (lang == 'uz'):
            bot.send_message(call.from_user.id,"MELBET dagi id nomeringizni kiriting! ")            
        else:
            bot.send_message(call.from_user.id,"Напишите ид из MELBET а!")             
    elif call.data == 'replanish_linebet':
        if (lang == 'uz'):
            bot.send_message(call.from_user.id,"LINEBET dagi id nomeringizni kiriting! ")            
        else:
            bot.send_message(call.from_user.id,"Напишите ид из LINEBET а!")
    user_id_upd(call) 

@bot.message_handler(content_types=['text'])
def get_text(message):
    if (message.text == "🔄Пополнить") or (message.text == "🔄Hisobni toldirish"):
        get_replenish(message, lang)
    if (message.text == "📚Qo'llanma") or (message.text == "📚 Инструкция"):
        get_instruction(message, lang)
    if (message.text == "🔰Hamyonlar") or (message.text == "🔰Мои счета"):
        get_userinfo(message, lang)
    if (message.text == "📈Kurs | 💰Zahira") or (message.text == "📈Курс | 💰Резервы"):
        get_kursinfo(message, lang, mydb)
    if (message.text == '🔖Identifikatsiya') or (message.text == "🔖Идитификация"):
        if (lang == 'ru'):
            bot.send_message(
                message.chat.id, "Добавте паспортные данные в виде рисунка!")
        else:
            bot.send_message(
                message.chat.id, "Passport ma'lumotlaringizni rasm kurinishida junating!")

        bot.register_next_step_handler(message, get_frontend)


bot.polling()
