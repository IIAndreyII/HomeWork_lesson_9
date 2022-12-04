import sqlite3


# def bas_sqlite():
#     db = sqlite3.connect('base_3.db')
#     cur = db.cursor()
#     cur.execute("SELECT * FROM guide")

#     tab_bas_sqlite = []

#     rows = cur.fetchall()
#     for row in rows:
#         tab_bas_sqlite.append(row)

#     cur.close()
#     db.close()

#     return tab_bas_sqlite

# # print(bas_sqlite())

def bas_sqlite():
    db = sqlite3.connect('base_3.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM guide")

    tab_bas_sqlite = []

    rows = cur.fetchall()
    for row in rows:
        c = row[0]+': '+row[1]
        tab_bas_sqlite.append(c)

    cur.close()
    db.close()

    return tab_bas_sqlite

