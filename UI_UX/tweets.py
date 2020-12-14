import tweepy
from time import sleep
import json
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.
consumer_key = 'hWhJZSXi52LCwEBy9QoRpvhbG'
consumer_secret = 'bkSWl3WILWilhyQhY5q6XPFUGXZShTMvi8zQNZMSXkyKE9pgBW'
access_token = '4065743119-vlZTgD2C0BNA8XIIVpWHAyUoknWDC2A8RP2S3SJ'
access_token_secret = 'svyX0vR78mfQYMge8MEP1OIX2MaIpJj6MJ3EjdeLlr3FG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!

q ='#mondaythoughts'
f1 = open('tweets_so_far.py', 'a')
f1.write("*" * 100)
#f1.write("\nAccount Name: @AJAY_911AK")
f1.write("\nHashtag :"+q)
f1.write("\nAccount Names:\n")
f1.write("*" * 50+'\n')
for tweet in tweepy.Cursor(api.search, q).items(1):
    try:

        #print('\nRetweet found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
        username = tweet.user.screen_name
        status_list = api.user_timeline(user=username)
        status = status_list[0]
        print(status.text)
        print("-"*60+'\n')
        tweet.retweet()


        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
        #sleep()

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('Retweet failed... ')


    except StopIteration:
        break
