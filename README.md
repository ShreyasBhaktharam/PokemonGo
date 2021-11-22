# PokemonGo
A simple web app demonstrating the working of a PostgresQL database as part of the Database Management Systems course - UE19CS301 at PES University

## Installation
Ensure you have Python 3 installed and package manager ```pip``` installed

Run the following command to install the required packages via ```pip```:
```
pip install -r requirements.txt
```

Define the following environment variables to configure the server:
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL= <your-postgresql-database-url>
```

Finally once all the packages are installed, run the server locally:
```
flask run
```

### Bonus
Website hosted on heroku:
```
https://pokemongo-db.herokuapp.com/
```