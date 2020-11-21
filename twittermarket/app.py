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

# twitter's API auth stuff
# auth = tweepy.OAuthHandler(config.TwitterDevConfig.consumer_key, config.TwitterDevConfig.consumer_secret)
# auth.set_access_token(config.TwitterDevConfig.access_token, config.TwitterDevConfig.access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)


# # for tweet in tweets:
# #     print(tweet.text)
# tweets = api.user_timeline(user_id = user.id, count = 4)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return "home"

#register account
@app.route('/register_account/<string:rusername>/<string:rproduct>/<string:rlocation>', methods = ['POST'])
def register_account(rusername, rproduct, rlocation):
    
    #add user to database table USER
    mycursor.execute("INSERT INTO Users(username, product, location) VALUES ('%s', '%s', '%s')" % (rusername, rproduct, rlocation))
    db.commit()

    #add product to table Products
    mycursor.execute("INSERT INTO Products(product_name) VALUES ('%s')" % (rproduct))
    db.commit()

    return "Account Registered Successfully"


# login auth stuff
# @app.route('/login_auth/<string:lemail>/<string:lpassword>', methods = ['POST'])
# def auth_login(lemail, lpassword):

#     # q = "SELECT * FROM USER WHERE email = {} AND password = {}".format(lemail, lpassword)

#     mycursor.execute('SELECT * FROM Users WHERE email = %s AND password = %s', (lemail, lpassword,))
    
#     for x in mycursor:
#         return str(x)
#     # string = "name: {}, username {}, email {}, password {}, product {}, location {}".format(name, username, email, password, product, location)

#     return 'hey'


#chart stuff
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

    #detele products.csv
    subprocess.run('rm -r products.csv', shell=True)

    return Response(json.dumps(listt),  mimetype='application/json')

    #send to machine learning module
    #get results back
    #send back to front end

    # return Response(json.dumps(tweets_text),  mimetype='application/json')


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

    
    mycursor.execute("INSERT INTO Requests(name, username, tweet, product, city, time_requested) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (user_name, user_screen_name, tweet_text, product_item, user_city, user_time_requested))
    db.commit()

    return "Request Sent"


#returns all products in the database
@app.route('/allproducts', methods = ['GET'])
def all_products():

    mycursor.execute("SELECT * FROM Products")
    allProducts = []
    for x in mycursor:
        allProducts.append(x)

    return Response(json.dumps(allProducts),  mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)

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

#the good stuff
# user = api.get_user('guilhermecenci5')
# tweets = api.user_timeline(user_id = user.id)

# for tweet in tweets:
#     print(tweet.text)










#database stuff


# mycursor = db.cursor()

# # mycursor.execute("CREATE DATABASE hack_db")
##mycursor.execute("CREATE TABLE User(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(60), username VARCHAR(20), email VARCHAR(120), password VARCHAR(60), product VARCHAR(20), city VARCHAR(20)")


# # 

# # mycursor.execute("DROP TABLE Tweet")
# # mycursor.execute("DESCRIBE Tweet")

# # for x in mycursor:
# #     print(x)

# # for x in mycursor:
# #     print(x)





# print(user.screen_name)




#SEARCH


# 



# for tweet in tweets:

#     # tweet_text = tweet.text
#     # #insert data into database
#     # tweet_text = tweet_text.replace("'","")
#     print(tweet.text)
#     mycursor.execute("""INSERT INTO Tweet(tweet_text) VALUES('%s')""" % (tweet_text))
#     db.commit()

# mycursor.execute("SELECT * FROM Tweet")

# for x in mycursor:
#     print(x)



# # filename = 'pic.png'
# # file = Image.open(filename)

# api.media_upload(filename = filename, file = file)

#SEND DMs
# user = api.get_user('____raff____')
# user_id = user.id

# api.send_direct_message(recipient_id = user_id, text = "Hey yo, this message was sent using Twitter's API")



# mycursor.execute("SELECT * FROM Tweet")

# for x in mycursor:
#     print(x)












