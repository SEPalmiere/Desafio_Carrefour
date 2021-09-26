import json
import tweepy
import re
import csv
import operator, functools
from services import get_trends_from_mongo
from authentication import create_api

# Cria uma lista com os endereços indicados nos trends
info=[]
ref = get_trends_from_mongo()
get_value = operator.itemgetter('url')
get_values = functools.partial(map, get_value)
get_values(ref)
info = list(map(operator.itemgetter('url'), ref))
refer = json.loads(json.dumps(info, indent=1))
#print(refer)

#_______________________________________________________________________________________________________________________
get_value = operator.itemgetter('name')
get_values = functools.partial(map, get_value)
get_values(ref)
info2 = list(map(operator.itemgetter('name'), ref))
refer2 = json.loads(json.dumps(info2, indent=1))
#print(refer2)

#_______________________________________________________________________________________________________________

api = create_api()

def get_tweets( hashtag_phrase, api: tweepy.API):
  
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % (fname), 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.get_oembed, q=hashtag_phrase+' -filter:retweets', \
                                   lang="br", tweet_mode='extended').items(50):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])


hashtag_phrase = info[2]

ver = get_tweets(hashtag_phrase, api= api)