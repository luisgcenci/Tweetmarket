import tweepy
import mysql.connector
import io
import json
from twittermarket import create_app, config, mycursor, db, api
from flask import request, Response
import csv
import pandas as pd
import numpy as np
from twittermarket import sentiment
import subprocess
 

app = create_app()


@app.route('/', methods = ['GET', 'POST'])
def home():

    return "home"

#register account
@app.route('/register_account/<string:rusername>/<string:rproduct>/<string:rlocation>', methods = ['POST'])
def register_account(rusername, rproduct, rlocation):
    
    #add user to database table USER
    mycursor.execute("INSERT INTO Users(name, product, location) VALUES ('%s', '%s', '%s')" % (rusername, rproduct, rlocation))
    db.commit()

    #add product to table Products
    mycursor.execute("INSERT INTO Products(product_name) VALUES ('%s')" % (rproduct))
    db.commit()

    return "Account Registered Successfully"


# chart stuff
@app.route('/get_analyze/<string:product>', methods = ['GET'])
def get_analyze_of_product(product):
    
    count = 100
    tweets = api.search(product, count = count)

    tweets_info = []

    for tweet in tweets:
        # tweets_text.append(tweet.text)

        user_id = tweet.user.id
        date_time = str(tweet.created_at)
        user_screen_name = tweet.user.screen_name
        tweet = tweet.text

        row = [user_id, date_time, user_screen_name, tweet]
        tweets_info.append(row)

    df= pd.DataFrame(np.array(tweets_info))
    
    df.to_csv("products.csv", index = False, header = False)
    
    listt = sentiment.run(len(df))
    
    feedback_total = len(listt)
    feedback_positive = 0
    feedback_negative = 0
    feedback_neutral = 0


    for x in listt:
        feedback = x.get('label')
        if feedback == "POSITIVE":
            feedback_positive += 1
        elif feedback == "NEGATIVE":
            feedback_negative +=  1
        elif feedback == "NEUTRAL":
            feedback_neutral += 1

    feedbacks = {}
    feedbacks['positive'] = int( (feedback_positive / feedback_total) * 100)
    feedbacks['negative'] = int( (feedback_negative / feedback_total) * 100)
    feedbacks['neutral'] = int( (feedback_neutral / feedback_total) * 100)

    #detele products.csv
    subprocess.run('rm -r products.csv', shell=True)
        
    return feedbacks


#handles requestes sent by streamer.py
@app.route('/newrequest/<string:tweet_text>/<string:user_name>/<string:user_screen_name>/<string:user_city>/<string:user_time_requested>', methods = ['POST'])
def stream(tweet_text, user_name, user_screen_name, user_city, user_time_requested):
    
    tweet_text = tweet_text.replace("_"," ")
    user_name = user_name.replace("_"," ")
    user_city = user_city.replace("_"," ")
    user_time_requested = user_time_requested.replace("_", " ")
    product_item = ""

    for i in tweet_text.split(' '):
        if(i[0]=='~'):
            if(i.index('~')==len(i)-i[::-1].index('~')-1):
                i = i.replace("~", "")
                product_item = i

    tweet_text = tweet_text.replace("~","!")
    
    mycursor.execute("INSERT INTO Requests(name, username, tweet, product, city, time_requested) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (user_name, user_screen_name, tweet_text, product_item, user_city, user_time_requested))
    db.commit()

    return "Request Sent!"


#returns all products in the database
@app.route('/allproducts', methods = ['GET'])
def all_products():

    mycursor.execute("SELECT * FROM Products")
    allProducts = []
    for x in mycursor:
        allProducts.append(x)

    return Response(json.dumps(allProducts),  mimetype='application/json')


#returns all requests to given suppler
@app.route('/get_requests/<string:product>/<string:location>', methods = ['GET'])
def get_requests(product, location):

    mycursor.execute('SELECT * FROM Requests WHERE product = %s AND city = %s', (product, location))
    allRequests = []

    for x in mycursor:
        allRequests.append(x)

    return Response(json.dumps(allRequests),  mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)












