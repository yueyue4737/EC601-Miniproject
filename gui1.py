import sys
# Core Functions except GUI
from PyQt5.QtCore import Qt
# UI components
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from analysis import get_keyword_sentiment, get_picture_list
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

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)  #?
		self.setWindowTitle("EC601 Mini Project1")

		self.layout1 = QVBoxLayout()
		self.layout2 = QHBoxLayout()
		self.layout3 = QHBoxLayout()
		self.layout4 = QHBoxLayout()

		self.title = QLabel("MiniProject1")
		title_font = self.title.font()
		title_font.setPointSize(30)
		self.title.setFont(title_font)
		self.layout1.addWidget(self.title)

		self.layout2.addWidget(QLabel("keyword:"))
		self.keyword = QLineEdit()
		self.keyword.setPlaceholderText("Enter the main keyword")
		self.layout2.addWidget(self.keyword)

		self.layout3.addWidget(QLabel("restriction word:"))
		self.restriction = QLineEdit()
		self.restriction.setPlaceholderText("Enter the restriction word")
		self.layout3.addWidget(self.restriction)

		self.sentiment_button = QPushButton('General sentiment')
		self.sentiment_button.clicked.connect(self.buildSentimentPopup)
		self.layout4.addWidget(self.sentiment_button)
		self.pics_button = QPushButton('Top 10 Pics')
		self.pics_button.clicked.connect(self.buildPicsPopup)
		self.layout4.addWidget(self.pics_button)
		
		self.layout1.addLayout(self.layout2)
		self.layout1.addLayout(self.layout3)
		self.layout1.addLayout(self.layout4)
		self.widget = QWidget()
		self.widget.setLayout(self.layout1)
		self.setCentralWidget(self.widget)

	def buildSentimentPopup(self, ):
		self.S_popup = SentimentPopup()
		argument = Argument()
		argument.add_argument('main_keyword', self.keyword.text())
		argument.add_argument('restriction', self.restriction.text())
		average_sentiment = get_keyword_sentiment(argument)
		self.S_popup.setText(average_sentiment, self.keyword.text())
		self.S_popup.show()

	def buildPicsPopup(self, ):
		self.P_popup = PicsPopup()
		argument = Argument()
		argument.add_argument('main_keyword', self.keyword.text())
		argument.add_argument('restriction', self.restriction.text())
		top_tweets = get_picture_list(argument)
		self.P_popup.display_pic(top_tweets)
		self.P_popup.show()


class SentimentPopup(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Keyword Sentiment")
		self.setGeometry(100,200,500,50)

	def setText(self, average_sentiment, keyword):
		if average_sentiment<37.5:
			self.text = "The average attitude on Twitter about " + keyword + " is negative."
		elif average_sentiment<62.5:
			self.text = "The average attitude on Twitter about " + keyword + " is neutral."
		else:
			self.text = "The average attitude on Twitter about " + keyword + " is positive."
		self.label = QLabel(self.text, self)

class PicsPopup(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Top 10 pictures")

	def display_pic(self, top_tweets):
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		scroll = QScrollArea(self)
		self.layout.addWidget(scroll)
		scroll.setWidgetResizable(True)
		scrollContent = QWidget(scroll)
		scrollLayout = QVBoxLayout(scrollContent)
		scrollContent.setLayout(scrollLayout)

		max_W = 0
		sum_H = 0
		label = []
		for idx, tweet_ in enumerate(top_tweets):
			file_path, file_type = get_pic(tweet_[1], idx)
			label.append(QLabel(self))
			pixmap = QPixmap(file_path)
			if pixmap.width() > max_W:
				max_W = pixmap.width()
			sum_H += pixmap.height()
			label[idx].setPixmap(pixmap)
			scrollLayout.addWidget(label[idx])

		scroll.setWidget(scrollContent)
		self.resize(max_W, sum_H)


if __name__ == "__main__":
	app = QApplication(sys.argv)

	mainWindow = MainWindow()
	picsWindow = PicsPopup()
	mainWindow.show() 
	app.exec_()