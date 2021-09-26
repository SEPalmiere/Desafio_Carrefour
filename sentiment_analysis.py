import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from textblob import TextBlob
import re

nlp = spacy.load('pt_core_news_md')

texto= " "

doc = nlp(texto)

def clean_tweet(self, tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

def get_sentiment(self, tweet):
        # call TextBlob api to calculate sentiment with cleaned tweet data
        analysis = TextBlob(self.clean_tweet(tweet))
        # if sentiment is greater than 0, it is positive
        if analysis.sentiment.polarity > 0:
            return 'Positivo'
        # if sentiment is 0, it is neutral
        elif analysis.sentiment.polarity == 0:
            return 'Neutro'
        # if sentiment is less than 0, it is negative
        else:
            return 'Negativo'

for sent in doc.sents:
    print(sent)