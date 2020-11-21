import tweepy
import config
import subprocess
import time 

# twitter's API auth stuff
auth = tweepy.OAuthHandler(config.TwitterDevConfig.consumer_key, config.TwitterDevConfig.consumer_secret)
auth.set_access_token(config.TwitterDevConfig.access_token, config.TwitterDevConfig.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = api.search('wine', count = 30000, lan = 'en')

# for tweet in tweets:
#     user_id = tweet.user.id
#     user_date = tweet.created_at
#     user_name = tweet.user.name
#     tweet_text = tweet.text
    
#     print (tweet_text)
    
    


# tweets = api.search('covid', count = 1)

# for x in tweets:
#     print(x.flag)

# user = api.get_user('guilhermecenci5')

# users = [user.id]

# api.list_timeline(list_id = users)
# tweets = api.search('wine', count = 10)
# product = 'wine'
# user = api.get_user('guilhermecenci5')
# listt = api.lists_all(user_id = user.id)

# for x in listt:
#     tweets = api.list_timeline(list_id = x.id)

#     for tweet in tweets:
#         print (tweet.text)

class MyStreamListener(tweepy.StreamListener):
    def on_status (self, status):

        if status.place is None:
            #dont do anything
            i = 1
        
        else:
        
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


myStreamListener = MyStreamListener()
myStream = tweepy.Stream (auth = api.auth, listener = myStreamListener)
myStream.filter(track = ['!wine', '!fruits', '!chocolates'])




# tweets = api.user_timeline(user_id = user.id)

# tweets = api.search(product, count = 5)
# string_match = "!{}".format(product)

# for tweet in tweets:
    
#     if tweet.text == string_match:
#         print('match found : {}'.format(tweet.text))
#     else:
#         print(tweet.text)
