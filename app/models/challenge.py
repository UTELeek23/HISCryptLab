

from app import db

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False, default=1)
    answer = db.Column(db.String(500), nullable=False)
    solved = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50), nullable=False)

    def __init__(self, name, difficulty):
        if difficulty < 1 or difficulty > 5:
            raise ValueError("Difficulty must be between 1 and 5")
        self.name = name
        self.difficulty = difficulty