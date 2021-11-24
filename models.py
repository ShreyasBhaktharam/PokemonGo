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

class Location(db.Model):
    __tablename__ = "location"

    LocationId = db.Column(db.Integer, primary_key=True, unique=True)
    LocationName = db.Column(db.String(30), nullable = False)
    Effects = db.Column(db.String(30))
    SpawnId = db.Column(db.Integer, nullable = False)
    FKPokemonId = db.Column(db.Integer, nullable = False)

    def __repr__(self) -> str:
        return super().__repr__()

    def serialize(self):
        return {
            'LocationId': self.LocationId,
            'LocationName': self.LocationName,
            'Effects': self.Effects,
            'SpawnId': self.SpawnId,
            'FKPokemonId': self.FKPokemonId
        }

        
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'username': self.username,
            'password': self.password
        }
