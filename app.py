from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, request
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Moves


db.init_app(app)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
