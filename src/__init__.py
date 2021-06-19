from flask import Flask
from dotenv import dotenv_values
from flask_migrate import Migrate

from .models import JSONFormMaster, database


app = Flask(__name__)
app.config.from_mapping(dotenv_values(".env"))

database.db.init_app(app)
migrate = Migrate(app, database.db)

@app.route('/')
def hello():
    return "Hello World!"



