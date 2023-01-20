import sqlite3
import pathlib
import db_creation

def db_connect():
    PATH_DB = "agenda.db"


    def _path_to_uri(path):
        path = pathlib.Path(path)
        if path.is_absolute():
            return path.as_uri()
        return 'file:' + urllib.parse.quote(path.as_posix(), safe=':/')
    try:
        print(_path_to_uri(PATH_DB))
        check_db_exist = sqlite3.connect(_path_to_uri(PATH_DB)+"?mode=rw", uri=True)
        print("db connected")
        check_db_exist.close()
    except sqlite3.OperationalError:
        db_creation.create_db()


    connection = sqlite3.connect(PATH_DB)
    cursor = connection.cursor()


    DB = {
        "connection": connection,
        "cursor":cursor,
    }

    return DB