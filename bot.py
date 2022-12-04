from telebot import types
import telebot
import sqlite3
import open_base_sqlite



res = []

def start_bot():
    bot = telebot.TeleBot('5951587908:AAEYdd-bDYljcxEkunSPgAOAJVRJLOFkR4I')

    
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Показать все контакты')
        item2 = types.KeyboardButton('Добавить контакт')
        item3 = types.KeyboardButton('Удалить контакт')
        item4 = types.KeyboardButton('Поиск по имени')

        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def Controller(message):

        if message.chat.type == 'private':
            if message.text == 'Показать все контакты':
                phone_list = open_base_sqlite.bas_sqlite()
                for i in phone_list:
                    bot.send_message(message.chat.id, i)
                bot.register_next_step_handler(message,Controller)

            if message.text == 'Добавить контакт':
                bot.send_message(message.chat.id, 'Введите имя контакта')
                bot.register_next_step_handler(message, Get_Sirname)


            if message.text == 'Удалить контакт':
                bot.send_message(message.chat.id, 'Введите имя контакта')
                bot.register_next_step_handler(message, Del_Cont)

            if message.text == 'Поиск по имени':
                bot.send_message(message.chat.id, 'Введите имя контакта')
                bot.register_next_step_handler(message, Search_cont)


                

    def Get_Sirname(message):
        name = (message.text)
        global res 
        res.append(name)
        bot.send_message(message.chat.id, 'Введите номер телефона')
        bot.register_next_step_handler(message,Get_Name)




    def Get_Name(message):
        num = (message.text)
        global res
        res.append(num)
        res = [(res[0],res[1])]


        db = sqlite3.connect('base_3.db')
        cur = db.cursor()

        cur.executemany("INSERT INTO guide VALUES(?, ?)", res)
        res = []

        db.commit()
        cur.close()
        db.close()

        bot.send_message(message.chat.id, 'Контакт добавлен')
        bot.register_next_step_handler(message,Controller)



    def Del_Cont(message):
        name = (message.text)

        db = sqlite3.connect('base_3.db')
        cur = db.cursor()
        cur.execute("DELETE FROM guide WHERE surname = ?",(name,))

        db.commit()
        cur.close()
        db.close()

        bot.send_message(message.chat.id, 'Контакт удален')
        bot.register_next_step_handler(message,Controller)



    def Search_cont(message):
        name = (message.text)


        db = sqlite3.connect('base_3.db')
        cur = db.cursor()

        cur.execute("SELECT * FROM guide WHERE surname = ?", (name,))
        people = cur.fetchall()
        
        for i in range(0,len(people)):
            b = people[i][0] + ': ' + people[i][1]

        
            bot.send_message(message.chat.id, f'{b}')
        


        db.commit()
        cur.close()
        db.close()

        bot.register_next_step_handler(message,Controller)






    bot.polling(none_stop=True)