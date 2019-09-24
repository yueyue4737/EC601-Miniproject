import sys
# Core Functions except GUI
from PyQt5.QtCore import Qt
# UI components
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)  #?
		self.setWindowTitle("EC601 Mini Project1")

		layout1 = QVBoxLayout()
		layout2 = QHBoxLayout()
		layout3 = QHBoxLayout()
		layout4 = QHBoxLayout()

		title = QLabel("MiniProject1")
		title_font = title.font()
		title_font.setPointSize(30)
		title.setFont(title_font)
		layout1.addWidget(title)

		layout2.addWidget(QLabel("keyword:"))
		keyword = QLineEdit()
		keyword.setPlaceholderText("Enter the main keyword")
		layout2.addWidget(keyword)

		layout3.addWidget(QLabel("restriction word:"))
		restriction = QLineEdit()
		restriction.setPlaceholderText("Enter the restriction word")
		layout3.addWidget(restriction)

		sentiment_button = QPushButton('General sentiment')
		sentiment_button.clicked.connect(self.buildSentimentPopup)
		layout4.addWidget(sentiment_button)
		pics_button = QPushButton('Top 10 Pics')
		pics_button.clicked.connect(self.buildpicsWindow)
		layout4.addWidget(pics_button)
		
		layout1.addLayout( layout2 )
		layout1.addLayout( layout3 )
		layout1.addLayout( layout4 )
		widget = QWidget()
		widget.setLayout(layout1)
		self.setCentralWidget(widget)

	def buildSentimentPopup(self):
		self.Popup = SentimentPopup(self)
		self.Popup.show()

	def buildpicsWindow(self):
		self.aa = PicsPopup()
		self.aa.show()



class SentimentPopup(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Sentiment of",)
		self.text = "test"
		self.label = QLabel(self.text, self)
class PicsPopup(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Top 10 pics of")
		self.initUI()
	def initUI(self):
		label = QLabel(self)
		pixmap = QPixmap('pic1.jpg')
		label.setPixmap(pixmap)
		self.resize(pixmap.width(), pixmap.height())



if __name__ == "__main__":
	app = QApplication(sys.argv)

	mainWindow = MainWindow()
	picsWindow = PicsPopup()
	mainWindow.show() 
	app.exec_()