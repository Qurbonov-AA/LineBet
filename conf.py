import telebot
from telebot import types
from mysql import connector



TOKEN = "1778835566:AAGCqelAKbl7DBltGvpOT8pv-4_6lZezS9o"
bot = telebot.TeleBot(TOKEN, parse_mode="html")


class Database():
    
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "linebet"
    
    
    def Connect(self,user,password):
        mydb = connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database
        )
        return mydb

    def upd_mydata(self,datas,my_id):
        mydb = Database.Connect()
        mycursor = mydb.cursor()
        if (datas == 'uzcard_upd'):
            sql = f"UPDATE users SET uzcard = '0' WHERE chat_id = '{my_id}'"
            bot.send_message(my_id,"Sizning carta raqamingiz uchirildi!")
            #bot.register_next_step_handler(gmessage, add_mycard)
        elif (datas == '1xbet_upd'):
            sql = f"UPDATE users SET 1xbet_uz = 0 WHERE chat_id = '{my_id}'"
            bot.send_message(my_id,"Sizning 1xbet id ingiz uchirildi!")
            #bot.register_next_step_handler(gmessage, add_1xbet)
        elif (datas == 'linebet_upd'):
            sql = f"UPDATE users SET linebet_uz = 0 WHERE chat_id = '{my_id}'"
            bot.send_message(my_id,"Sizning linebet id ingiz uchirildi!")
            #bot.register_next_step_handler(gmessage, add_linebet)
        elif (datas == 'melbet_upd'):
            sql = f"UPDATE users SET melbet_uz = 0 WHERE chat_id = '{my_id}'"
            bot.send_message(my_id,"Sizning melbet id ingiz uchirildi!")
            #bot.register_next_step_handler(gmessage, add_melbet)
        mycursor.execute(sql)
        mydb.commit()