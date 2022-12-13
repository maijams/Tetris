from database_connection import get_database_connection
from initialize_database import initialize_database
from datetime import date


class ScoreBoard:
    def __init__(self):
        self.database = get_database_connection()

    def save_score(self, points):
        today = date.today().strftime("%d.%m.%Y")
        try:
            self.database.execute(
                "INSERT INTO scoreboard (score, date) VALUES (?, ?)",
                [points, today]
            )
        except:
            initialize_database()
            self.database.execute(
                "INSERT INTO scoreboard (score, date) VALUES (?, ?)",
                [points, today]
            )
        self.database.commit()
        
    
    def get_scoreboard(self):
        return self.database.execute(
            "SELECT * FROM scoreboard ORDER BY score DESC LIMIT 10").fetchall()