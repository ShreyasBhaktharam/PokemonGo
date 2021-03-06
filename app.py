from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Resolving Heroku PostgresQL migration error
uri = os.environ['DATABASE_URL']
if uri.startswith('postgres'):
    uri = re.sub(r'^postgres:', 'postgresql:', uri)
    

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Location, Moves, User


db.init_app(app)


@app.route('/')
def hello():
    return 'Hello Pokemon!'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            username = request.form.get('username')
            password = request.form.get('password')
            #password_hash = generate_password_hash(password)
            user = User.query.filter_by(username=username).first()

            if user:
                if user.password == password:
                    return jsonify({'message': 'Your login was successful!'})
                else:
                    return jsonify({'message': 'Invalid password'})
            new_user = User(username=username, password=password)
            #Check if user is created
            if new_user:
                print('created')
                db.session.add(new_user)
                db.session.commit()
                return jsonify({'You\'re signed in!'})
            else:
                return jsonify({'message': 'User already exists please try again'})
   
        except Exception as e:
            return jsonify({'error': str(e)})
    return render_template('login.html')
    
    

@app.route('/add', methods=['POST'])
def add_move():
    move_id = request.args.get('MoveId')
    move_name = request.args.get('MoveName')
    effects = request.args.get('effects')
    damage = request.args.get('damage')
    description = request.args.get('description')
    stat_changes = request.args.get('stat_changes')
    

    try:
        move = Moves(MoveId = move_id, MoveName=move_name, effects=effects, damage=damage, description=description, stat_changes=stat_changes)
        db.session.add(move)
        db.session.commit()
        return 'Move added!'
    except Exception as e:
        return(str(e))

@app.route('/getPokemon')
def get_all():
    try:
        moves = Moves.query.all()
        return jsonify([move.serialize() for move in moves])
    except Exception as e:
        return(str(e))

@app.route('/getLocation')
def get_location():
    try:
        location = Location.query.all()
        return jsonify([location.serialize() for location in location])
    except Exception as e:
        return(str(e))

@app.route('/getLocation/id=<LocationId>')
def get_location_id(LocationId):
    try:
        location = Location.query.filter_by(LocationId=LocationId).first()
        return jsonify(location.serialize())
    except Exception as e:
        return jsonify('That location does not exist!')

@app.route('/getPokemon/id=<PokemonId>')
def get_pokemon_id(PokemonId):
    try:
        pokemon = Moves.query.filter_by(MoveId=PokemonId).first()
        return jsonify(pokemon.serialize())
    except Exception as e:
        return jsonify('That pokemon does not exist!')




@app.route('/add/move', methods=['GET', 'POST'])
def add_move_form():
    if request.method == 'POST':
        move_id = request.form.get('MoveId')
        move_name = request.form.get('name')
        effects = request.form.get('effects')
        damage = request.form.get('damage')
        description = request.form.get('description')
        stat_changes = request.form.get('stat_changes')
        try:
            move = Moves(MoveId = move_id, MoveName=move_name, effects=effects, damage=damage, description=description, stat_changes=stat_changes)
            db.session.add(move)
            db.session.commit()
            return 'Move added!'
        except Exception as e:
            return(str(e))
    return render_template('add_move.html')

if __name__ == '__main__':
    app.run()