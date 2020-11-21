from flask import Flask, Response
from flask_bcrypt import Bcrypt
from twittermarket import config
import mysql.connector
import subprocess
import tweepy

#database connection
db = mysql.connector.connect(
    host = 'localhost',
    user = 'lcenci',
    password = 'root',
    database = 'hack_db'
)


# twitter's API auth stuff
auth = tweepy.OAuthHandler(config.TwitterDevConfig.consumer_key, config.TwitterDevConfig.consumer_secret)
auth.set_access_token(config.TwitterDevConfig.access_token, config.TwitterDevConfig.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

bcrypt = Bcrypt()
mycursor = db.cursor()

def create_app(config_class = config.FlaskConfig):
    app = Flask(__name__)
    app.config.from_object(config.FlaskConfig)

    #encryption
    bcrypt.init_app(app)

    # login_manager.init_app(app)
    # mail.init_app(app)

    # from flaskblog.users.routes import users
    # from flaskblog.posts.routes import posts
    # from flaskblog.main.routes import main
    # from flaskblog.errors.handlers import errors
    
    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    # app.register_blueprint(main)
    # app.register_blueprint(errors)
    
    return app