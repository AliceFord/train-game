import re
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		mainWidget = QWidget()
		mainLayout = QHBoxLayout()
		mainLayout.setAlignment(Qt.AlignTop)

		mainLayout.addWidget()

		mainWidget.setLayout(mainLayout)

		self.setCentralWidget(mainWidget)
		self.setWindowTitle("Train Game")
		self.setGeometry(50, 50, 200, 200)
		self.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	app.exec_()
