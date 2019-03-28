import sqlite3

con = sqlite3.connect('Carteira.db')

def create_table():
    con.cursor().execute('CREATE TABLE IF NOT EXISTS moviment (cod integer, mod intenger, valor real, cred real, date text)')

create_table()

def data_entry():
    con.cursor().execute('INSERT INTO moviment VALUES(0, 1 , 0, 0, "09-06-2018 02:55:56")')
    con.commit()

data_entry()
