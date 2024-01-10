import os
from dotenv import load_dotenv
basdir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basdir, '.env'))

class Config():
    '''
		Set config variables for the flask app
        using Environment variables where available.
        Otherwise create the config variable if not done already
    '''
	

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'whatever'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basdir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False 

