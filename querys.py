import sqlite3
from flask import g

def get_user(email, password):
    db = g._database = sqlite3.connect('agenda.db')
    cursor = db.cursor()
    cursor.execute("select * from User where email='" + email + "' and password='" + password + "'")
    user = cursor.fetchall()

    print("foi")
    user_id = user[0][0]

    #if(user):
    #    print("Existe!")
    #    print(user)

    db.commit()
    db.close()
    return user_id

def register_user(name, email, password):
    db = g._database = sqlite3.connect('agenda.db')
    cursor = db.cursor()
    cursor.execute("insert into User (name, email, password, status) values(?, ?, ?, ?)", [name, email, password, 0])

    db.commit()
    db.close()

def get_events(user_id):
    db = g._database = sqlite3.connect('agenda.db')
    cursor = db.cursor()
    cursor.execute("select * from Evento where userID='" + str(user_id) + "'")
    all_data = cursor.fetchall()
    codigos = [str(val[0]) for val in all_data]
    titulos = [str(val[1]) for val in all_data]
    descricoes = [str(val[2]) for val in all_data]
    datas = [str(val[3]) for val in all_data]
    anos = [val[:4] for val in datas]
    meses = [val[5:7] for val in datas]
    dias = [val[8:10] for val in datas]

    db.commit()
    db.close()
    return codigos, titulos, descricoes, anos, meses, dias