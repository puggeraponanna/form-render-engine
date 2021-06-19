from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
server.config.from_mapping(dotenv_values(".env"))
db = SQLAlchemy(server)

@server.route('/')
def hello():
    return "Hello World!"


if __name__ == "__main__":
    server.run(host='0.0.0.0', debug=server.config.get('DEBUG'))
