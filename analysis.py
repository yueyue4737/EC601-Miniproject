from communication import search_keyword, keyword_sentiment
# retrun the list of top 10 popular pictures of the keyword
# Input: arguments
# Output: List((count, Dict)), the dictionary contains url of the original tweet,
#         expanded url (web page containing the video/photo), media url (https)...
def get_picture_list(arguments):
	key_dict = arguments.keyword_dic
	tweet_list = search_keyword(key_dict, arguments.function_name)
	ordered_tweets = []
	for tweet_dict in tweet_list:
		total_count = tweet_dict["retweet_count"] + tweet_dict["favorite_count"]
		ordered_tweets.append((total_count, tweet_dict["entities"]))
	ordered_tweets.sort(key=lambda tweet_ : tweet_[0])  # sort the list in order of total_count

	tmp_list = ordered_tweets[len(ordered_tweets)-10:len(ordered_tweets)]
	tmp_list.reverse()
	ordered_tweets = tmp_list
	return ordered_tweets


# return the overall sentiment of the keyword (float range from -1 to 1)
# Input: arguments
# Output: ([-1, 1]+1)*50 --> [0, 100];
def get_keyword_sentiment(arguments):
	key_dict = arguments.keyword_dic
	tweet_list = search_keyword(key_dict, arguments.function_name)
	sentiment = 0
	sum_power = 0
	for tweet_dict in tweet_list:
		count = tweet_dict['retweet_count']+tweet_dict['favorite_count']
		score, magnitude = get_single_sentiment(tweet_dict)
		sentiment += score*count*magnitude
		sum_power += count*magnitude
	average_sentiment = ((sentiment/sum_power) + 1)* 50
	return average_sentiment


#
def get_single_sentiment(tweet_dict):
	return keyword_sentiment(tweet_dict)