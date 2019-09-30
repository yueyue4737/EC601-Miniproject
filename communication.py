import time
import re
# Import the twython library for Twitter APIs
from twython import Twython
from twython import TwythonError
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

COUNT = 100

# filter the tweet text to delete the hash tag, urls, etc.
def filter(text):
	text = re.sub('RT \@+\w+\:','',text) #delete head of retweet
	text = re.sub('\#+\w+\s','',text)     #delete hashtag
	text = re.sub('https://t.co/+\w+.','',text)  #delete url
	text = re.sub('\@+\w+(\\n|\s)','',text)    #delete @people	
	text = re.sub('\n','',text)                #delete \n
	return text

# return a list of tweets and their attributes
# Param:keywords=[keyword1,keyword2...];
# Twitter API
def search_keyword(keyword_dic, function_name):
	twitter_list = []
	hash_list = []
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
	
	try:
		results = twitter.cursor(twitter.search, q=keyword, result_type = 'recent'
								, count = COUNT, include_entities = True)
		if function_name == 'keyword_sentiment':
			MAX_TWEETS = 30
		elif function_name == 'picture_list':
			MAX_TWEETS = COUNT * 10
		else:
			print("wrong function name")
		for idx, status in enumerate(results):  # 'results' is a generator. It yields tweet objects
			if idx < MAX_TWEETS:
				#print(idx)
				content={}
				content['lang'] = status['lang']
				hashValue = hash(status["text"])  #if texts are identical, hash value is same
				flag = False
				if function_name == 'keyword_sentiment':
					flag = content['lang'] in SUPPORTED_LANGUAGE
				elif function_name == 'picture_list':
					flag = (content['lang'] in SUPPORTED_LANGUAGE) and ('media' in status['entities'])
				else:
					print("wrong function name.")
				if flag:
					if (hashValue not in hash_list) : #or (content["hash"] in twitter_list and content['text'] not in twitter_list)
						hash_list.append(hashValue)
						content["text"] = filter(status['text'])
						content["entities"] = status['entities']
						content["retweet_count"] = status['retweet_count'] # return int
						content["favorite_count"] = status['favorite_count'] #return integer or Nullable
						twitter_list.append(content)
			else:
				break
	except TwythonError as e:
		if e.error_code == 429:
			print("Too many requests!")
		else:
			print(e.error_code)
		# print("begin sleep for 15 minutes. Please wait...")
		# time.sleep(60 * 15)
		# print("wake up!")

	return twitter_list


# Google API
def keyword_sentiment(tweet_dict):
	client = language.LanguageServiceClient()
	document = types.Document(
		content=tweet_dict["text"],
		language=tweet_dict["lang"],
		type=enums.Document.Type.PLAIN_TEXT,
		)
	# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment
	return sentiment.score, sentiment.magnitude

if __name__ == '__main__':
	keyword_dic={'main_keyword': 'jhope', 'restriction': 'bts'}
	twitter_list= search_keyword(keyword_dic, 'keyword_sentiment')
	
	# for i in range(len(twitter_list)):
	# 	print(twitter_list[i])
	# 	print('\n')
	print(len(twitter_list))
