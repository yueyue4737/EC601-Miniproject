from twython import Twython
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# Regular expression operations in Perl
import re 

COUNT = 100

# return a list of tweets and their attributes
# Param:keywords=[keyword1,keyword2...];
# Twitter API
def search_keyword(keyword_dic):
	twitter_list = []
	#Instantiates twitter APIs
	APP_KEY= '9pvkwqpcmqsoIpi7N2S2EYifT'
	APP_SECRET = 'mPyCOwlFfThkOcoNqs9CAZOQ4xfzg2WhiYH337Zf0olR9kdUyt'
	OAUTH_TOKEN = '1172962292217999360-1lz5v2VcMjffkI1ZMfKEkJ5w1OuIer'
	OAUTH_TOKEN_SECRET = 'MtmCnea4BFTIKuPuFhn9g4Z5axjSoNgFg57LO3dLScio0'
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	SUPPORTED_LANGUAGE = ['zh', 'zh-Hant', 'en', 'fr', 'de', 'it',
					'ja', 'ko', 'pt', 'es', 
					]
	keyword = keyword_dic["main_keyword"] + ' "' + keyword_dic["restriction"] +'"'
	
	search_result = twitter.search(q=keyword, result_type = 'recent', count = COUNT, include_entities = True)

	statuses =search_result['statuses'] # The type of statuses is list.
	for status in statuses:
		content={}
		content['lang'] = status['lang']
		content["hash"] = hash(status["text"])  #if texts are identical, hash value is same
		if (content['lang'] in SUPPORTED_LANGUAGE) and ('media' in status['entities']):
			#if (content["hash"] not in twitter_list) : #or (content["hash"] in twitter_list and content['text'] not in twitter_list)
				content["textf"] = filter(status['text'])
				content["text"] = status["text"]
				content["entities"] = status['entities']
				content["retweet_count"] = status['retweet_count'] # return int
				content["favorite_count"] = status['favorite_count'] #return integer or Nullable
				twitter_list.append(content)
	return twitter_list

def filter(text):
	text = re.sub('RT \@+\w+\:','',text) #delete head of retweet
	text = re.sub('\#+\w+\s','',text)     #delete hashtag
	text = re.sub('https://t.co/+\w+.','',text)  #delete url
	text = re.sub('\@+\w+(\\n|\s)','',text)    #delete @people	
	text = re.sub('\n','',text)                #delete \n
	return text




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
	twitter_list= search_keyword(keyword_dic)
	
	for i in range(len(twitter_list)):
		print(twitter_list[i])
		print('\n')
	print(len(twitter_list))

