from app import db


class Moves(db.Model):
    __tablename__ = "moves"

    MoveId = db.Column(db.Integer, primary_key=True, unique=True)
    MoveName = db.Column(db.String(20), nullable=False)
    effects = db.Column(db.String(20))
    damage = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(50))
    stat_changes = db.Column(db.String(20))

    def __init__(self, MoveId, MoveName, effects, damage, description, stat_changes):
        self.MoveId = MoveId
        self.MoveName = MoveName
        self.effects = effects
        self.damage = damage
        self.description = description
        self.stat_changes = stat_changes

    def __repr__(self):
        return '<Pokemon %r>' % self.name

    def serialize(self):
        return {
            'MoveId': self.MoveId,
            'MoveName': self.MoveName,
            'effects': self.effects,
            'damage': self.damage,
            'description': self.description,
            'stat_changes': self.stat_changes
        }
