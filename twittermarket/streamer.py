import tweepy
import config
import subprocess
import time

# twitter's API auth stuff
auth = tweepy.OAuthHandler(config.TwitterDevConfig.consumer_key, config.TwitterDevConfig.consumer_secret)
auth.set_access_token(config.TwitterDevConfig.access_token, config.TwitterDevConfig.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#stream class 
class MyStreamListener(tweepy.StreamListener):
    def on_status (self, status):

        if status.place is None:
            #dont do anything
            i = 0
        
        else:
            
            #get status info and send it to app.py
            tweet = status.text
            tweet = tweet.replace(" ", "_")
            tweet = tweet.replace("!", "~")
            user_name = status.user.name
            user_name = user_name.replace(" ", "_")
            user_screen_name = status.user.screen_name
            user_city = status.place.name
            user_city = user_city.replace(" ", "_")
            
            user_time_requested = str(status.created_at)
            user_time_requested = user_time_requested.replace(" ", "_")
            url = "curl -i -X POST http://localhost:5000/newrequest/{}/{}/{}/{}/{}".format(tweet, user_name, user_screen_name, user_city, user_time_requested)
            subprocess.run(url, shell=True)

#create stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream (auth = api.auth, listener = myStreamListener)
myStream.filter(track = ['!wine'])

#get products that should be filtered
# products = subprocess.run("curl -X GET http://localhost:5000/allproducts", shell=True,capture_output=True)
# products_str = products.stdout.decode('utf-8')

# print(products_str)
