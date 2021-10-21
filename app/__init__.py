from flask import Flask
from flask_socketio import SocketIO
from flask_mongoengine import MongoEngine

#create a flask application
web_app = Flask(__name__)
socketio = SocketIO(web_app)
web_app.debug = True

#Load configurations
web_app.config.from_pyfile('config.py')

#Init Mongodb
mongodb = MongoEngine()
mongodb.init_app(web_app)


from .main import main as main_blueprint
web_app.register_blueprint(main_blueprint)
