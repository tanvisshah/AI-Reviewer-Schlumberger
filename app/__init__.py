#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

from flask_session import *

import nltk
nltk.download('wordnet')

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
# SESSION_TYPE = 'filenames'
app.config.from_object('config')

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

Session(app)

login_manager = LoginManager(app)

login_manager.login_view = 'login'



from app import routes
from app import models

