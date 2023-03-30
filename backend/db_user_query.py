import mysql.connector
from mysql.connector import Error

config = {
  'user': 'MPS',
  'password': '#LClc03092002',
  'host': 'localhost',
  'database': 'mps_db',
  'raise_on_warnings': True
}

def get_connection():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection

    except Error as e:
        print("Error while connecting to MySQL", e)
        return False

def add_user(data):
    cnx = get_connection()

    if(get_connection != False):
        cursor = cnx.cursor()

        add_user = ("INSERT INTO agenda_user "
                    "(user_name, user_email, user_password, user_status) "
                    "VALUES (%s, %s, %s, %s)")

        data_user = data

        # Insert new user
        cursor.execute(add_user, data_user)

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()

#add_user(('Jucimar', 'jucimar@gmail.com', '123456', 0))

def verify_user_email(data):
    cnx = get_connection()

    if(get_connection != False):
        cursor = cnx.cursor()

        query = ("SELECT user_id FROM agenda_user WHERE user_email = '{}'".format(data))

        cursor.execute(query)
        
        user_id = None
        for id in cursor:
            user_id = id[0]
        
        if user_id is None:
            print("Email inexistente!")
        else:
            print("Email existe! Email pertence ao id " + str(user_id))

        cnx.commit()

        cursor.close()
        cnx.close()

        return user_id

#verify_user_email(("lala@gmail.com"))

def verify_user_password(id, password):
    cnx = get_connection()

    if(get_connection != False):
        cursor = cnx.cursor()

        query = ("SELECT user_name FROM agenda_user WHERE user_password = '{}' AND user_id = {}".format(password, id))

        cursor.execute(query)
        
        user_name = None
        for name in cursor:
            user_name = name[0]
        
        if user_name is None:
            print("Senha incorreta!")
        else:
            print("Senha correta! Dono da conta: " + str(user_name))

        cnx.commit()

        cursor.close()
        cnx.close()

        return user_name

def get_user_name(id):
    cnx = get_connection()

    if(get_connection != False):
        cursor = cnx.cursor()

        query = ("SELECT user_name FROM agenda_user WHERE  user_id = {}".format(id))

        cursor.execute(query)
        
        user_name = None
        for name in cursor:
            user_name = name[0]

        cnx.commit()

        cursor.close()
        cnx.close()

        return user_name

#verify_user_password(1, "111111")

def change_user_status(id, status):
    cnx = get_connection()

    if(get_connection != False):
        cursor = cnx.cursor()

        query = ("UPDATE agenda_user SET user_status = {} WHERE user_id = {}".format(status, id))

        cursor.execute(query)

        cnx.commit()

        cursor.close()
        cnx.close()

#change_user_status(1, 1)

def get_user_events(id, showAllEvents):
    cnx = get_connection()

    if(get_connection != False):
        cursor = cnx.cursor()

        query = ("SELECT *"
                 "FROM agenda_event WHERE user_id = {}".format(id))

        cursor.execute(query)

        events = []
        for event in cursor:
            events.append(event)
        
        if len(events) == 0:
            print("Usuário não possui eventos!")
        
        return events

        cnx.commit()

        cursor.close()
        cnx.close()

#get_user_events(1, True)