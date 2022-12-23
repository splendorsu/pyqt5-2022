# change_icon.py

#  https://codetorial.net/pyqt5/index.html
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QLabel, QPushButton, QVBoxLayout, QWidget,)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import random

class ChangeIcon(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 600, 400) # 창 위치 지정
		self.setWindowTitle("안녕하세요") # 창 캡션
		self.setWindowIcon(QIcon("images/banana.png"))
		self.createMenu()
		self.createWidgets()
		self.show() 
	
	def createWidgets(self):
		info_label = QLabel("버튼을 클릭하셔서, 과일을 선택하세요")
		self.images = [
			"images/pineapple.png",
			"images/watermelon.png",
			"images/banana.png",
			]
		self.icon_button = QPushButton()
		self.icon_button.setIcon(QIcon(random.choice(self.images)))
		self.icon_button.setIconSize(QSize(60, 60))
		self.icon_button.clicked.connect(self.changeIcon)

		v_box = QVBoxLayout()
		v_box.addStretch(2)
		v_box.addWidget(info_label)
		v_box.addWidget(self.icon_button)
		v_box.addStretch(1)

		widget = QWidget()
		widget.setLayout(v_box)
		self.setCentralWidget(widget)

	def changeIcon(self):
		self.icon_button.setIcon(QIcon(random.choice(self.images)))
		self.icon_button.setIconSize(QSize(60, 60))

	def createMenu(self):
		exit_act = QAction("Exit", self)
		exit_act.setShortcut("Ctrl+Q")
		exit_act.triggered.connect(self.close)
		
		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu("File")
		file_menu.addAction(exit_act)

if __name__ ==  '__main__' :
	app = QApplication(sys.argv)		
	window = ChangeIcon()
	sys.exit(app.exec_())