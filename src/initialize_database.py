from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS scoreboard;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE scoreboard (
            score int,
            date text
        );
    ''')

    connection.commit()


def initialize_database(db_name):
    connection = get_database_connection(db_name)

    drop_tables(connection)
    create_tables(connection)
