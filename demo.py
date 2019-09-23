'''
'''
# Imports the Twitter APIs library
from twython import Twython
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# languages that NL API supports
SUPPORTED_LANGUAGE = ['zh', 'zh-Hant', 'en', 'fr', 'de', 'it',
                      'ja', 'ko', 'pt', 'es', 
                     ]
# Twitter APIs keys

APP_KEY= ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


# Instantiates twitter APIs and google NL API client.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
client = language.LanguageServiceClient()

# program main function begin
while True:
  keyword = input("Please enter a key word you want to search:\n")
  search_result = twitter.search(q=keyword, result_type='popular', include_entities=True)
  # The type of search_result is dict.
  # the first entity is 'statuses'
  statuses = search_result['statuses']  # The type of statuses is list.
  average_attitude = 0
  for status in statuses:  # The type of status is dict.
    tweet_text = status['text']  # The type of tweet_text is string
    tweet_lang = status['lang']  # The type of tweet_lang is string
    print(status['entities'])
    
    if tweet_lang in SUPPORTED_LANGUAGE:
      document = types.Document(
          content=tweet_text,
          language=tweet_lang,
          type=enums.Document.Type.PLAIN_TEXT,
          )

      # Detects the sentiment of the text
      sentiment = client.analyze_sentiment(document=document).document_sentiment
      average_attitude += sentiment.score * sentiment.magnitude

  average_attitude /= len(statuses)
  
  if average_attitude<-0.25:
    print("The average attitude on Twitter about " + keyword + " is negative.")
  elif average_attitude<0.25:
    print("The average attitude on Twitter about " + keyword + " is neutral.")
  else:
    print("The average attitude on Twitter about " + keyword + " is positive.")
