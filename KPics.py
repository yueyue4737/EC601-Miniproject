'''
'''
import UI
from communication import 
from analysis import get_picture_list, get_sentiment

exit_ = False  # if the user want to exit

# Welcome users and output the usage information.
UI.hello_message()
UI.usage_info()
while exit_== False:
  # Print the input instructions, split the arguments and do validation checking.
  arguments, exit_ = UI.get_input()
  # We may need to store something. But for now, just leave it blank

  # Find out which function the user choose
  if arguments.fuction_name == 'picture_list':
    # Call get_picture_list and get top popular pics, but the return type is not decided yet.
    UI.display_pic(?)
  elif arguments.fuction_name == 'keyword_sentiment':
    # Likewise, call get_sentiment. But the return type is not decided.
    UI.display_sentiment(?)