from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask import Flask, request
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Resolving Heroku PostgresQL migration error
uri = os.environ['DATABASE_URL']
if uri.startswith('postgres'):
    uri = re.sub(r'^postgres:', 'postgresql:', uri)

os.setenv('DATABASE_URL', uri)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Moves


db.init_app(app)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
