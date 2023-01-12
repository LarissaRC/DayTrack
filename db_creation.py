import sqlite3

connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()

cursor.execute("create table User (userId INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, password text, status integer)")
cursor.execute("create table Evento (eventoId INTEGER PRIMARY KEY AUTOINCREMENT, title text, description text, data text, userID integer, FOREIGN KEY(userID) references User(userID))")

'''
Status possíveis:
- 0 - Inativo (logado)
- 1 - Ativo (deslogado)
- 2 - Conta deletada
'''
users = [
    ("Larissa Rock", "larissa@gmail.com", "123456", 0),
    ("Duquesa", "duquesa@gmail.com", "654321", 0)
]

cursor.executemany("insert into User (name, email, password, status) values (?,?,?,?)", users)

cursor.execute("select userId from User")
result_search = cursor.fetchall()
id1 = result_search[0][0]
id2 = result_search[1][0]

eventos = [
    ("Passeio no parque", "Passeio no parque de tarde com os meus amigos :)", "2023-01-20 16:00:00.000", id1),
    ("Reunião da faculdade", "Reunião com os membros da minha equipe para dividir as tarefas", "2023-02-03 09:30:00.000", id1),
    ("Atividade de MPS", "Entregar o diagrama de arquitetura.", "2023-03-13 18:15:00.000", id2),
    ("Apresentação de Redes", "Apresentação sobre o protocolo TCP.", "2023-01-10 16:20:00.000", id2),
    ("Aniversário da mamãe", "Festa na casa da vovó, não esquecer o bolo!", "2023-02-04 20:00:00.000", id2)
]

cursor.executemany("insert into Evento (title, description, data, userId) values (?,?,?,?)", eventos)

connection.commit()
connection.close()