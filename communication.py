from twython import Twython
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Twitter API: return a list of tweets and their attributes
# Input: dict{"main_keyword":, "restriction":}
# Output: list(dict{"lang":, "text":, 
# 					"entities":{"hashtag":, media":({"media_url":, "url":, "expanded_url": }), ...},
#					"retweet_count":, "favorite_count":})
def search_keyword(keyword_dic):
	twitter_list = []
	#Instantiates twitter APIs
	APP_KEY= ''
	APP_SECRET = ''
	OAUTH_TOKEN = ''
	OAUTH_TOKEN_SECRET = ''
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	SUPPORTED_LANGUAGE = ['zh', 'zh-Hant', 'en', 'fr', 'de', 'it',
                      'ja', 'ko', 'pt', 'es', 
                     ]
	keyword = keyword_dic["main_keyword"] + ' "' + keyword_dic["restriction"] +'"'
	
	search_result = twitter.search(q=keyword, result_type = 'recent', count = 100, include_entities = True)

	statuses =search_result['statuses'] # The type of statuses is list.
	for status in statuses:
		content={}
		content['lang'] = status['lang']
		if content['lang'] in SUPPORTED_LANGUAGE:
			content["text"] = status['text']
			content["entities"] = status['entities']
			content["retweet_count"] = status['retweet_count'] # return int
			content["favorite_count"] = status['favorite_count'] #return integer or Nullable
			twitter_list.append(content)
	return twitter_list


# Google API
def keyword_sentiment():
	client = language.LanguageServiceClient()
	document = types.Document(
          content=tweet_text,
          language=tweet_lang,
          type=enums.Document.Type.PLAIN_TEXT,
          )
	# Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

if __name__ == '__main__':
	keyword_dic={'main_keyword': 'jhope', 'restriction': 'bts'}
	twitter_list= search_keyword(keyword_dic)
	
	for i in range(len(twitter_list)):
		print(twitter_list[i])
		print('\n')
	print(len(twitter_list))


