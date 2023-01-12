import sqlite3

connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()

op = -1
id = -1

while op != 4:
    print("------------------------------")
    print("01 - Ver tabela User")
    print("02 - Ver tabela Eventos")
    print("03 - Ver os eventos de um usuário")
    print("04 - Sair")

    op = int(input())

    print("------------------------------")

    if op == 1:
        cursor.execute("select * from User")
        result_search = cursor.fetchall()
        for row in result_search:
            print(row)
    if op == 2:
        cursor.execute("select * from Evento")
        result_search = cursor.fetchall()
        for row in result_search:
            print(row)
    if op == 3:
        id = int(input("Insira o id do usuário: "))
        cursor.execute("select * from Evento where userId=" + str(id))
        result_search = cursor.fetchall()
        for row in result_search:
            print(row)

connection.commit()
connection.close()