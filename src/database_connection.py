import os
import sqlite3


def get_database_connection(db_name):
    dirname = os.path.dirname(__file__)
    connection = sqlite3.connect(os.path.join(dirname, "..", "data", db_name))
    connection.row_factory = sqlite3.Row

    return connection
