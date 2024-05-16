import sqlite3 as sq
def create_data_base():
    with sq.connect("Database/weather.db") as con:
       cur = con.cursor() # возвращает экземплял класса
       cur.execute('''DROP TABLE IF EXISTS users''')  # удаление таблицы
       cur.execute(f'''CREATE TABLE users (
       city TEXT NOT NULL, 
       temp TEXT NOT NULL, 
       wind FlOAT NOT NULL, 
       pressure FLOAT NOT NULL, 
       humidity FLOAT NOT NULL, 
       description TEXT NOT NULL
       )''')

def data_base_update(info):
    with sq.connect("Database/weather.db") as con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO users VALUES(\'{info[0]}\', \'{info[1]}\', {info[2]}, {info[3]}, {info[4]}, \'{info[5]}\')')