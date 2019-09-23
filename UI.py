from PIL import Image
from analysis import get_picture_list,get_keyword_sentiment
from storage import get_pic


# A class used by get_input to store arguments that user enters.
# Arguments are stored in a dictionary:
# "main_keyword": the keyword user want to search
# "restriction": some restriction user added for the search
class Argument:
	def __init__(self, ):
		self.function_name = ''
		self.keyword_dic = {}

	def add_argument(self, key, value):
		self.keyword_dic[key] = value

	def add_type(self, type_):
		self.function_name = type_


# Print hello message and usage information.
def hello_message():
	print('Hello!')

# Print usage information
def usage_info():
	print("Which kind of function do you want to use?:\n")
	print("Enter 1 to get top ten popular pictures!\n")
	print("Enter 2 to get the sentiment\n")

# Display the top popular
def display_pic(top_tweets):
	for idx, tweet_ in enumerate(top_tweets):
		file_path, file_type = get_pic(tweet_[1], idx)
		img = Image.open(file_path)
		img.show()
		#img.close()
		print(file_type)

def display_sentiment(average_sentiment,keyword):
	if average_sentiment<37.5:
		print("The average attitude on Twitter about " + keyword + " is negative.")
	elif average_sentiment<62.5:
		print("The average attitude on Twitter about " + keyword + " is neutral.")
	else:
		print("The average attitude on Twitter about " + keyword + " is positive.")
		
#simple interface.
def get_input():
	arguments = Argument()
	quit_ = input("Do you want to exit? Enter [y/n]\n")
	exit_ = False
	if quit_ == 'y':
		exit_ = True
		return arguments, exit_

	name = input("Please enter a Kpop singer's name you want to search:\n")
	arguments.add_argument('main_keyword', name)
	restriction = input("You can add restriction word for searching:\n")
	arguments.add_argument('restriction', restriction)

	valid = False
	while valid == False:
		usage_info()
		function_type = input("")
		if function_type == '1':
			valid = True
			arguments.add_type('picture_list')
		elif function_type == '2':
			valid = True
			arguments.add_type('keyword_sentiment')
		else:
			print('Invalid fucntion! Please Enter again.')

	return arguments, exit_

if __name__ == '__main__':
	test_argument=get_input()
	print(test_argument.function_name)
	print(test_argument.keyword_dic)
