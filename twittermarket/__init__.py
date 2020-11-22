from flask import Flask, Response
from twittermarket import config
import mysql.connector
import subprocess
import tweepy

#database connection
db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'lcenci',
    password = 'root',
    database = 'hack_db'
)


# twitter's API auth stuff
auth = tweepy.OAuthHandler(config.TwitterDevConfig.consumer_key, config.TwitterDevConfig.consumer_secret)
auth.set_access_token(config.TwitterDevConfig.access_token, config.TwitterDevConfig.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

mycursor = db.cursor()

def create_app(config_class = config.FlaskConfig):
    app = Flask(__name__)
    app.config.from_object(config.FlaskConfig)
    
    return app