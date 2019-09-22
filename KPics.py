'''
'''
import UI
from analysis import get_picture_list, get_keyword_sentiment

exit_ = False  # if the user want to exit

# Welcome users and output the usage information.
UI.hello_message()
while exit_== False:
  # Print the input instructions, split the arguments and do validation checking.
  arguments, exit_ = UI.get_input()
  if exit_ == False:
    # Find out which function the user choose
    if arguments.function_name == 'picture_list':
      top_tweets = get_picture_list(arguments)
      UI.display_pic(top_tweets)
    elif arguments.function_name == 'keyword_sentiment':
      average_sentiment = get_keyword_sentiment(arguments)
      UI.display_sentiment(average_sentiment, arguments.keyword_dic["main_keyword"])