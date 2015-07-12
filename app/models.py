from app import db

class FirstWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word1 = db.Column(db.String(30))
    word2 = db.Column(db.String(30))

    def __repr__(self):
        return '<Word1: %r, Word2: %r>' % (self.word1, self.word2)

class SecondWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word1 = db.Column(db.String(30))
    word2 = db.Column(db.String(30))

    def __repr__(self):
        return '<Word1: %r, Word2: %r>' % (self.word1, self.word2)
