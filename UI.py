from PIL import Image
import numpy as np

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
def display_pic():
	return;

def display_sentiment():
	return;
  
#simple interface.
def get_input():
	arguments = Argument()
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

	return arguments

if __name__ == '__main__':
	test_argument=get_input()
	print(test_argument.function_name)
	print(test_argument.keyword_dic)
