import mysql.connector
from db_connect import get_connection

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