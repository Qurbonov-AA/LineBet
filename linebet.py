import telebot
from telebot import types
from mysql import connector
bot = telebot.TeleBot("1778835566:AAGCqelAKbl7DBltGvpOT8pv-4_6lZezS9o",parse_mode="html")

lang = ''
#main menu

def user_add(chatid):

    mydb = connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="linebet"
    )
    mycursor = mydb.cursor()    
    mycursor.execute("SELECT * FROM users WHERE chat_id = "+str(chatid))
    myresult = mycursor.fetchall()
    if (len(myresult) == 0 ):
        sql = "INSERT INTO users (chat_id) VALUES ("+str(chatid)+")"
        mycursor.execute(sql)
        mydb.commit()





def get_menu(call,lang):
    markup = types.ReplyKeyboardMarkup()
    if(lang == 'ru'):
        replenish     = types.KeyboardButton("🔄Пополнить")
        withdraw      = types.KeyboardButton("Вывести")
        instruction   = types.KeyboardButton("📚 Инструкция")
        orderkiwi     = types.KeyboardButton("Обмен QIWI")
        cashback      = types.KeyboardButton("Cashback")
        mycards       = types.KeyboardButton("🔰Мои счета")
        kurs          = types.KeyboardButton("Курс | Резервы")
        myreplenish   = types.KeyboardButton("Мои пополнения")
        callback      = types.KeyboardButton("Обратная связь")
        markup.row(replenish)        
        markup.row(withdraw,instruction)
        markup.row(orderkiwi,cashback)
        markup.row(mycards,kurs)
        markup.row(myreplenish,callback)        
        bot.send_message(call.message.chat.id, "Главное меню", reply_markup=markup)
    if(lang == 'uz'):
        replenish     = types.KeyboardButton("🔄Hisobni toldirish")
        withdraw      = types.KeyboardButton("chiqarish")
        instruction   = types.KeyboardButton("📚Qo'llanma")
        orderkiwi     = types.KeyboardButton("QIWI ayrboshlash")
        cashback      = types.KeyboardButton("Cashback")
        mycards       = types.KeyboardButton("🔰Hamyonlar")
        kurs          = types.KeyboardButton("Kurs | Zahira")
        myreplenish   = types.KeyboardButton("Tulovlar tarixi")
        callback      = types.KeyboardButton("Aloqa")
        markup.row(replenish)
        markup.row(withdraw,instruction)
        markup.row(orderkiwi,cashback)
        markup.row(mycards,kurs)
        markup.row(myreplenish,callback)
        bot.send_message(call.message.chat.id, "Bosh menu", reply_markup=markup)

# replenish

def get_replenish(message,lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    xbet_uz = types.InlineKeyboardButton("1XBET UZS", callback_data = 'replenish_uzs')
    xbet_ru = types.InlineKeyboardButton("1XBET RUB", callback_data = 'replenish_rub')
    linebet_uz = types.InlineKeyboardButton("LineBet UZS", callback_data = 'linebet_uzs')
    markup.add(xbet_uz,xbet_ru,linebet_uz)
    if (lang == 'ru'):
        bot.send_message(message.chat.id,"Выберите валюту пополнения.", reply_markup = markup)        
    if (lang == 'uz'):
        bot.send_message(message.chat.id,"To'ldirilayotgan valyuta turini tanlang.",reply_markup = markup)
        


def get_instruction(message,lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if (lang == 'ru'):
        instruction_out = types.InlineKeyboardButton("❓ Как вывести", callback_data = 'instruction_out')
        instruction_in  = types.InlineKeyboardButton("⁉️ Как пополнить счет", callback_data = 'instruction_in')
        main_menu       = types.InlineKeyboardButton("🔙Главное меню", callback_data = 'main_menu')
        markup.add(instruction_out,instruction_in,main_menu)
        bot.send_message(message.chat.id,"Выберите вопрос.", reply_markup = markup)      
    if (lang == 'uz'):
        instruction_out = types.InlineKeyboardButton("❓ Pul chiqarish qanday kerak", callback_data = 'instruction_out')
        instruction_in  = types.InlineKeyboardButton("⁉️ Hisobni qanday to'ldirish kerak", callback_data = 'instruction_in')
        main_menu       = types.InlineKeyboardButton("🔙Bosh menu", callback_data = 'main_menu')
        markup.add(instruction_out,instruction_in,main_menu)
        bot.send_message(message.chat.id,"Savolni tanlang.", reply_markup = markup)
    
         

def get_userinfo(message,lang):
    markup = types.InlineKeyboardMarkup(row_width=3)
    if (lang == 'ru'):
        user_card         = types.InlineKeyboardButton("➕UZCARD", callback_data = 'user_uzcard')
        user_ruxbet       = types.InlineKeyboardButton("➕1XBET RUB", callback_data = 'user_1xrub')
        user_uzxbet       = types.InlineKeyboardButton("➕1XBET UZS", callback_data = 'user_1xuzb')
        user_ruline       = types.InlineKeyboardButton("➕LINEBET RUB", callback_data = 'user_linerub')
        user_uzline       = types.InlineKeyboardButton("➕LINEBET UZS", callback_data = 'user_lineuzb')
        user_rumelbet     = types.InlineKeyboardButton("➕MELBET RUB", callback_data = 'user_melbetrub')
        user_uzmelbet     = types.InlineKeyboardButton("➕MELBET UZS", callback_data = 'user_melbetuzb')
        markup.add(user_card,user_ruxbet,user_uzxbet,user_ruline,user_uzline,user_rumelbet,user_uzmelbet)
        bot.send_message(message.chat.id,"🗂Ваши Кошельки:", reply_markup = markup)      
    if (lang == 'uz'):
        user_card         = types.InlineKeyboardButton("➕UZCARD", callback_data = 'user_uzcard')
        user_ruxbet       = types.InlineKeyboardButton("➕1XBET RUB", callback_data = 'user_1xrub')
        user_uzxbet       = types.InlineKeyboardButton("➕1XBET UZS", callback_data = 'user_1xuzb')
        user_ruline       = types.InlineKeyboardButton("➕LINEBET RUB", callback_data = 'user_linerub')
        user_uzline       = types.InlineKeyboardButton("➕LINEBET UZS", callback_data = 'user_lineuzb')
        user_rumelbet     = types.InlineKeyboardButton("➕MELBET RUB", callback_data = 'user_melbetrub')
        user_uzmelbet     = types.InlineKeyboardButton("➕MELBET UZS", callback_data = 'user_melbetuzb')
        markup.add(user_card,user_ruxbet,user_uzxbet,user_ruline,user_uzline,user_rumelbet,user_uzmelbet)
        bot.send_message(message.chat.id,"🗂Sizning hisoblaringiz:", reply_markup = markup)
    
     


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    ru = types.InlineKeyboardButton("🇷🇺Руский", callback_data='ru')
    uz = types.InlineKeyboardButton("🇺🇿Ўзбек тили", callback_data='uz')
    markup.add(ru, uz)
    bot.send_message(message.chat.id, "<em>Выберите язык интерфейса💬</em>")
    bot.send_message(message.chat.id, '<em>Interfeys tilini tanlang</em>',reply_markup=markup)               
    user_add(message.from_user.id)  





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global lang
    if call.data == 'ru':
        lang = 'ru'
        get_menu(call,lang)
        
    if call.data == 'uz':
        lang = 'uz'
        get_menu(call,lang)
    
        


@bot.message_handler(content_types=['text'])
def get_text(message):
    if (message.text == "🔄Пополнить") or (message.text == "🔄Hisobni toldirish"): 
        get_replenish(message,lang)
    if (message.text == "📚Qo'llanma") or (message.text == "📚 Инструкция"):
        get_instruction(message,lang)
    if (message.text == "🔰Hamyonlar") or (message.text == "🔰Мои счета"):
        get_userinfo(message,lang)
   
    


bot.polling()
