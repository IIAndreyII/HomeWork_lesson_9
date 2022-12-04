import sqlite3



db = sqlite3.connect('base_3.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS guide(
    surname text,
    phone text
)""")

c.execute("INSERT INTO guide (surname, phone) VALUES('Сергеев', '+7(903)123-45-67')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Иванов', '+7(921)654-87-42')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Петров', '+7(987)345-56-19')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Глазова', '+7(435)543-26-19')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Громова', '+7(803)321-54-67')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Глазова', '+7(876)345-76-19')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Пушкин', '+7(999)123-32-56')")
c.execute("INSERT INTO guide (surname, phone) VALUES('Фёдоров', '+7(234)546-83-67')")


db.commit()


c.close()
db.close()