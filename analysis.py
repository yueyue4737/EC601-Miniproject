from communication import search_keyword, keyword_sentiment
# retrun the list of top 10 popular pictures of the keyword
# Input: arguments
# Output: List(Dict), the dictionary contains url of the original tweet,
#         expanded url (web page containing the video/photo), media url (https).
def get_picture_list(arguments):
	key_dict = arguments.keyword_dic
	tweet_list = search_keyword(key_dict)
	ordered_tweets = []
	for tweet_dict in tweet_list:
		total_count = tweet_dict["retweet_count"] + tweet_dict["favorite_count"]
		ordered_tweets.append((total_count, tweet_dict["entities"]))
	ordered_tweets.sort(key=lambda tweet_ : tweet_[0])  # sort the list in order of total_count

	return ordered_tweets[-10:]


# return the overall sentiment of the keyword (float range from -1 to 1)
# Input: arguments
# Output: ([-1, 1]+1)*50 --> [0, 100];using power instaed of count;
def get_keyword_sentiment(arguments):
	key_dict = arguments.keyword_dic
	tweet_list = search_keyword(key_dict)
	sentiment = 0
	sum_power = 0
	for tweet_dict in tweet_list:
		power = tweet_dict['retweet_count']+tweet_dict['favorite_count']
		sentiment += get_single_sentiment(tweet_dict)*power
		sum_power += power
	average_sentiment = ((sentiment/sum_power) + 1)* 50
	return average_sentiment


#
def get_single_sentiment(tweet_dict):
	return keyword_sentiment(tweet_dict)