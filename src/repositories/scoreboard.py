from datetime import date
import sqlite3
from database_connection import get_database_connection
from initialize_database import initialize_database


class ScoreBoard:
    '''Class that handles database related functions.'''

    def __init__(self, db_name):
        '''Class constructor that creates new database connection.'''

        self._database = get_database_connection(db_name)
        self._db_name = db_name

    def save_score(self, points):
        '''Saves game score & current date to database.

        If database doesn't exist, new database is initialized.

        Args:
            points: Current game score.
        '''

        today = date.today().strftime("%d.%m.%Y")
        try:
            self._database.execute(
                "INSERT INTO scoreboard (score, date) VALUES (?, ?)",
                [points, today]
            )
        except sqlite3.Error:
            initialize_database(self._db_name)
            self._database.execute(
                "INSERT INTO scoreboard (score, date) VALUES (?, ?)",
                [points, today]
            )
        self._database.commit()

    def get_scoreboard(self):
        '''Get top 10 high score.

        Return:
            SQL query result for top 10.
        '''
        try:
            return self._database.execute(
                "SELECT * FROM scoreboard ORDER BY score DESC LIMIT 10").fetchall()
        except sqlite3.OperationalError:
            return None
