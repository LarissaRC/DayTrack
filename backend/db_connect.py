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
    '''
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    '''