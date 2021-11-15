from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask import Flask, request, jsonify
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Resolving Heroku PostgresQL migration error
uri = os.environ['DATABASE_URL']
if uri.startswith('postgres'):
    uri = re.sub(r'^postgres:', 'postgresql:', uri)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Moves


db.init_app(app)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/add')
def add_move():
    move = Moves(request.args['move_id'], request.args['move_name'], request.args['effects'], request.args['damage'], request.args['description'], request.args['stat_changes'])
    try:
        db.session.add(move)
        db.session.commit()
        return 'Move added!'
    except Exception as e:
        return(str(e))

@app.route('getall/')
def get_all():
    try:
        moves = Moves.query.all()
        return jsonify([move.serialize() for move in moves])
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()
